# ---------------------------------------------------------------------------
# Licensed under the MIT License. See LICENSE file for license information.
# ---------------------------------------------------------------------------
import sys
from collections import Counter
from typing import Any, List, Optional

from .argparse import create_parser
from .const import (
    DEFAULT_OUTPUT_FIELDS, FIELDS_TO_METADATA_KEYS, LICENSE_UNKNOWN,
    SUMMARY_FIELD_NAMES, SUMMARY_OUTPUT_FIELDS, SYSTEM_PACKAGES,
    CustomNamespace, FormatArg, FromArg, OrderArg)
from .parse import get_pkg_info, select_license_by_source
from .table import factory_styled_table_with_args
from .utils import create_warn_string, save_if_needs

try:
    from pip._internal.utils.misc import get_installed_distributions
except ImportError:  # pragma: no cover
    from pip import get_installed_distributions


def get_packages(
    *,
    from_: FromArg,
    ignore_packages: Optional[List[str]] = None,
    with_system: bool = False,
    filter_strings: bool = False,
    filter_code_page: str = 'latin1',
    fail_on: Optional[str] = None,
    allow_only: Optional[str] = None,
    **kwargs: Any,
):
    pkgs = get_installed_distributions()
    ignore_pkgs_as_lower = [pkg.lower() for pkg in ignore_packages or []]

    fail_on_licenses = None
    if fail_on:
        fail_on_licenses = fail_on.split(";")

    allow_only_licenses = None
    if allow_only:
        allow_only_licenses = allow_only.split(";")

    for pkg in pkgs:
        pkg_name = pkg.project_name

        if pkg_name.lower() in ignore_pkgs_as_lower:
            continue

        if not with_system and pkg_name in SYSTEM_PACKAGES:
            continue

        pkg_info = get_pkg_info(pkg, filter_strings, filter_code_page)

        license_name = select_license_by_source(
            from_,
            pkg_info['license_classifier'],
            pkg_info['license'])

        if fail_on_licenses and license_name in fail_on_licenses:
            sys.stderr.write("fail-on license {} was found for package "
                             "{}:{}".format(
                                license_name,
                                pkg_info['name'],
                                pkg_info['version'])
                             )
            sys.exit(1)

        if allow_only_licenses and license_name not in allow_only_licenses:
            sys.stderr.write("license {} not in allow-only licenses was found"
                             " for package {}:{}".format(
                                license_name,
                                pkg_info['name'],
                                pkg_info['version'])
                             )
            sys.exit(1)

        yield pkg_info


def create_licenses_table(
        args: CustomNamespace, output_fields=DEFAULT_OUTPUT_FIELDS):
    table = factory_styled_table_with_args(args.format_, output_fields)

    for pkg in get_packages(**vars(args)):
        row = []
        for field in output_fields:
            if field == 'License':
                license_str = select_license_by_source(
                    args.from_, pkg['license_classifier'], pkg['license'])
                row.append(license_str)
            elif field == 'License-Classifier':
                row.append(', '.join(pkg['license_classifier'])
                           or LICENSE_UNKNOWN)
            elif field.lower() in pkg:
                row.append(pkg[field.lower()])
            else:
                row.append(pkg[FIELDS_TO_METADATA_KEYS[field]])
        table.add_row(row)

    return table


def create_summary_table(args: CustomNamespace):
    counts = Counter(pkg['license'] for pkg in get_packages(**vars(args)))

    table = factory_styled_table_with_args(args.format_, SUMMARY_FIELD_NAMES)
    for license, count in counts.items():
        table.add_row([count, license])
    return table


def get_output_fields(args: CustomNamespace):
    if args.summary:
        return list(SUMMARY_OUTPUT_FIELDS)

    output_fields = list(DEFAULT_OUTPUT_FIELDS)

    if args.from_ == FromArg.ALL:
        output_fields.append('License-Metadata')
        output_fields.append('License-Classifier')
    else:
        output_fields.append('License')

    if args.with_authors:
        output_fields.append('Author')

    if args.with_urls:
        output_fields.append('URL')

    if args.with_description:
        output_fields.append('Description')

    if args.with_license_file:
        if not args.no_license_path:
            output_fields.append('LicenseFile')

        output_fields.append('LicenseText')

        if args.with_notice_file:
            output_fields.append('NoticeText')
            if not args.no_license_path:
                output_fields.append('NoticeFile')

    return output_fields


def get_sortby(
        order: OrderArg, *,
        summary: bool = False,
        with_authors: bool = False,
        with_urls: bool = False,
        **kwargs: Any,
) -> str:
    if summary and order == OrderArg.COUNT:
        return 'Count'
    elif summary or order == OrderArg.LICENSE:
        return 'License'
    elif order == OrderArg.NAME:
        return 'Name'
    elif order == OrderArg.AUTHOR and with_authors:
        return 'Author'
    elif order == OrderArg.URL and with_urls:
        return 'URL'

    return 'Name'


def create_output_string(args: CustomNamespace):
    output_fields = get_output_fields(args)

    if args.summary:
        table = create_summary_table(args)
    else:
        table = create_licenses_table(args, output_fields)

    sortby = get_sortby(**vars(args))

    if args.format_ == FormatArg.HTML:
        return table.get_html_string(fields=output_fields, sortby=sortby)
    else:
        return table.get_string(fields=output_fields, sortby=sortby)


def main():  # pragma: no cover
    parser = create_parser()
    args = parser.parse_args()

    output_string = create_output_string(args)

    output_file = args.output_file
    save_if_needs(output_file, output_string)

    print(output_string)
    warn_string = create_warn_string(**vars(args))
    if warn_string:
        print(warn_string, file=sys.stderr)


if __name__ == '__main__':  # pragma: no cover
    main()
