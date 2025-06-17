import streamlit as st
from sympy import symbols, Eq, solve, simplify, diff, integrate, expand, factor
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

x, y, z = symbols('x y z')
transformations = (standard_transformations + (implicit_multiplication_application,))

st.title("Algebra & Calculus Calculator")

operation = st.selectbox("Choose an operation", [
    "Simplify expression",
    "Solve equation (set to 0)",
    "Derivative",
    "Integral",
    "Expand expression",
    "Factor expression",
    "Evaluate with values"
])

expression = st.text_input("Enter the expression (e.g., 2*x^2 - y^2, use variables x,y,z):")

# Show input box for variable values ONLY if "Evaluate with values" is selected
values_str = ""
if operation == "Evaluate with values":
    # Use session state to remember input even if hidden/re-shown
    if "values_str" not in st.session_state:
        st.session_state.values_str = ""
    values_str = st.text_input("Enter values separated by commas (e.g., x=2, y=3)", value=st.session_state.values_str)
    st.session_state.values_str = values_str  # save back to session state

if st.button("Calculate"):
    try:
        expr = parse_expr(expression.replace("^", "**"), transformations=transformations)

        if operation == "Simplify expression":
            result = simplify(expr)

        elif operation == "Solve equation (set to 0)":
            eq = Eq(expr, 0)
            result = solve(eq, x)

        elif operation == "Derivative":
            result = diff(expr, x)

        elif operation == "Integral":
            result = integrate(expr, x)

        elif operation == "Expand expression":
            result = expand(expr)

        elif operation == "Factor expression":
            result = factor(expr)

        elif operation == "Evaluate with values":
            if values_str:
                substitutions = {}
                for pair in values_str.split(","):
                    var, val = pair.split("=")
                    substitutions[var.strip()] = float(val.strip())
                result = expr.evalf(subs=substitutions)
            else:
                st.warning("Please enter variable values to evaluate.")
                result = None

        if result is not None:
            st.write("**Result:**")
            st.write(result)

    except Exception as e:
        st.error(f"Error: {e}")
