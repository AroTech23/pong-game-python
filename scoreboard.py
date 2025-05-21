from turtle import  Turtle,Screen
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.goto (-100 , 230 )
        self.write (self.l_score , align="center" , font=("Courier" , 60 , "normal"))
        self.goto (100 , 230 )
        self.write ( self.r_score , align="center" , font=("Courier" , 60 , "normal"))
        screen = Screen()
        screen.title ( f"Pong | Left: {self.l_score}  Right: {self.r_score}" )

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self , winner):
        self.goto ( 0 , 0 )
        self.color("Green")
        self.write ( f"Game Over\n{winner} Wins!" , align="center" , font=("Courier" , 30 , "bold") )

    def reset_scores(self):
        self.l_score = 0
        self.r_score = 0
        self.clear ()
        self.update_scoreboard ()
