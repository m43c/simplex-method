# Simplex Method

## Introduction

The Simplex Method Solver is a Python-based tool that implements the simplex
algorithm for solving linear programming problems. The simplex algorithm is an
optimization technique used to find the optimal solution to a linear programming
problem. This project provides a user-friendly interface for inputting linear
programming problems and displays the step-by-step solution using the simplex
method.

## Features

- Allows users to input the objective function and constraints of a linear
  programming problem.
- Displays the objective function, constraints, and simplex tableau.
- Guides users through each step of the simplex algorithm.
- Provides the optimal solution to the linear programming problem.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/m43c/simplex-method.git
```

2. Navigate to the project directory:

```bash
cd simplex-method
```

## Usage

1. Run the `main.py` file:

```bash
python main.py
```

2. Follow the on-screen instructions to input the objective function and
   constraints of your linear programming problem.

3. The solver will guide you through each step of the simplex algorithm and
   display the optimal solution.

## Example

Consider the following linear programming problem:

**Objective Function:**

```
Maximize Z = 10x1 + 20x2
```

**Subject to:**

```
4x1 + 2x2 <= 20
8x1 + 8x2 <= 20
      2x2 <= 10 
```

After running the Simplex Method, the optimal solution would be:

```
Optimal Solution:
x1 = 0
x2 = 5/2
Z = 50
```

## Screenshot

![Screenshot](https://github.com/m43c/simplex-method/blob/main/screenshot.png?raw=true)

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements,
feel free to open an issue or create a pull request.

