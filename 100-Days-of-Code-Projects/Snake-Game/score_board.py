from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, 'normal'))
        self.hideturtle()
        with open('data.txt') as score:
            self.highscore = int(score.read())

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align='center', font=("Arial", 24, 'normal'))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest score: {self.highscore}" , align="center", font=("Arial", 24, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode='w') as points:
                points.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.clear()
        self.score +=1
        self.update_scoreboard()
