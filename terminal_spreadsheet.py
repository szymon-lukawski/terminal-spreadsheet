import argparse
import sys, os
from spreadsheet import Spreadsheet


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--NAME",
        type=str,
        default="example",
        help="Name of the spreadsheet document. Used for saving.",
    )
    parser.add_argument(
        "--dims",
        type=int,
        nargs=2,
        default=[10,5],
        help="number of columns and number of rows of the spreadsheet.",
    )
    parsed_args = parser.parse_args(args[1:])
    name = parsed_args.NAME
    sheet = Spreadsheet(name, parsed_args.dims)
    while True:
        os.system("clear")
        print(sheet)
        print("ADDRESS(column,row)=FORMULA")
        user_input = input("e.g.: B3=13+2 : ")
        address, *formula = user_input.split("=")
        formula = "=".join(formula)
        sheet.change_(address, formula)
        sheet.refresh()

if __name__ == "__main__":
    main(sys.argv)
