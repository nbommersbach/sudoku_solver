from canvas import goto


class Sudoku:

    def __init__(self, canvas_size):
        self.canvas_size = canvas_size
        self.puzzle = []
        self.possible_solutions = []
        self.solution_found = []

    def matrix_setup(self, matrix):
        for i in range(9):
            new_row = []

            for j in range(9):
                new_row.append([])

            matrix.append(new_row)

        return matrix

    def print_puzzle(self):
        for i in range(9):
            print(self.puzzle[i])

    def set_value(self, matrix, x, y, value):
        matrix[x][y] = value

    def setup_sudoku(self, data):

        # initialize the matrices
        self.puzzle = self.matrix_setup(self.puzzle)
        self.possible_solutions = self.matrix_setup(self.possible_solutions)
        self. solution_found = self.matrix_setup(self.solution_found)

        digit_count = 0

        for i in range (9):
            for j in range(9):

                if data[digit_count] == '.':
                    self.set_value(self.puzzle, i, j, ' ')
                    self.set_value(self.solution_found, i, j, False)
                else:
                    self.set_value(self.puzzle, i, j, data[digit_count])
                    self.set_value(self.solution_found, i, j, True)

                digit_count += 1

    def write_to_canvas(self, t):
        ix = -self.canvas_size / 2 + self.canvas_size / 17
        iy = self.canvas_size / 2 - self.canvas_size / 17 - int(self.canvas_size / 15) / 2

        y = iy
        for i in range(9):
            x = ix
            for j in range(9):
                goto(t, x, y)

                if self.puzzle[i][j] != ' ':
                    t.write(arg=self.puzzle[i][j], move=False, align='center', font=('Arial', int(self.canvas_size / 15), 'normal'))

                x += self.canvas_size / 9
            y -= self.canvas_size / 9

    def return_row_numbers(self, row_number):
        row = self.puzzle[row_number]
        result_row = []

        for i in range(9):
            if row[i] != ' ':
                result_row.append(row[i])

        return result_row

    def return_column_numbers(self, column_number):
        column = []
        for i in range(9):
            column.append(self.puzzle[i][column_number])

        result_column = []

        for i in range(9):
            if column[i] != ' ':
                result_column.append(column[i])

        return result_column

    def return_block_numbers(self, x, y):
        result_block = []

        # search for block boundaries:
        lower_x_boundary = x
        while lower_x_boundary % 3 != 0:
            lower_x_boundary -= 1

        lower_y_boundary = y
        while lower_y_boundary % 3 != 0:
            lower_y_boundary -= 1

        for i in range(3):
            row = self.puzzle[lower_y_boundary + i]
            for j in range(3):
                if row[lower_x_boundary + j] != ' ':
                    result_block.append(row[lower_x_boundary + j])

        return result_block

    def find_possible_solutions(self, x, y):
        row = self.return_row_numbers(y)
        column = self.return_column_numbers(x)
        block = self.return_block_numbers(x, y)

        forbidden = list(set(row + column + block))

        possible_solutions = []
        for i in range(9):
            possible_solutions.append(i + 1)

        for j in forbidden:
            if int(j) in possible_solutions:
                possible_solutions.remove(int(j))

        return possible_solutions

    def fill_possible_solution(self):
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == ' ':
                    test = self.find_possible_solutions(j, i)
                    self.possible_solutions[i][j] = test
                    print(i, j, test)

    def solved(self):
        for i in range(9):
            for j in range(9):
                if self.solution_found[i][j] == False:
                    return False
        return True

    def solve(self, t):
        while not self.solved():

            self.fill_possible_solution()

            for i in range(9):
                for j in range(9):
                    sols = self.possible_solutions[i][j]
                    if len(sols) == 1:
                        self.puzzle[i][j] = sols[0]
                        self.solution_found[i][j] = True

        self.write_to_canvas(t)


