from json import JSONEncoder


class RankingLine:

  def __init__(self, position, teamName, points, played, win, draw, lose, forfait, goal, goalAgainst, penalty, goalDifference):
    self.position = position
    self.teamName = teamName
    self.points = points
    self.played = played
    self.win = win
    self.draw = draw
    self.lose = lose
    self.forfait = forfait
    self.goal = goal
    self.goalAgainst = goalAgainst
    self.penalty = penalty
    self.goalDifference = goalDifference

class RankingLineEncoder(JSONEncoder):
  def default(self, o):
    return o.__dict__