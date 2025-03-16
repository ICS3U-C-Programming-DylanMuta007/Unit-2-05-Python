#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date :23-02-2025
# This program calculates the perimeter & area of a rectangle

# global variable
variable_x = 5


def local_variable() -> None:
    variable_x = 1
    variable_y = 3

    variable_x = variable_x + 29
    variable_z = variable_x + variable_y

    print(f"Local variable:  {variable_x} + {variable_y} = {variable_z}")


def global_variable() -> None:
    global variable_x
    variable_y = 3

    variable_x = variable_x + 360
    variable_z = variable_x + variable_y

    print(f"Global variable: {variable_x} + {variable_y} = {variable_z}")


def main() -> None:
    local_variable()
    global_variable()

    print("\nDone.")


if __name__ == "__main__":
    main()