def add_decision_variables():
    number_of_decision_variables = int(
        input("Number of decision variables for objetive function: ")
    )
    decision_variables = [int(input(f"x{i + 1}=")) for i in
                          range(number_of_decision_variables)]

    return decision_variables


def show_objective_function(objective_function):
    # Create a modified list for the representation of decision variables in the
    # objetive function
    modified_decision_variables = [
        f"+{coef}x{i + 1}" if i > 0 and coef > 0 else f"{coef}x{i + 1}" for
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
                constraint_variables.append(int(input("rhs=")))
            else:
                constraint_variables.append(int(input(f"x{i + 1}=")))

        restrictions.append(constraint_variables)
        print()

    return restrictions


def show_restrictions(restrictions):
    print("Subject to:")

    # Create a modified list for the representation of decision variables in the
    # objetive function
    for restriction in restrictions:
        modified_coefficients = [
            f"+{coef}x{i + 1}" if i > 0 and int(coef) > 0 else f"{coef}x{i + 1}"
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


def main():
    objective_function = add_decision_variables()
    restrictions = add_constraint_variables()

    show_objective_function(objective_function)
    show_restrictions(restrictions)

    print()
    objective_function_equation = convert_objective_function_to_equation(
        objective_function
    )
    print(objective_function_equation)

    constraint_equations = convert_constraints_to_equations(restrictions)
    print(constraint_equations)


if __name__ == "__main__":
    main()
