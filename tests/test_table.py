from piplicenses.const import FormatArg
from piplicenses.table import RULE_FRAME, factory_styled_table_with_args


def test_format_plain():
    table = factory_styled_table_with_args(FormatArg.PLAIN)
    assert 'l' in table.align.values()
    assert table.border is False
    assert table.header is True
    assert table.junction_char == '+'
    assert table.hrules == RULE_FRAME
