# SudokuGraphia

**Authors:** [tituss3](https://github.com/titusse3), 
  [lurgrid](https://github.com/Lurgrid)

**License:** GPLv3

**Language:** Python

### Sudoku Application Interface

![Sudoku Application](gif/presentation.gif)

## Project Description

SudokuGraphia is a project developed as part of a computer science license program. The project encompasses functionalities related to graph theory and Sudoku puzzles. It provides a REPL (Read-Eval-Print Loop) for generating and manipulating graphs and a graphical application built with PyQt 6 for playing and generating Sudoku puzzles. The generated Sudoku puzzles can be solved using three different algorithms: Greedy, Powell, and Backtracking.

## Features

### Graph REPL

- Interactive environment for generating and applying various operations on graphs.
- Supports a range of graph algorithms and visualizations.

### Sudoku Application

- **Play Sudoku:** A user-friendly interface to play Sudoku puzzles.
- **Generate Sudoku:** Generate Sudoku puzzles with varying difficulty levels.
- **Solve Sudoku:** Attempt to solve generated Sudoku puzzles using three algorithms:
  - **Greedy Algorithm**
  - **Powell Algorithm**
  - **Backtracking Algorithm**

## Installation

To run SudokuGraphia, ensure you have Python installed on your system. Then, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/tituss3/sudokuGraphia.git
    cd sudokuGraphia
    ```

2. Install the dependencies:

    ```bash
    ./install.sh
    ```

## Usage

### Running the Graph REPL

To start the REPL for graph operations:

```bash
cd repl_dynamique
python repl_dynamique.py
```

Follow the on-screen instructions to interact with the graph functionalities.

### Running the Sudoku Application

```bash
cd sudokuGraphia/exec
./sudokuGraphia
```

Use the interface to play, generate, and solve Sudoku puzzles. Choose the 
desired algorithm to solve generated puzzles.

## License

This project is licensed under the GPLv3 License. See the 
[LICENSE](LICENSE) file for more details.