import turtle
import math
import random
import pygame

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Game")
wn.setup(700, 700)
wn.tracer(0)



`
turtle.register_shape("tile_t.gif")
turtle.register_shape("tile_b.gif")
turtle.register_shape("tile_l.gif")
turtle.register_shape("tile_r.gif")
turtle.register_shape("tile_1.gif")
turtle.register_shape("tile_2.gif")
turtle.register_shape("tile_3.gif")
turtle.register_shape("tile_4.gif")
turtle.register_shape("tile_x.gif")
turtle.register_shape("tile_j.gif")
turtle.register_shape("tile_k.gif")
turtle.register_shape("tile_=.gif")


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.pensize(24)
        self.penup()
        self.speed(0)


# speed doesnt mean object speed, it means animation ki speed

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("pink")
        self.penup()
        self.speed(0)

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 32
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 32
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 32
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 32
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)


    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.xcor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance <8 :
            return True
        else:
            return False


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

class enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up","down", "left", "right"])

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

    def move(self):
        if self.direction == "up":
            dx=0
            dy=32
        elif self.direction == "down":
            dx=0
            dy=-32
        elif self.direction == "left":
            dx=-32
            dy=0
        elif self.direction == "right":
            dx=32
            dy=0
        else:
            dx = 0
            dy = 0

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.xcor() > self.xcor():
                self.direction = "up"

        move_to_x = self.xcor()+ dx
        move_to_y = self.ycor() + dy

        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        else :
            self.direction = random.choice(["up","down", "left", "right"])

        turtle.ontimer(self.move, t=random.randint(100,300))

    def is_close(self, other):
        a =self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a**2)+(b**2))

        if distance <100:
            return True
        else:
            return False


levels = [""]
# P is for player= matlab player waha start karega in maze layout(pink)
# G to represent treasure (white)
# T TOP EXPOSED
# B BOTTOM EXPOSED
# R RIGHT EXPOSED
# L LEFT EXPOSED
# 1 LEFT BOTTOM CORNER
# 2 RIGHT BOTTOM CORNER
# 3 TOP RIGHT CORNER
# 4 TOP LEFT CORNER
# J REVERSE U
# K 90 DEGREE LEFT RIGHT FROM BOTTOM U '=]'
# X NOT EXPOSED
# = EXPOSED FROM TOP AND BOTTOM
level_1 = [
    "XBBBXXXXXXXXXXXXXXXX",
    "R P  LXXXXXBBBXXXBXX",
    "XR   1BBXXR    12 EL",
    "XR       LR        L",
    "XX==T3   LXT3   J  L",
    "XR  12   1BB2   LTXX",
    "XR            E LBBX",
    "XXXBBBTT3    4TTR  L",
    "XXR   LXR    LXXR  L",
    "XXR   1B2    LXXR  L",
    "XXR          1BB2  L",
    "XXXT====K          L",
    "XXXR           4TTXX",
    "XXXR    4TTT==XXXBXX",
    "XXB2    1BB2   LR GL",
    "XRE            12  L",
    "XXTTTT=====K       L",
    "XXBBB2           4TX",
    "XR       43   E4TXXX",
    "XXTTTTTTXXXTTTXXXXXX"


    # "XXXXXXXXXXXXXXXXXXXX",
    # "X P  XXXXXXXXXXXXXXX",
    # "XX   XXXXXX    XX  X",
    # "XX       XX        X",
    # "XXXXXX   XXXX   X  X",
    # "XX  XX   XXXX   XXXX",
    # "XX              XXXX",
    # "XXXXXXXXX    XXXX  X",
    # "XXX   XXX    XXXX  X",
    # "XXX   XXX    XXXX  X",
    # "XXX          XXXX  X",
    # "XXXXXXXXX          X",
    # "XXXX           XXXXX",
    # "XXXX    XXXXXXXXXXXX",
    # "XXXX    XXXX   XX GX",
    # "XX             XX  X",
    # "XXXXXXXXXXXX       X",
    # "XXXXXX           XXX",
    # "XX       XX    XXXXX",
    # "XXXXXXXXXXXXXXXXXXXX"
]

treasures = []
enemies =[]
levels.append(level_1)


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 32)
            screen_y = 288 - (y * 32)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
                pen.shape("tile_x.gif")
            if character == "B":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
                pen.shape("tile_b.gif")

            if character == "L":
                pen.shape("tile_l.gif")
                pen.pensize(24)
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            if character == "R":
                pen.shape("tile_r.gif")
                pen.pensize(24)
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            if character == "T":
                pen.shape("tile_t.gif")
                pen.pensize(24)
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            if character == "B":
                pen.shape("tile_b.gif")
                pen.pensize(24)
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))


            if character == "1":
                pen.shape("tile_1.gif")
                pen.pensize(24)
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            if character == "2":
                pen.shape("tile_2.gif")
                pen.pensize(24)
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            if character == "3":
                pen.shape("tile_3.gif")
                pen.pensize(24)
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            if character == "4":
                pen.shape("tile_4.gif")
                pen.pensize(24)
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            if character == "J":
                pen.shape("tile_j.gif")
                pen.pensize(24)
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            if character == "K":
                pen.shape("tile_k.gif")
                pen.pensize(24)
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            if character == "=":
                pen.shape("tile_=.gif")
                pen.pensize(24)
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)
                print(player.position)

            if character == "G":
                treasures.append(Treasure(screen_x, screen_y))

            if character == "E":
                enemies.append(enemy(screen_x,screen_y))



pen = Pen()
player = Player()
walls = []
# setting up level
setup_maze(levels[1])
print(walls)

# keyboard binding
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

wn.tracer(0)
for enemy in enemies:
    turtle.ontimer(enemy.move , t=250)


# main game loop
while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)
    for enemy in enemies:
        if player.is_collision(enemy):
            print("enemy dies")

    wn.update()