def add_decision_variables():
    number_of_decision_variables = int(
        input("Number of decision variables for objetive function: "))
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
    print("\nObjective function:")
    print("Z=" + "".join(modified_decision_variables))


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
            -2] + f"{restriction[-1]}")


def main():
    objective_function = add_decision_variables()
    show_objective_function(objective_function)

    restrictions = add_constraint_variables()
    show_restrictions(restrictions)


if __name__ == "__main__":
    main()
