from tabulate import tabulate
from fractions import Fraction


def add_decision_variables():
    number_of_decision_variables = int(
        input("Number of decision variables for objetive function: ")
    )
    decision_variables = [float(input(f"X{i + 1}=")) for i in
                          range(number_of_decision_variables)]

    return number_of_decision_variables, decision_variables


def show_objective_function(objective_function):
    modified_decision_variables = [
        f"+{Fraction(coef).limit_denominator()}X{i + 1}" if i > 0 and coef > 0 else f"{Fraction(coef).limit_denominator()}X{i + 1}"
        for
        i, coef in enumerate(objective_function)]

    print("Objective function:")
    print("Z=" + "".join(modified_decision_variables) + "\n")


def add_constraint_variables():
    restrictions = []
    number_of_restrictions = int(input("\nNumber of restrictions: "))

    for _ in range(number_of_restrictions):
        constraint_variables = []
        number_of_decision_variables = int(
            input("Number of decision variables: ")
        )

        for i in range(number_of_decision_variables + 2):
            if i == number_of_decision_variables:
                constraint_variables.append(input("Comparator="))
            elif i == number_of_decision_variables + 1:
                constraint_variables.append(float(input("RHS=")))
            else:
                constraint_variables.append(float(input(f"X{i + 1}=")))

        restrictions.append(constraint_variables)
        print()

    return restrictions


def show_restrictions(restrictions):
    print("Subject to:")

    for restriction in restrictions:
        modified_coefficients = [
            f"+{Fraction(coef).limit_denominator()}X{i + 1}" if i > 0 and coef > 0 else f"{Fraction(coef).limit_denominator()}X{i + 1}"
            for i, coef in enumerate(restriction[:-2])]

        print("".join(modified_coefficients) + restriction[
            -2] + f"{Fraction(restriction[-1]).limit_denominator()}"
              )


def convert_objective_function_to_equation(objective_function):
    equation = ([1.0] + [coef * -1 for coef in objective_function] +
                [0.0 for _ in range(3)] + [0.0])
    return equation


def convert_constraints_to_equations(restrictions):
    equations = []

    for i, restriction in enumerate(restrictions):
        z = 0.0
        coefficients = list(filter(lambda element: not isinstance(element, str),
                                   restriction[:-1]
                                   )
                            )
        slack_variables = [1.0 if j == i else 0.0 for j in
                           range(len(restrictions))]
        rhs = restriction[-1]

        new_restriction = [z] + coefficients + slack_variables + [rhs]
        equations.append(new_restriction)

    return equations


def show_tableau_simplex(tableau, number_dec_var, pvt_col_idx):
    decision_variables = [f"X{coef + 1}" for coef in range(number_dec_var)]
    slack_variables = [f"S{var + 1}" for var in range(len(tableau) - 1)]
    header = ["BV", "Z"] + decision_variables + slack_variables + ["RHS"]
    modified_tableau = []

    for idx, row in enumerate(tableau):
        if idx < len(tableau) - 1:
            modified_row = [f"S{idx + 1}"] + [Fraction(i).limit_denominator()
                                              for i in row.copy()]
        else:
            modified_row = ["Z"] + [Fraction(i).limit_denominator() for i in
                                    row.copy()]

        modified_tableau.append(modified_row)

    modified_tableau_representation = tabulate(modified_tableau, headers=header,
                                               tablefmt="pretty"
                                               )
    print(modified_tableau_representation)


def is_optimal_solution(row_z):
    return any(coef < 0 for coef in row_z)


def find_pivot_column(tableau_simplex):
    row_z = tableau_simplex[-1]
    min_value = min(row_z)
    column_index = row_z.index(min_value)
    column = [row[column_index] for row in tableau_simplex]

    return column_index, column


def find_pivot_row(tableau_simplex, pivot_column):
    rhs_column = [row[-1] for row in tableau_simplex]
    results = []
    index = 0

    for rhs_col_coef, pivot_col_coef in zip(rhs_column, pivot_column):
        result = rhs_col_coef / pivot_col_coef
        results.append((result, index))

        index += 1

    positive_results = list(filter(lambda value: value[0] > 0, results))
    min_result = min(positive_results, key=lambda value: value[0])

    row_index = min_result[1]
    row = [value for value in tableau_simplex[row_index]]

    return row_index, row


def calculate_optimal_solution(tableau_simplex, number_of_decision_variables):
    tableau_number = 2

    while is_optimal_solution(tableau_simplex[-1]):
        pivot_column_index, pivot_column = find_pivot_column(tableau_simplex
                                                             )  # Input variable
        pivot_row_index, pivot_row = find_pivot_row(tableau_simplex,
                                                    pivot_column
                                                    )  # Output variable
        pivot_element = tableau_simplex[pivot_row_index][pivot_column_index]

        new_tableau_simplex = []
        incoming_row = [value / pivot_element for value in
                        tableau_simplex[pivot_row_index]]
        old_row_pivot_coef = [row[pivot_column_index] for row in
                              tableau_simplex]

        print(f"Tableau Simplex #1")
        show_tableau_simplex(tableau_simplex, number_of_decision_variables,
                             pivot_column_index
                             )

        for i, row in enumerate(tableau_simplex):
            new_row = []

            if i != pivot_row_index:
                old_row = [value for value in tableau_simplex[i]]

                for old_val, incoming_val in zip(old_row, incoming_row):
                    result = old_val - old_row_pivot_coef[i] * incoming_val
                    new_row.append(result)
            else:
                new_row = incoming_row

            new_tableau_simplex.append(new_row)

        tableau_simplex = new_tableau_simplex

        print(f"\nTableau Simplex #{tableau_number}")
        show_tableau_simplex(tableau_simplex, number_of_decision_variables,
                             pivot_column_index
                             )

        tableau_number += 1


def main():
    number_of_decision_variables, objective_function = add_decision_variables()
    restrictions = add_constraint_variables()

    show_objective_function(objective_function)
    show_restrictions(restrictions)

    print()
    objective_function_equation = convert_objective_function_to_equation(
        objective_function
    )
    constraint_equations = convert_constraints_to_equations(restrictions)

    tableau_simplex = constraint_equations + [objective_function_equation]

    calculate_optimal_solution(tableau_simplex, number_of_decision_variables)


if __name__ == "__main__":
    main()
