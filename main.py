from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
WINNING_SCORE = 5
scoreboard=Scoreboard()
screen=Screen()
screen.bgcolor("black")
is_paused=False

def toggle_pause():
    global is_paused
    is_paused = not is_paused
    if is_paused:
        disable_controls ()
        print ( "Paused" )
    else:
        enable_controls ()
        print ( "Resumed" )
def enable_controls():
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")
def disable_controls():
    screen.onkey(lambda:None, "Up")
    screen.onkey(lambda:None, "Down")
    screen.onkey(lambda:None, "w")
    screen.onkey(lambda:None, "s")




screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)
paddle=Turtle()
r_paddle=Paddle((350, 0))
l_paddle=Paddle((-350, 0))
ball=Ball()





def countdown():
    countdown_turtle = Turtle()
    countdown_turtle.color("red")
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.goto(0, 0)
    for i in range(3, 0, -1):
        countdown_turtle.clear()
        countdown_turtle.write(str(i), align="center", font=("Courier", 50, "bold"))
        screen.update()
        time.sleep(1)
    countdown_turtle.clear()
    countdown_turtle.write("Go!", align="center", font=("Courier", 40, "bold"))
    screen.update()
    time.sleep(1)
    countdown_turtle.clear()
    screen.update()
def restart_game():
    global is_game_on, is_paused
    is_game_on = True
    is_paused = False
    scoreboard.reset_scores()
    r_paddle.goto(350, 0)
    l_paddle.goto(-350, 0)
    ball.reset_position()
    countdown()

# Run the countdown before the game loop
countdown()
screen.listen()
enable_controls()


screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(toggle_pause, "space")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(restart_game, "r")






is_game_on=True
while is_game_on:

    time.sleep(ball.move_speed)
    screen.update()
    if not is_paused:
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
            #detect collision with paddle§
        if (320 < ball.xcor () < 360 and abs ( ball.ycor () - r_paddle.ycor () ) < 60) or \
            (-360 < ball.xcor () < -320 and abs ( ball.ycor () - l_paddle.ycor () ) < 60):

            ball.bounce_x ()
        #Detect when right paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()
        #Detect when left paddle misses
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()
        # Check if left or right player won
        if scoreboard.l_score == WINNING_SCORE:
            scoreboard.game_over ( "Left Player" )
            is_game_on = False
        elif scoreboard.r_score == WINNING_SCORE:
            scoreboard.game_over ( "Right Player" )
            is_game_on = False



screen.exitonclick()