from storage import Storage
from plotter import Plotter
from storage import Storage
import random

# test data generating class - produces sample runs
class Tester:
  def __init__(self):
    self.hello = []


  # creates a run for a given time interval and starting speed using probabilistic speed changes over the course
  # of this time period
  def createRun(self, T=600, startSpeed=10):
    returnArray = []
    distance = 0.0
    lastChange = 1.0
    speed = startSpeed # meters / second
    for t in xrange(T):
      distance += speed
      returnArray.append(distance)
      [speed, lastChange] = self.alterSpeed(speed, lastChange)

    return returnArray

  # probabilistic function to alter the speed of a runner over each time interval of an activity
  # we emperically determined these values based on reasonable analysis of real run data
  def alterSpeed(self, speed, lastChange):

    modifier = random.random() # between 0.0 and 1.0
    """
    if lastChange <= 0.99:
      return [speed * 1.0, 1.0]
    if lastChange >= 1.00:
      return [speed * 1.0, 1.0]
    """

    if modifier <= 0.1:
      return [speed * 0.95, 0.95]
    if modifier <= 0.2:
      return [speed * 0.96, 0.96]
    if modifier <= 0.3:
      return [speed * 0.97, 0.97]
    if modifier <= 0.4:
      return [speed * 0.98, 0.98]
    if modifier <= 0.5:
      return [speed * 0.99, 0.99]
    if modifier <= 0.6:
      return [speed * 1.01, 1.01]
    if modifier <= 0.7:
      return [speed * 1.02, 1.02]
    if modifier <= 0.8:
      return [speed * 1.03, 1.03]
    if modifier <= 0.9:
      return [speed * 1.04, 1.04]
    if modifier <= 1.0:
      return [speed * 1.05, 1.05]


# sample usage of this, displaying a run being created, plotted, and saved
"""
tester = Tester()
run = tester.createRun()
enumeratedRun = enumerate(run)
plotter = Plotter()
#plotter.createGraph(enumeratedRun)
distance = run[len(run) - 1]

storage = Storage()
storage.saveRun(distance, enumeratedRun, "fast10minute5.csv")
"""







