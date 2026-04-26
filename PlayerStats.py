import json
import time
from util import file_asset


SCORES = file_asset("scores.json")

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

def get_high_score():
    with SCORES.open() as file:
        scores: dict[str, int] = json.load(file)
    return max(scores.values())
    
def add_score(score: int):
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
    def __init__(self):
        self.lives = 3
        self.score = 0
        self.highScore = get_high_score()