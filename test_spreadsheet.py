from spreadsheet import Spreadsheet


def test_spreadsheet_creation():
    sheet = Spreadsheet((1, 2))
    assert sheet.n_columns == 1
    assert sheet.n_rows == 2
    assert sheet.grid == [[None], [None]]
