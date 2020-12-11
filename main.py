import turtle



boo = turtle.Turtle()
screen = turtle.Screen()

turtle.colormode(255)
boo.shape("classic")
boo.color("blue")
boo.speed(0)
boo.pensize(5)
screen.bgcolor("black")



# 10 x 10
# size 20 space 50

def hirst_painting():
    game_on = -100
    after_first_round = -100
    dot_start = -1

    while game_on < 100:
        boo.penup()
        boo.setpos(-200, game_on)

        for x in range(15):
            if (game_on == -90) and (x == 7):
                boo.color("red")
                boo.pendown()
                boo.forward(0)
                boo.penup()
                boo.forward(8)
            elif game_on == (after_first_round) and game_on < -10 and x >= 7-dot_start and x <= 7+dot_start:

                boo.color("red")
                boo.pendown()
                boo.forward(0)
                boo.penup()
                boo.forward(8)

            elif game_on == -10:
                if x >= 0 and x <= 6:
                    boo.color("red")
                    boo.pendown()
                    boo.forward(0)
                    boo.penup()
                    boo.forward(8)
                elif x >= 8 and x <= 14:
                    boo.color("red")
                    boo.pendown()
                    boo.forward(0)
                    boo.penup()
                    boo.forward(8)
                else:
                    boo.penup()
                    boo.forward(0)
                    boo.penup()
                    boo.forward(8)
            elif game_on == 0:
                if x >= 1 and x <= 5:
                    boo.color("red")
                    boo.pendown()
                    boo.forward(0)
                    boo.penup()
                    boo.forward(8)
                elif x >= 9 and x <= 13:
                    boo.color("red")
                    boo.pendown()
                    boo.forward(0)
                    boo.penup()
                    boo.forward(8)
                else:
                    boo.penup()
                    boo.forward(0)
                    boo.penup()
                    boo.forward(8)
            elif game_on == 10:
                if x >= 2 and x <= 4:
                    boo.color("red")
                    boo.pendown()
                    boo.forward(0)
                    boo.penup()
                    boo.forward(8)
                elif x >= 10 and x<= 12:
                    boo.color("red")
                    boo.pendown()
                    boo.forward(0)
                    boo.penup()
                    boo.forward(8)
                else:
                    boo.penup()
                    boo.forward(0)
                    boo.penup()
                    boo.forward(8)


            elif game_on >= 20:
                boo.penup()
                boo.forward(0)
                boo.penup()
                boo.forward(8)
            else:
                boo.pencolor("darkgrey")
                boo.pendown()
                boo.forward(0)
                boo.penup()
                boo.forward(8)

        game_on += 10
        after_first_round += 10
        dot_start += 1
        print(after_first_round+10)
        print(game_on)


hirst_painting()



















# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     my_colors = (r, g, b)
#     return my_colors
#
#
# def draw_circle(circles):
#
#     for circle in range(int(360/circles)):
#         boo.pencolor(random_color())
#         boo.circle(75)
#         boo.setheading(boo.heading() + circles)
#
#
# draw_circle(100)
#













# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     my_colors = (r, g, b)
#     return my_colors
#
#
# angles = [0, 90, 180, 270, 360]
#
# def draw_random_line(how_many_lines):
#     for move in range(how_many_lines):
#         boo.pencolor(random_color())
#         turn = [boo.right(random.choice(angles)), boo.left(random.choice(angles))]
#         random.choice(turn)
#         boo.forward(30)
#
# draw_random_line(200)








# def draw_shape(angles):
#     for side in range(7):
#         angle_dim = 360 / angles
#         boo.pencolor(random.choice(colors))
#         for move in range(angles):
#             boo.forward(100)
#             boo.right(angle_dim)
#         angles += 1
# draw_shape(5)











# def draw_triangle():
#
# def draw_square():
#     for move in range(4):
#         boo.forward(100)
#         boo.right(90)
#
# def draw_pentagon():
#
# def draw_hexagon():
#
# def draw_heptagon():
#
# def draw_octagon():
#
# def draw_nonagon():
#
# def draw_decadon()

















# def draw_dashed_line():
#
#     for dash in range(10):
#         boo.pendown()
#         boo.forward(10)
#         boo.penup()
#         boo.forward(10)





screen.exitonclick()