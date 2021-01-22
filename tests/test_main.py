from typing import Any

import pytest

from piplicenses.__main__ import get_packages, get_sortby
from piplicenses.argparse import CompatibleArgumentParser
from piplicenses.const import OrderArg

from .conftest import UNICODE_APPENDIX


@pytest.mark.parametrize('kwargs,field_name', [
    ({'order': OrderArg.NAME}, 'Name'),
    ({'order': OrderArg.LICENSE}, 'License'),
    ({'order': OrderArg.AUTHOR, 'with_authors': True}, 'Author'),
    ({'order': OrderArg.URL, 'with_urls': True}, 'URL'),
    ({'order': OrderArg.URL}, 'Name'),
    ({'order': OrderArg.COUNT, 'summary': True}, 'Count'),
    ({'order': OrderArg.NAME, 'summary': True}, 'License'),
])
def test_order(kwargs: Any, field_name: str):
    assert get_sortby(**kwargs) == field_name


def test_without_filter(parser: CompatibleArgumentParser):
    args = parser.parse_args([])
    packages = list(get_packages(**vars(args)))
    assert UNICODE_APPENDIX in packages[-1]["name"]


def test_with_default_filter(parser: CompatibleArgumentParser):
    args = parser.parse_args(["--filter-strings"])
    packages = list(get_packages(**vars(args)))
    assert UNICODE_APPENDIX not in packages[-1]["name"]


def test_with_specified_filter(parser: CompatibleArgumentParser):
    args = parser.parse_args(["--filter-strings", "--filter-code-page=ascii"])
    packages = list(get_packages(**vars(args)))
    assert UNICODE_APPENDIX not in packages[-1]["summary"]
