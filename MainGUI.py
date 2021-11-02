from tkinter import *
import random
import time

score = 0
direction = 'down'

players = ["x", "o"]
player_symbol = random.choice(players)
class Ball:
    def __init__ (self,canvas,x,y,diameter,xVelo,yVelo,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=color)
        self.xVelo = xVelo
        self.yVelo = yVelo
    def move(self):
        coordinates = self.canvas.coords(self.image)
        if (coordinates[2] >= self.canvas.winfo_width() or coordinates[0] < 0):
            self.xVelo = -self.xVelo
        if (coordinates[3] >= self.canvas.winfo_height() or coordinates[1] < 0):
            self.yVelo = -self.yVelo
        self.canvas.move(self.image,self.xVelo,self.yVelo)
## create Balls class for openScreen
def openSnake(event):
    GAME_WIDTH = 1200
    GAME_HEIGTH = 600
    SPEED = 100
    SPACE_SIZE = 50
    BODY_PARTS = 3
    SNAKE_COLOR = "#00FF00"
    FOOD_COLOR = "#FF0000"
    BACKGROUND_COLOR = "#000000"

    class Snake:
        def __init__(self):
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []

            for i in range(0, BODY_PARTS):
                self.coordinates.append([0, 0])

            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
                self.squares.append(square)

    class Food(Snake):
        def __init__(self):
            x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGTH / SPACE_SIZE) - 1) * SPACE_SIZE
            self.coordinates = [x, y]
            for body_part in snake.coordinates[1:]:
                if x == body_part[0] and y == body_part[1]:
                    return self.__init__()

            canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

    def next_turn(snake, food):
        x, y = snake.coordinates[0]
        if direction == "up":
            y -= SPACE_SIZE
        elif direction == "down":
            y += SPACE_SIZE
        elif direction == "left":
            x -= SPACE_SIZE
        elif direction == "right":
            x += SPACE_SIZE

        snake.coordinates.insert(0, (x, y))

        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            global score
            score += 1
            label.config(text="Score:{}".format(score))
            canvas.delete("food")
            food = Food()
        else:

            del snake.coordinates[-1]

            canvas.delete(snake.squares[-1])

            del snake.squares[-1]
        if check_collision(snake):
            game_over()
        else:
            window2.after(SPEED, next_turn, snake, food)

    def change_direction(new_direction):
        global direction

        if new_direction == 'left':
            if direction != 'right':
                direction = new_direction
        elif new_direction == 'right':
            if direction != 'left':
                direction = new_direction
        elif new_direction == 'up':
            if direction != 'down':
                direction = new_direction
        if new_direction == 'down':
            if direction != 'up':
                direction = new_direction

    def check_collision(snake):
        x, y = snake.coordinates[0]
        if x < 0 or x >= GAME_WIDTH:
            return True
        elif y < 0 or y >= GAME_HEIGTH:
            return True

        for body_part in snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False

    def game_over():
        global score
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('consolas', 70), text="GAME OVER",
                           fill="red")
        canvas.create_text(canvas.winfo_width() / 2, (canvas.winfo_height() / 2) + 100, font=('consolas', 25), text="Your final score is {}".format(score),
                           fill="red")
        score = 0

    window2 = Tk()
    window2.title("Snake game")
    window2.resizable(False, False)

    label = Label(window2, text="Score:{}".format(score), font=('consolas', 40))
    label.pack()

    canvas = Canvas(window2, bg=BACKGROUND_COLOR, height=GAME_HEIGTH, width=GAME_WIDTH)
    canvas.pack()

    window2.update()

    window_width = window2.winfo_width()
    window_height = window2.winfo_height()
    screen_width = window2.winfo_screenwidth()
    screen_height = window2.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window2.geometry(f"{window_width}x{window_height}+{x}+{y-50}")
    window2.bind('<Left>', lambda event: change_direction('left'))
    window2.bind('<Right>', lambda event: change_direction('right'))
    window2.bind('<Up>', lambda event: change_direction('up'))
    window2.bind('<Down>', lambda event: change_direction('down'))

    snake = Snake()
    food = Food()

    next_turn(snake, food)
    window2.mainloop()

