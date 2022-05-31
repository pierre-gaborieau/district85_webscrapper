from json import JSONEncoder


class RankingLine:

  def __init__(self, position : int, teamName : str, points : int, played, win, draw, lose, forfait, goal, goalAgainst, penalty, goalDifference):
    self.position = int(position)
    self.teamName = str(teamName)
    self.points = int(points)
    self.played = int(played)
    self.win = int(win)
    self.draw = int(draw)
    self.lose = int(lose)
    self.forfait = int(forfait)
    self.goal = int(goal)
    self.goalAgainst = int(goalAgainst)
    self.penalty = int(penalty)
    self.goalDifference = int(goalDifference)

class RankingLineEncoder(JSONEncoder):
  def default(self, o):
    return o.__dict__