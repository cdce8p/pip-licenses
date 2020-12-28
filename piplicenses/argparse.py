import argparse
import codecs
import sys

from .const import __summary__, __version__


class ArgumentParser(argparse.ArgumentParser):
    def parse_args(self, args=None, namespace=None):
        args = super().parse_args(args, namespace)
        self._compatible_format_args(args)
        self._check_code_page(args.filter_code_page)

        return args

    @staticmethod
    def _check_code_page(code_page):
        try:
            codecs.lookup(code_page)
        except LookupError:
            print(("error: invalid code page '%s' given for "
                   "--filter-code-page;\n"
                   "       check https://docs.python.org/3/library/"
                   "codecs.html for valid code pages") % code_page)
            sys.exit(1)

    @staticmethod
    def _compatible_format_args(args):
        from_input = getattr(args, 'from').lower()
        order_input = args.order.lower()
        format_input = args.format.lower()

        # XXX: Use enum when drop support Python 2.7
        if from_input in ('meta', 'm'):
            setattr(args, 'from', 'meta')

        if from_input in ('classifier', 'c'):
            setattr(args, 'from', 'classifier')

        if from_input in ('mixed', 'mix'):
            setattr(args, 'from', 'mixed')

        if order_input in ('count', 'c'):
            args.order = 'count'

        if order_input in ('license', 'l'):
            args.order = 'license'

        if order_input in ('name', 'n'):
            args.order = 'name'

        if order_input in ('author', 'a'):
            args.order = 'author'

        if order_input in ('url', 'u'):
            args.order = 'url'

        if format_input in ('plain', 'p'):
            args.format = 'plain'

        if format_input in ('markdown', 'md', 'm'):
            args.format = 'markdown'

        if format_input in ('rst', 'rest', 'r'):
            args.format = 'rst'

        if format_input in ('confluence', 'c'):
            args.format = 'confluence'

        if format_input in ('html', 'h'):
            args.format = 'html'

        if format_input in ('json', 'j'):
            args.format = 'json'

        if format_input in ('json-license-finder', 'jlf'):
            args.format = 'json-license-finder'

        if format_input in ('csv', ):
            args.format = 'csv'


def create_parser():
    parser = ArgumentParser(description=__summary__)
    parser.add_argument('-v', '--version',
                        action='version',
                        version='%(prog)s ' + __version__)
    parser.add_argument('--from',
                        action='store', type=str,
                        default='mixed', metavar='SOURCE',
                        help=('where to find license information\n'
                              '"meta", "classifier, "mixed", "all"\n'
                              'default: --from=mixed'))
    parser.add_argument('-s', '--with-system',
                        action='store_true',
                        default=False,
                        help='dump with system packages')
    parser.add_argument('-a', '--with-authors',
                        action='store_true',
                        default=False,
                        help='dump with package authors')
    parser.add_argument('-u', '--with-urls',
                        action='store_true',
                        default=False,
                        help='dump with package urls')
    parser.add_argument('-d', '--with-description',
                        action='store_true',
                        default=False,
                        help='dump with short package description')
    parser.add_argument('-l', '--with-license-file',
                        action='store_true',
                        default=False,
                        help='dump with location of license file and '
                             'contents, most useful with JSON output')
    parser.add_argument('--no-license-path',
                        action='store_true',
                        default=False,
                        help='when specified together with option -l, '
                             'suppress location of license file output')
    parser.add_argument('--with-notice-file',
                        action='store_true',
                        default=False,
                        help='when specified together with option -l, '
                             'dump with location of license file and contents')
    parser.add_argument('-i', '--ignore-packages',
                        action='store', type=str,
                        nargs='+', metavar='PKG',
                        default=[],
                        help='ignore package name in dumped list')
    parser.add_argument('-o', '--order',
                        action='store', type=str,
                        default='name', metavar='COL',
                        help=('order by column\n'
                              '"name", "license", "author", "url"\n'
                              'default: --order=name'))
    parser.add_argument('-f', '--format',
                        action='store', type=str,
                        default='plain', metavar='STYLE',
                        help=('dump as set format style\n'
                              '"plain", "plain-vertical" "markdown", "rst", \n'
                              '"confluence", "html", "json", \n'
                              '"json-license-finder",  "csv"\n'
                              'default: --format=plain'))
    parser.add_argument('--filter-strings',
                        action="store_true",
                        default=False,
                        help=('filter input according to code page'))
    parser.add_argument('--filter-code-page',
                        action="store", type=str,
                        default="latin1",
                        help=('specify code page for filtering'))
    parser.add_argument('--summary',
                        action='store_true',
                        default=False,
                        help='dump summary of each license')
    parser.add_argument('--output-file',
                        action='store', type=str,
                        help='save license list to file')
    parser.add_argument('--fail-on',
                        action='store', type=str,
                        default=None,
                        help='fail (exit with code 1) on the first occurrence '
                             'of the licenses of the semicolon-separated list')
    parser.add_argument('--allow-only',
                        action='store', type=str,
                        default=None,
                        help='fail (exit with code 1) on the first occurrence '
                             'of the licenses not in the semicolon-separated '
                             'list')

    return parser
