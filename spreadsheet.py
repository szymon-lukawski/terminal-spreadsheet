from string import ascii_uppercase
from parsing import parse_formula


class Cell:
    def __init__(self, formula: str):
        self.formula = formula
        self.value = None

    def __repr__(self):
        return self.formula

    def __str__(self):
        return str(self.value)
    
    def __len__(self):
        return len(self.value)

    def refresh(self):
        if self.formula and len(self.formula) > 0 and self.formula[0] == '=':
            self.value = parse_formula(self.formula)
        else:
            self.value = self.formula



class Spreadsheet:
    def __init__(self, name: str, dims: tuple[int, int]):
        self.name = name
        self.n_columns, self.n_rows = dims
        self.grid: list[list[Cell]] = None
        self._create_empty_grid(*dims)
        self._col_sep = "|"
        self._empty_cell_repr = " "

    def refresh(self):
        for row in self.grid:
            for cell in row:
                if cell is not None:
                    cell.refresh()

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
        if cell is not None:
            cell_str = str(cell)
            col_lens[col_idx] = max(col_lens[col_idx], len(cell_str))
            
            return " "*(col_lens[col_idx]-len(cell_str)) + cell_str
        return " "*(col_lens[col_idx]-len(self._empty_cell_repr)) + self._empty_cell_repr

    def _generate_column_titles(self, col_lens):
        col_title_line = [len(str(self.n_rows)) * " "]
        for col_i, max_col_len in enumerate(col_lens):
            col_title_line.append(self._format_column_title(col_i, max_col_len))
        return self._col_sep.join(col_title_line)

    def _format_column_title(self, col_idx, max_col_len):
        col_title = self._col_idx_to_str(col_idx)
        padding = (max_col_len - len(col_title)) * " "
        return padding + col_title

    def _col_idx_to_str(self, col_idx: int):
        if col_idx > 25:
            raise NotImplementedError("Column index can be 0-25 for now!")
        return ascii_uppercase[col_idx]

    def _col_str_to_idx(self, col_str: str):
        if len(col_str) > 1:
            raise NotImplementedError("Column index can be 0-25 for now!")
        return ascii_uppercase.index(col_str)

    def _get_coordinates_from_(self, address: str):
        index = 0
        for i, letter in enumerate(address):
            if letter not in ascii_uppercase:
                index = i
                break
        return self._col_str_to_idx(address[:index]), int(address[index:])

    def _add_new_cell(self, col_idx: int, row_idx: int, formula: str):
        self.grid[col_idx][row_idx] = Cell(formula)

    def change_(self, address: str, formula: str):
        col_idx, row_idx = self._get_coordinates_from_(address)
        cell_to_change = self.grid[col_idx][row_idx]
        if cell_to_change:
            cell_to_change.formula = formula
        else:
            self._add_new_cell(col_idx, row_idx, formula)
