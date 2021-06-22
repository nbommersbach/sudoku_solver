import turtle
from canvas import grid
from Sudoku import Sudoku
from Reader import Reader

s = turtle.getscreen()
s.bgcolor('white')
t = turtle.Turtle()

canvas_size = 600

reader = Reader("sudokus/puzzles")
reader.read_sudoku()

sudo = Sudoku(canvas_size)
sudo.setup_sudoku(reader.select_sudoku(244))
t.speed(20000)
grid(t, canvas_size)

sudo.print_puzzle()
sudo.write_to_canvas(t)

s = input("go?: ")

if s == 'go':
    sudo.solve(t)

turtle.Screen().exitonclick()