def openScreen(event):
    HEIGHT = 1080
    WIDTH = 1920
    window = Tk()

    canvas = Canvas(window, height=HEIGHT, width=WIDTH)
    canvas.pack()
    canvas.config(bg="#1ADEAA")
    basket_ball = Ball(canvas, 0, 0, 50, 2, 3, "orange")
    soccer_ball = Ball(canvas, 399, 399, 499, 5, 7, "black")
    tennis_ball = Ball(canvas, 0, 0, 20, 4, 8, "green")
    first_ball = Ball(canvas, 0, 0, 20, 1, 2, "yellow")
    second_ball = Ball(canvas, 0, 0, 25, 4, 3, "blue")
    third_ball = Ball(canvas, 0, 0, 120, 5, 6, "red")
    fourth_ball = Ball(canvas, 0, 0, 60, 8, 7, "pink")
    fifth_ball = Ball(canvas, 0, 0, 75, 9, 10, "purple")
    sixth_ball = Ball(canvas, 0, 0, 40, 12, 11, "gray")

    while True:
        tennis_ball.move()
        basket_ball.move()
        soccer_ball.move()
        first_ball.move()
        second_ball.move()
        third_ball.move()
        fourth_ball.move()
        fifth_ball.move()
        sixth_ball.move()
        window.update()
        time.sleep(0.01)

    window.mainloop()

def openTictactoe(event):

    def next_turn(row, column):
        global player_symbol
        if buttons[row][column]['text'] == "" and check_winner() is False:
            if player_symbol == players[0]:
                buttons[row][column]['text'] = player_symbol
                if check_winner() is False:
                    player_symbol = players[1]
                    label.config(text=(players[1] + " turn"))
                elif check_winner() is True:
                    label.config(text=(players[0] + " wins"))
                elif check_winner() == "Tie":
                    label.config(text="Tie!")
            else:
                buttons[row][column]['text'] = player_symbol
                if check_winner() is False:
                    player_symbol = players[0]
                    label.config(text=(players[0] + " turn"))
                elif check_winner() is True:
                    label.config(text=(players[1] + " wins"))
                elif check_winner() == "Tie":
                    label.config(text="Tie!")

    def check_winner():
        for row in range(3):
            if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
                buttons[row][0].config(bg="green")
                buttons[row][1].config(bg="green")
                buttons[row][2].config(bg="green")
                return True
        for column in range(3):
            if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
                buttons[0][column].config(bg="green")
                buttons[1][column].config(bg="green")
                buttons[2][column].config(bg="green")
                return True
        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            buttons[0][0].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][2].config(bg="green")
            return True
        elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            buttons[0][2].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][0].config(bg="green")
            return True
        elif empty_spaces() is False:
            for row in range(3):
                for column in range(3):
                    buttons[row][column].config(bg="yellow")
            return "Tie"
        else:
            return False

    def empty_spaces():
        spaces = 9
        for row in range(3):
            for column in range(3):
                if buttons[row][column]['text'] != "":
                    spaces -= 1
        if spaces == 0:
            return False
        else:
            return True

    def new_game():
        global player_symbol
        player_symbol = random.choice(players)
        label.config(text=player_symbol + " turn")
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(text="", bg="white")

    window = Tk()
    players = ["x", "o"]
    player_symbol = random.choice(players)
    buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    label = Label(window, text=player_symbol + " turn", font=('consolas', 40))
    label.pack(side="top")

    reset_button = Button(window, text="reset", font=('consolas', 20), command=new_game)
    reset_button.pack(side="top")
    frame = Frame(window)
    frame.pack()
    for x in range(3):
        for y in range(3):
            buttons[x][y] = Button(frame, text="", width=5, height=2,
                                   command=lambda row=x, column=y: next_turn(row, column))
            buttons[x][y].grid(row=x, column=y)

    window.mainloop()


window = Tk()
window.title("WINDOWS VIP PRO")
backgroundImage = PhotoImage(file = "C:\\Users\\User\\Downloads\\bg2.png")
screenImage = PhotoImage(file = "C:\\Users\\User\\Downloads\\Screen.png")
snakeImage = PhotoImage(file = "C:\\Users\\User\\Downloads\\Snake.png")
tictactoeImage = PhotoImage(file = "C:\\Users\\User\\Downloads\\Tictactoe.png")
canvas = Canvas(window, width = 1920, height = 1080)
canvas.pack()
canvas.create_image(0,0,image = backgroundImage,anchor=NW)
snakeLabel = Label(canvas, image = snakeImage, text = "Snake game", compound = "top")
snakeLabel.place(x=1000,y=0)
screenLabel = Label(canvas, image = screenImage, text = "Off-screen", compound = "top")
screenLabel.place(x=1100,y=0)
tictactoeLabel = Label(canvas, image = tictactoeImage, text = "Tictactoe", compound = "top")
tictactoeLabel.place(x=1000,y=100)
snakeLabel.bind('<Double-Button-1>',openSnake)
screenLabel.bind('<Double-Button-1>',openScreen)
tictactoeLabel.bind('<Double-Button-1>',openTictactoe)






window.mainloop()
