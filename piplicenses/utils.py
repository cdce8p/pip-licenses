# ---------------------------------------------------------------------------
# Licensed under the MIT License. See LICENSE file for license information.
# ---------------------------------------------------------------------------
import sys
from enum import Enum
from functools import partial
from typing import Any, List

from .const import FormatArg, NoValueEnum


def value_to_enum_key(value: str) -> str:
    return value.replace('-', '_').upper()


def enum_key_to_value(enum_key: Enum) -> str:
    return enum_key.name.replace('_', '-').lower()


def choices_from_enum(enum_cls: NoValueEnum) -> List[str]:
    return [key.replace('_', '-').lower()
            for key in enum_cls.__members__.keys()]


def create_warn_string(
        *,
        format_: FormatArg = FormatArg.PLAIN,
        summary: bool = False,
        with_license_file: bool = False,
        with_authors: bool = False,
        with_urls: bool = False,
        **kwargs: Any,
) -> str:
    warn_messages = []
    warn = partial(output_colored, '33')

    if with_license_file and not format_ == FormatArg.JSON:
        message = warn(('Due to the length of these fields, this option is '
                        'best paired with --format=json.'))
        warn_messages.append(message)

    if summary and (with_authors or with_urls):
        message = warn(('When using this option, only --order=count or '
                        '--order=license has an effect for the --order '
                        'option. And using --with-authors and --with-urls '
                        'will be ignored.'))
        warn_messages.append(message)

    return '\n'.join(warn_messages)


def output_colored(code, text, is_bold=False):
    """
    Create function to output with color sequence
    """
    if is_bold:
        code = '1;%s' % code

    return '\033[%sm%s\033[0m' % (code, text)


def save_if_needs(output_file, output_string):
    """
    Save to path given by args
    """
    if output_file is None:
        return

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(output_string)
        sys.stdout.write('created path: ' + output_file + '\n')
        sys.exit(0)
    except IOError:
        sys.stderr.write('check path: --output-file\n')
        sys.exit(1)
