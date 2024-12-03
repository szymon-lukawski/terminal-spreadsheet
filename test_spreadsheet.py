from spreadsheet import Spreadsheet, Cell


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


def test_str_not_empty_spreadsheet_1_by_1_one_letter_formula():
    sheet = Spreadsheet("", (1, 1))
    sheet.grid[0][0] = Cell('L')
    sheet.refresh()
    assert str(sheet) == "\n |A\n1|L"

def test_str_not_empty_spreadsheet_1_by_1_two_letter_formula():
    sheet = Spreadsheet("", (1, 1))
    sheet.grid[0][0] = Cell('LL')
    sheet.refresh()
    assert str(sheet) == "\n | A\n1|LL"

def test_str_not_empty_spreadsheet_1_by_1_three_letter_formula():
    sheet = Spreadsheet("", (1, 1))
    sheet.grid[0][0] = Cell('LLL')
    sheet.refresh()
    assert str(sheet) == "\n |  A\n1|LLL"

def test_str_not_empty_spreadsheet_2_by_1_three_letter_formula():
    sheet = Spreadsheet("", (2, 1))
    sheet.grid[0][0] = Cell('LLL')
    sheet.refresh()
    assert str(sheet) == "\n |  A|B\n1|LLL| "

def test_str_not_empty_spreadsheet_2_by_1_three_letter_formula_in_second_column():
    sheet = Spreadsheet("", (2, 1))
    sheet.grid[0][1] = Cell('LLL')
    sheet.refresh()
    assert str(sheet) == "\n |A|  B\n1| |LLL"