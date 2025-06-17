from sympy import symbols, Eq, solve, simplify, diff, integrate, expand, factor
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

# Support multiple variables
x, y, z = symbols('x y z')

# Enable implicit multiplication like 3(2*x + y)
transformations = (standard_transformations + (implicit_multiplication_application,))

while True:
    print("\n=== Python Math Calculator ===")
    print("0. Quit")
    print("1. Simplify expression")
    print("2. Solve equation")
    print("3. Derive expression")
    print("4. Integrate expression")
    print("5. Expand expression")
    print("6. Factor expression")
    print("7. Evaluate with values (e.g., x=2, y=3)")

    choice = input("Enter your choice (0-7): ")

    if choice == '0':
        print("Goodbye!")
        break

    expression = input("Enter the expression (use variables like x, y): ").replace("^", "**")

    try:
        expr = parse_expr(expression, transformations=transformations)

        if choice == '1':
            print("Simplified:", simplify(expr))

        elif choice == '2':
            eq = Eq(expr, 0)
            print("Solutions:", solve(eq, x))

        elif choice == '3':
            print("Derivative:", diff(expr, x))

        elif choice == '4':
            print("Integral:", integrate(expr, x))

        elif choice == '5':
            print("Expanded:", expand(expr))

        elif choice == '6':
            print("Factored:", factor(expr))

        elif choice == '7':
            val_input = input("Enter variable values (e.g., x=2, y=3): ")
            substitutions = {}
            for pair in val_input.split(","):
                var, val = pair.split("=")
                substitutions[var.strip()] = float(val.strip())
            result = expr.evalf(subs=substitutions)
            print("Result:", result)

        else:
            print("Invalid choice.")

    except Exception as e:
        print("Error:", e)
