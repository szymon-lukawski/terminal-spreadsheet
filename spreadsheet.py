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
        lines = [self.name, ""]  # Add name and placeholder for column names
        col_lens = self._initialize_column_lengths()
        lines.extend(self._generate_row_lines(col_lens))
        lines[1] = self._generate_column_titles(col_lens)
        return "\n".join(lines)

    def _initialize_column_lengths(self):
        return [1 for _ in range(self.n_columns)]

    def _generate_row_lines(self, col_lens):
        lines = []
        for row_i, row in enumerate(self.grid):
            line = self._generate_row_line(row, row_i, col_lens)
            lines.append(line)
        return lines

    def _generate_row_line(self, row, row_i, col_lens):
        row_title_padding = (len(str(self.n_rows)) - len(str(row_i + 1))) * " "
        line = [str(row_i + 1) + row_title_padding]
        for col_idx, cell in enumerate(row):
            line.append(self._format_cell(cell, col_idx, col_lens))
        return self._col_sep.join(line)

    def _format_cell(self, cell, col_idx, col_lens):
        if cell:
            col_lens[col_idx] = max(col_lens[col_idx], len(cell))
            return str(cell)
        return self._empty_cell_repr

    def _generate_column_titles(self, col_lens):
        col_title_line = [len(str(self.n_rows)) * " "]
        for col_i, max_col_len in enumerate(col_lens):
            col_title_line.append(self._format_column_title(col_i, max_col_len))
        return self._col_sep.join(col_title_line)

    def _format_column_title(self, col_idx, max_col_len):
        col_title = self._col_idx_to_str(col_idx)
        padding = (max_col_len - len(col_title)) * " "
        return padding + col_title


    def _col_idx_to_str(self, col_idx):
        if col_idx > 25: 
            raise NotImplementedError("Column index can be 0-25 for now!")
        return ascii_uppercase[col_idx]

        


                


        

    def change_(self, address: str, value: str):
        pass
