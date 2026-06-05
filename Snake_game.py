from tkinter import *
import random

# ---------------- CONFIG ---------------- #

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 25

BG_COLOR = "black"
SNAKE_COLOR = "lime"
FOOD_COLOR = "red"

INITIAL_SPEED = 120

# ---------------- SNAKE ---------------- #

class Snake:
    def __init__(self):
        self.body = [[100, 100], [75, 100], [50, 100]]
        self.direction = "Right"

    def move(self):
        x, y = self.body[0]

        if self.direction == "Up":
            y -= CELL_SIZE
        elif self.direction == "Down":
            y += CELL_SIZE
        elif self.direction == "Left":
            x -= CELL_SIZE
        elif self.direction == "Right":
            x += CELL_SIZE

        self.body.insert(0, [x, y])

    def remove_tail(self):
        self.body.pop()


# ---------------- FOOD ---------------- #

class Food:
    def __init__(self, snake_body):
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE

            if [x, y] not in snake_body:
                self.position = [x, y]
                break


# ---------------- GAME ---------------- #

class SnakeGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.resizable(False, False)

        self.score_label = Label(
            root,
            text="Score: 0",
            font=("Consolas", 20)
        )
        self.score_label.pack()

        self.canvas = Canvas(
            root,
            width=WIDTH,
            height=HEIGHT,
            bg=BG_COLOR
        )
        self.canvas.pack()

        self.root.bind("<Up>", self.change_direction)
        self.root.bind("<Down>", self.change_direction)
        self.root.bind("<Left>", self.change_direction)
        self.root.bind("<Right>", self.change_direction)
        self.root.bind("r", self.restart)

        self.start_game()

    def start_game(self):
        self.score = 0
        self.speed = INITIAL_SPEED

        self.snake = Snake()
        self.food = Food(self.snake.body)

        self.update_score()
        self.draw()
        self.game_loop()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def draw(self):
        self.canvas.delete("all")

        # Draw snake
        for x, y in self.snake.body:
            self.canvas.create_rectangle(
                x,
                y,
                x + CELL_SIZE,
                y + CELL_SIZE,
                fill=SNAKE_COLOR,
                outline=""
            )

        # Draw food
        x, y = self.food.position
        self.canvas.create_oval(
            x,
            y,
            x + CELL_SIZE,
            y + CELL_SIZE,
            fill=FOOD_COLOR,
            outline=""
        )

    def change_direction(self, event):
        key = event.keysym

        opposite = {
            "Up": "Down",
            "Down": "Up",
            "Left": "Right",
            "Right": "Left"
        }

        if key != opposite[self.snake.direction]:
            self.snake.direction = key

    def game_loop(self):
        self.snake.move()

        head = self.snake.body[0]

        # Eat food
        if head == self.food.position:
            self.score += 1
            self.update_score()

            if self.speed > 50:
                self.speed -= 2

            self.food = Food(self.snake.body)

        else:
            self.snake.remove_tail()

        if self.check_collision():
            self.game_over()
            return

        self.draw()
        self.root.after(self.speed, self.game_loop)

    def check_collision(self):
        x, y = self.snake.body[0]

        # Wall collision
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return True

        # Self collision
        if self.snake.body[0] in self.snake.body[1:]:
            return True

        return False

    def game_over(self):
        self.canvas.delete("all")

        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2 - 40,
            text="GAME OVER",
            fill="red",
            font=("Consolas", 40, "bold")
        )

        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2 + 10,
            text=f"Score: {self.score}",
            fill="white",
            font=("Consolas", 20)
        )

        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2 + 50,
            text="Press R to Restart",
            fill="yellow",
            font=("Consolas", 16)
        )

    def restart(self, event=None):
        self.start_game()


# ---------------- MAIN ---------------- #

root = Tk()

game = SnakeGame(root)

root.mainloop()