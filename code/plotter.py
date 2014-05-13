import matplotlib.pyplot as plt


# simple implementation of matplotlib graphing library
class Plotter:
  def __init__(self):
    self.hello = []


  # given a set of coordinates of speed and time, will graph this run
  """
  def graphRun(self, run):
    xList, yList = zip(*run)
    list(xList)
    list(yList)
    xMax = max(xList) * 1.5
    yMax = max(yList) * 1.5

    plt.plot(xList, yList, 'ro')
    plt.axis([0, xMax, 0, yMax])
    plt.show()
  """


  def createGraph(self, runs,colors=[]):
    xMax = 0
    yMax = 0
    if colors == []:
      colors = ['r', 'b', 'y','c','go']
      #colors = ['r', 'b', 'g', 'y','c', 'm','k','w','go']

    for run in runs:
      xList, yList = zip(*run)
      list(xList)
      list(yList)
      xMax = max(xMax, max(xList) * 1.5)
      yMax = max(yMax, max(yList) * 1.5)

      
      plt.plot(xList, yList, colors[0])
      colors.pop(0)

    plt.axis([0, xMax, 0, yMax])
    plt.xlabel('time (seconds)')
    plt.ylabel('distance (meters)')
    plt.show()



# example usage
"""
plotter = Plotter()
plotter.createRun([ [[x_0,y_0],...,[x_n,y_n]], [[x_0,y_0],....,[x_n,y_n]], [x_0,y_0],....,[x_n,y_n]]])
"""


