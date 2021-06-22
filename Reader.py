class Reader:
    def __init__(self, path):
        self.path = path
        self.data = None

    def read_sudoku(self):
        with open(self.path, 'r') as file:
            self.data = file.readlines()

    def select_sudoku(self, number):
        return self.data[number]