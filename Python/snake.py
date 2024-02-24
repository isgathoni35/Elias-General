import random

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.blocks = [(5, 5)]
        self.direction = (0, 1)

    def move(self):
        head_x, head_y = self.blocks[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.blocks.insert(0, new_head)
        if new_head in blocks and new_head not in self.blocks:
            blocks.remove(new_head)
        else:
            self.blocks.pop(0)

    def change_direction(self, new_direction):
        if not (new_direction[0] == -self.direction[0] or new_direction[1] == -self.direction[1]):
            self.direction = new_direction

def generate_block():
    return Block(*random.sample(range(10), 2))

snake = Snake()
blocks = [generate_block() for _ in range(10)]

while blocks:
    snake.move()
    input("Press enter to change direction. Enter a new direction (x y): ")
    new_direction = tuple(map(int, input().split()))
    snake.change_direction(new_direction)
    
    