from parsing import (
    parse_formula,
    _parse_multiplicative,
    _parse_term,
    _divide_into_elements,
)


def test_divide_sum_elements_one_operand():
    assert _divide_into_elements("sum", "1") == ["1", ""]


def test_divide_sum_elements_two_operands():
    assert _divide_into_elements("sum", "1+2") == ["1", "2"]


def test_divide_sum_elements_two_operands_but_it_is_multiplication():
    assert _divide_into_elements("sum", "1*2") == ["1*2", ""]


def test_divide_sum_elements_sum_of_multiplications():
    assert _divide_into_elements("sum", "1*2+3*5") == ["1*2", "3*5"]


def test_divide_mutli_elements_one_operand():
    assert _divide_into_elements("multi", "1") == ["1", ""]


def test_divide_mutli_elements_two_operands():
    assert _divide_into_elements("multi", "1*2") == ["1", "2"]


def test_parse_multiplicative_empty():
    assert _parse_multiplicative("") == 1


def test_parse_multiplicative_one_operand():
    assert _parse_multiplicative("2") == 2


def test_parse_multiplicative_two_operands():
    assert _parse_multiplicative("2*3") == 6


def test_parse_multiplicative_three_operands():
    assert _parse_multiplicative("2*3*4") == 24


def test_parse_multiplicative_four_operands():
    assert _parse_multiplicative("2*3*4*5") == 120


def test_parse_formula_empty():
    assert parse_formula("") == 0


def test_parse_formula_one_operand():
    assert parse_formula("5") == 5


def test_parse_formula_two_operands():
    assert parse_formula("5+4") == 9


def test_parse_formula_three_operands():
    assert parse_formula("5+4+3") == 12


def test_parse_formula_sum_of_multiplications():
    assert parse_formula("5*2+3*4") == 22


def test_parse_formula_multiplication_of_sums():
    assert parse_formula("(2+3)*(4+5)") == (2+3)*(4+5)


def test_parse_formula_subtraction():
    assert parse_formula("1-2") == -1

def test_parse_formula_division():
    assert parse_formula("1/2") == 1/2

def test_parse_formula_division_by_zero():
    assert parse_formula("1/0") == 'Error'

def test_parse_formula_division_by_not_literal_zero():
    assert parse_formula("1/(1-1)") == 'Error'




