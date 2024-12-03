from string import ascii_uppercase
class Cell:
    pass


class Spreadsheet:
    def __init__(self, name: str, dims: tuple[int, int]):
        self.name = name
        self.n_columns, self.n_rows = dims
        self.grid: list[list[Cell]] = None
        self._create_empty_grid(*dims)
        self._col_sep = "|"
        self._empty_cell_repr = " "

    def _create_empty_grid(self, n_columns, n_rows):
        self.grid = [[None for _ in range(n_columns)] for _ in range(n_rows)]

    def __str__(self):
        lines = []
        lines.append(self.name)
        lines.append("") # Placeholder for column name row
        col_lens = [1 for _ in range(self.n_columns)]
        for row_i, row in enumerate(self.grid):
            row_title_padding = (len(str(self.n_rows)) - len(str(row_i+1))) * " "
            line = [str(row_i+1) + row_title_padding]
            for col_idx, cell in enumerate(row):
                if cell:
                    col_lens[col_idx] = max(col_lens[col_idx], len(cell))
                    line.append(str(cell)) # add padding 
                else:
                    # cell is None
                    line.append(self._empty_cell_repr)
            line = self._col_sep.join(line)
            lines.append(line)
        col_title_line = [len(str(self.n_rows))* " "]
        for col_i, max_col_len in enumerate(col_lens):
            col_title = self._col_idx_to_str(col_i)
            len_col_title = len(col_title)
            padded_col_title = (max_col_len-len_col_title) * " " + col_title # this line needs to be changed if different allignment
            col_title_line.append(padded_col_title)
        lines[1] = self._col_sep.join(col_title_line)
        return "\n".join(lines)

    def _col_idx_to_str(self, col_idx):
        if col_idx > 25: 
            raise NotImplementedError("Column index can be 0-25 for now!")
        return ascii_uppercase[col_idx]

        


                


        

    def change_(self, address: str, value: str):
        pass
