from string import digits


def parse_formula(formula: str):
    if formula == "":
        return 0
    divided = _divide_into_elements("sum", formula)
    a = divided[0]
    b = divided[1]
    x = _parse_multiplicative(a)
    if x == "Error":
        return x
    a = float(x)
    y = parse_formula(b)
    if y == "Error":
        return y
    b = float(y)
    return a + b


def _parse_multiplicative(formula):
    if formula == "":
        return 1
    divided = _divide_into_elements("multiplication", formula)
    a = divided[0]
    b = divided[1]
    if a[0] == "/":
        x = _parse_term(a[1 : len(a)])
        try:
            a = 1 / x
        except ZeroDivisionError:
            return "Error"
    else:
        a = _parse_term(a)
    if a == "Error":
        return a

    y = _parse_multiplicative(b)
    if y == "Error":
        return y

    b = float(y) if b != "" else 1
    return a * b


def _parse_term(formula):
    first_char = formula[0]
    if formula == "-1":
        return -1
    if first_char == "(":
        if formula[-1] == ")":
            return parse_formula(formula[1 : len(formula) - 1])
        return parse_formula(formula)
    elif first_char in digits:
        return float(formula)
    return "Error"


def _divide_into_elements(operation, formula):
    if operation == "sum":
        special_chars = ["-", "+"]
    else:
        special_chars = ["/", "*"]
    divided = [formula, ""]
    num_of_l_bracket = 0
    num_of_r_bracket = 0
    for i, char in enumerate(formula):
        if char == "(":
            num_of_l_bracket += 1
        elif char == ")":
            num_of_r_bracket += 1
        elif char == "-" and i == 0:
            if operation != "sum":
                divided[0] = "-1"
                divided[1] = formula[1:]
                break
        elif char == special_chars[0] and i == 0 and operation != "sum":
            break
        elif char in special_chars and num_of_r_bracket == num_of_l_bracket:
            divided[0] = formula[:i]
            divided[1] = formula[i + 1 :] if char == special_chars[1] else formula[i:]
            break
    return divided
