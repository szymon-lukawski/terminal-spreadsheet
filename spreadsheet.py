class Cell:
    pass


class Spreadsheet:
    def __init__(self, dims: tuple[int, int]):
        self.n_columns, self.n_rows = dims
        self.grid: list[list[Cell]] = None
        self._create_empty_grid(*dims)

    def _create_empty_grid(self, n_columns, n_rows):
        self.grid = [[None for col_i in range(n_columns)] for row_i in range(n_rows)]
