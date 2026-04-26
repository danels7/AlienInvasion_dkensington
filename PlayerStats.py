from pygame import Surface
import json
import time
import util


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
        self.screen = screen
        self.lives = 3
        self.score = 0
        self.level = 0
        self.highScore = get_high_score()

    def save_score(self) -> None:
        add_score(self.score)

    def add_score(self, amount: int) -> None:
        self.score += amount

    def remove_life(self) -> None:
        self.lives -= 1

    def get_lives(self) -> int:
        return self.lives
    
    def level_up(self) -> None:
        self.level += 1

    def get_level(self) -> int:
        return self.level