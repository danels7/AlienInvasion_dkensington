import pygame
from pygame import Surface
from Ship import SHIPIMG
from AlienInvasion import WINDOWWIDTH
import json
import time
import util


pygame.font.init()
FONTASSET = util.font_asset("Silkscreen-Regular.ttf")
FONT = pygame.font.Font(FONTASSET, 30)


SCORES = util.file_asset("scores.json")

file = SCORES.open()
if not file.read().strip():
    file.close()
    file = SCORES.open('w')
    file.write(r"{}")
file.close
del file

# data format
# {
#   "<time (unix timestamp)>": <score (integer)>
# }

def get_high_score() -> int:
    with SCORES.open() as file:
        scores: dict[str, int] = json.load(file)
    return max(scores.values(), default=0)
    
def add_score(score: int) -> None:
    with SCORES.open() as file:
        scores: dict[str, int] = json.load(file)
    timeStr = str(int(time.time()))
    keys = scores.keys()
    if timeStr in keys: # you never know man
        timeStr += "_2"
        app = 3
        while timeStr in keys:
            timeStr = timeStr[:-1] + str(app)
            app += 1
    scores[timeStr] = score
    with SCORES.open('w') as file:
        json.dump(scores, file)
        

class PlayerStats:
    def __init__(self, screen: Surface):
        self.lives = 3
        self.score = 0
        self.level = 0
        self.highScore = get_high_score()

        self.screen = screen

        self.scoreText = FONT.render("Score: 0", False, pygame.Color(0xff, 0xff, 0xff))
        self.livesText = FONT.render("Lives:", False, pygame.Color(0xff, 0xff, 0xff))
        self.ship1 = SHIPIMG.copy()
        self.ship2 = SHIPIMG.copy()
        self.highScoreText = FONT.render(f"High Score: {self.highScore}", False, pygame.Color(0xff, 0xff, 0xff))
        self.extraLivesText = FONT.render(f"+0", False, pygame.Color(0xff, 0xff, 0xff))

        self.scoreTextRect = self.scoreText.get_rect()
        self.scoreTextRect.x = round((WINDOWWIDTH/2) - (self.scoreTextRect.width/2))
        self.scoreTextRect.y = 0

        self.livesTextRect = self.livesText.get_rect()
        self.livesTextRect.x = 0
        self.livesTextRect.y = 0

        self.ship1rect = self.ship1.get_rect()
        self.ship1rect.x = self.livesTextRect.width
        self.ship1rect.y = 0
        
        self.ship2rect = self.ship2.get_rect()
        self.ship2rect.x = self.livesTextRect.width + self.ship1rect.width
        self.ship2rect.y = 0

        self.highScoreTextRect = self.highScoreText.get_rect()
        self.highScoreTextRect.x = WINDOWWIDTH - self.highScoreTextRect.width
        self.highScoreTextRect.y = 0

        self.extraLivesTextRect = self.extraLivesText.get_rect()
        self.extraLivesTextRect.x = self.livesTextRect.width + self.ship1rect.width + self.ship2rect.width
        self.extraLivesTextRect.y = 0

    def save_score(self) -> None:
        if self.score != 0:
            add_score(self.score)

    def add_score(self, amount: int) -> None:
        self.score += amount
        self.scoreText = FONT.render(f"Score: {self.score}", False, pygame.Color(0xff, 0xff, 0xff))
        self.scoreTextRect = self.scoreText.get_rect()
        self.scoreTextRect.x = round((WINDOWWIDTH/2) - (self.scoreTextRect.width/2))
        self.scoreTextRect.y = 0

    def remove_life(self) -> None:
        self.lives -= 1
        self.extraLivesText = FONT.render(f"+{self.lives-3}", False, pygame.Color(0xff, 0xff, 0xff))
        self.extraLivesTextRect = self.extraLivesText.get_rect()
        self.extraLivesTextRect.x = self.livesTextRect.width + self.ship1rect.width + self.ship2rect.width
        self.extraLivesTextRect.y = 0

    def add_life(self) -> None:
        self.lives += 1
        self.extraLivesText = FONT.render(f"+{self.lives-3}", False, pygame.Color(0xff, 0xff, 0xff))
        self.extraLivesTextRect = self.extraLivesText.get_rect()
        self.extraLivesTextRect.x = self.livesTextRect.width + self.ship1rect.width + self.ship2rect.width
        self.extraLivesTextRect.y = 0

    def get_lives(self) -> int:
        return self.lives
    
    def level_up(self) -> None:
        self.level += 1

    def get_level(self) -> int:
        return self.level
    
    def get_score(self) -> int:
        return self.score
    
    def draw_stats(self) -> None:
        self.screen.blit(self.scoreText, self.scoreTextRect)
        self.screen.blit(self.highScoreText, self.highScoreTextRect)

        self.screen.blit(self.livesText, self.livesTextRect)
        displayLives = self.lives - 1
        if displayLives >= 1:
            self.screen.blit(self.ship1, self.ship1rect)
        if displayLives >= 2:
            self.screen.blit(self.ship2, self.ship2rect)
        if displayLives >= 3:
            self.screen.blit(self.extraLivesText, self.extraLivesTextRect)