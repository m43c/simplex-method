def add_decision_variables():
    number_of_decision_variables = int(
        input("Number of decision variables for objetive function: ")
    )
    decision_variables = [int(input(f"X{i + 1}=")) for i in
                          range(number_of_decision_variables)]

    return decision_variables


def show_objective_function(objective_function):
    # Create a modified list for the representation of decision variables in the
    # objetive function
    modified_decision_variables = [
        f"+{coef}X{i + 1}" if i > 0 and coef > 0 else f"{coef}X{i + 1}" for
        i, coef in enumerate(objective_function)]

    # Print the objective function
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
                constraint_variables.append(int(input("RHS=")))
            else:
                constraint_variables.append(int(input(f"X{i + 1}=")))

        restrictions.append(constraint_variables)
        print()

    return restrictions


def show_restrictions(restrictions):
    print("Subject to:")

    # Create a modified list for the representation of decision variables in the
    # objetive function
    for restriction in restrictions:
        modified_coefficients = [
            f"+{coef}X{i + 1}" if i > 0 and int(coef) > 0 else f"{coef}X{i + 1}"
            for i, coef in enumerate(restriction[:-2])]

        # Print each constraint
        print("".join(modified_coefficients) + restriction[
            -2] + f"{restriction[-1]}"
              )


def convert_objective_function_to_equation(objective_function):
    equation = [1] + [coef * -1 for coef in objective_function] + [0 for _ in
                                                                   range(3)] + [
                   0]
    return equation


def convert_constraints_to_equations(restrictions):
    equations = []

    for i, restriction in enumerate(restrictions):
        z = 0
        coefficients = list(filter(lambda element: not isinstance(element, str),
                                   restriction[:-1]
                                   )
                            )
        slack_variables = [1 if j == i else 0 for j in range(len(restrictions))]
        rhs = restriction[-1]

        new_restriction = [z] + coefficients + slack_variables + [rhs]
        equations.append(new_restriction)

    return equations


def show_tableau_simplex(tableau_simplex):
    print("BV\t\tZ\t\tX1\t\tX2\t\tS1\t\tS2\t\tS3\t\tRHS")
    print("------------------------------------------------------------")

    for i, restriction in enumerate(tableau_simplex):
        for j, value in enumerate(restriction):
            if i < len(tableau_simplex) - 1 and j == 0:
                print(f"S{i + 1}\t\t{value}\t\t", end="")
            elif i == len(tableau_simplex) - 1 and j == 0:
                print(f"Z\t\t{value}\t\t", end="")
            else:
                print(f"{value}\t\t", end="")
        print()


def is_optimal_solution(row_z):
    return any(coef < 0 for coef in row_z)


def find_pivot_column(tableau_simplex):
    row_z = tableau_simplex[-1]
    min_value = min(row_z)
    column_index = row_z.index(min_value)

    return [column[column_index] for column in tableau_simplex]


def find_pivot_row(tableau_simplex, pivot_column):
    rhs_column_index = len(tableau_simplex) - 1
    rhs_column = [column[rhs_column_index] for column in tableau_simplex]
    positives_results = []

    for pivot_col_coef, rhs_col_coef in zip(pivot_column[:-1], rhs_column[:-1]):
        positive_result = pivot_col_coef / rhs_col_coef

        if positive_result > 0:
            positives_results.append(positive_result)

    row_index = rhs_column.index(min(positives_results))

    return [value for value in tableau_simplex[row_index]]


def calculate_optimal_solution(tableau_simplex):
    while is_optimal_solution(tableau_simplex[-1]):
        pivot_column = min(tableau_simplex)  # Input variable

        pivot_row = find_pivot_row(tableau_simplex, pivot_column
                                   )  # Output variable


def main():
    objective_function = add_decision_variables()
    restrictions = add_constraint_variables()

    show_objective_function(objective_function)
    show_restrictions(restrictions)

    print()
    objective_function_equation = convert_objective_function_to_equation(
        objective_function
    )
    constraint_equations = convert_constraints_to_equations(restrictions)

    tableau_simplex = constraint_equations + [objective_function_equation]

    print("Tableau Simplex")
    show_tableau_simplex(tableau_simplex)


if __name__ == "__main__":
    main()
