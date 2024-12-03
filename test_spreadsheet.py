from spreadsheet import Spreadsheet


def test_spreadsheet_creation():
    sheet = Spreadsheet("", (1, 2))
    assert sheet.name == ""
    assert sheet.n_columns == 1
    assert sheet.n_rows == 2
    assert sheet.grid == [[None], [None]]


def test_str_empty_spreadsheet_1_by_1():
    sheet = Spreadsheet("", (1, 1))
    assert str(sheet) == "\n |A\n1| "


def test_str_empty_spreadsheet_2_by_1():
    sheet = Spreadsheet("", (2, 1))
    assert str(sheet) == "\n |A|B\n1| | "


def test_str_empty_spreadsheet_1_by_2():
    sheet = Spreadsheet("", (1, 2))
    assert str(sheet) == "\n |A\n1| \n2| "


def test_str_empty_spreadsheet_2_by_2():
    sheet = Spreadsheet("", (2, 2))
    assert str(sheet) == "\n |A|B\n1| | \n2| | "


def test_str_empty_spreadsheet_3_by_2():
    sheet = Spreadsheet("", (3, 2))
    assert str(sheet) == "\n |A|B|C\n1| | | \n2| | | "
