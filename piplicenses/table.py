from prettytable import PrettyTable

from .const import DEFAULT_OUTPUT_FIELDS

try:
    from prettytable.prettytable import ALL as RULE_ALL
    from prettytable.prettytable import FRAME as RULE_FRAME
    from prettytable.prettytable import HEADER as RULE_HEADER
    from prettytable.prettytable import NONE as RULE_NONE
except ImportError:  # pragma: no cover
    from prettytable import ALL as RULE_ALL
    from prettytable import FRAME as RULE_FRAME
    from prettytable import HEADER as RULE_HEADER
    from prettytable import NONE as RULE_NONE


class JsonPrettyTable(PrettyTable):
    """PrettyTable-like class exporting to JSON"""

    def _format_row(self, row, options):
        resrow = {}
        for (field, value) in zip(self._field_names, row):
            if field not in options["fields"]:
                continue

            resrow[field] = value

        return resrow

    def get_string(self, **kwargs):
        # import included here in order to limit dependencies
        # if not interested in JSON output,
        # then the dependency is not required
        import json

        options = self._get_options(kwargs)
        rows = self._get_rows(options)
        formatted_rows = self._format_rows(rows, options)

        lines = []
        for row in formatted_rows:
            lines.append(row)

        return json.dumps(lines, indent=2, sort_keys=True)


class JsonLicenseFinderTable(JsonPrettyTable):
    def _format_row(self, row, options):
        resrow = {}
        for (field, value) in zip(self._field_names, row):
            if field == 'Name':
                resrow['name'] = value

            if field == 'Version':
                resrow['version'] = value

            if field == 'License':
                resrow['licenses'] = [value]

        return resrow

    def get_string(self, **kwargs):
        # import included here in order to limit dependencies
        # if not interested in JSON output,
        # then the dependency is not required
        import json

        options = self._get_options(kwargs)
        rows = self._get_rows(options)
        formatted_rows = self._format_rows(rows, options)

        lines = []
        for row in formatted_rows:
            lines.append(row)

        return json.dumps(lines, sort_keys=True)


class CSVPrettyTable(PrettyTable):
    """PrettyTable-like class exporting to CSV"""

    def get_string(self, **kwargs):

        def esc_quotes(val):
            """
            Meta-escaping double quotes
            https://tools.ietf.org/html/rfc4180
            """
            try:
                return val.replace('"', '""')
            except UnicodeDecodeError:  # pragma: no cover
                return val.decode('utf-8').replace('"', '""')
            except UnicodeEncodeError:  # pragma: no cover
                return val.encode('unicode_escape').replace('"', '""')

        options = self._get_options(kwargs)
        rows = self._get_rows(options)
        formatted_rows = self._format_rows(rows, options)

        lines = []
        formatted_header = ','.join(['"%s"' % (esc_quotes(val), )
                                     for val in self._field_names])
        lines.append(formatted_header)
        for row in formatted_rows:
            formatted_row = ','.join(['"%s"' % (esc_quotes(val), )
                                      for val in row])
            lines.append(formatted_row)

        return '\n'.join(lines)


class PlainVerticalTable(PrettyTable):
    """PrettyTable for outputting to a simple non-column based style.

    When used with --with-license-file, this style is similar to the default
    style generated from Angular CLI's --extractLicenses flag.
    """

    def get_string(self, **kwargs):
        options = self._get_options(kwargs)
        rows = self._get_rows(options)

        output = ''
        for row in rows:
            for v in row:
                output += '{}\n'.format(v)
            output += '\n'

        return output


def factory_styled_table_with_args(args, output_fields=DEFAULT_OUTPUT_FIELDS):
    table = PrettyTable()
    table.field_names = output_fields
    table.align = 'l'
    table.border = (args.format == 'markdown' or args.format == 'rst' or
                    args.format == 'confluence' or args.format == 'json')
    table.header = True

    if args.format == 'markdown':
        table.junction_char = '|'
        table.hrules = RULE_HEADER
    elif args.format == 'rst':
        table.junction_char = '+'
        table.hrules = RULE_ALL
    elif args.format == 'confluence':
        table.junction_char = '|'
        table.hrules = RULE_NONE
    elif args.format == 'json':
        table = JsonPrettyTable(table.field_names)
    elif args.format == 'json-license-finder':
        table = JsonLicenseFinderTable(table.field_names)
    elif args.format == 'csv':
        table = CSVPrettyTable(table.field_names)
    elif args.format == 'plain-vertical':
        table = PlainVerticalTable(table.field_names)

    return table
