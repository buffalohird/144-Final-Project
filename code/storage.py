import time
import csv




class Storage:
  def __init__(self):
    self.runFiles = ["10minute1.csv","10minute5.csv","5minute4.csv",  "fast10minute3.csv", "10minute2.csv","5minute1.csv","5minute5.csv","fast10minute4.csv","10minute3.csv","5minute2.csv","fast10minute1.csv","fast10minute5.csv","10minute4.csv","5minute3.csv","fast10minute2.csv","test1.csv"]

  def setRuns(self, runs):
    self.runFiles = runs

  # given a file name of a csv will read it and return that data when Storage.readRun() is called
  def readRun(self, inputFile):
    try:
      with open(inputFile, "rU") as csvFile:
        returnPoints = []
        csvReader = csv.reader(csvFile)

        if csvReader == []:
          print "empty reader"
          time.sleep(100)
        for row in csvReader:
          returnPoints.append(map(float, row))

        return returnPoints
    except IOError:
      print "IOERROR is raised. Error opening file %s with logger.py" % (str(inputFile)) 


  def readRunDistance(self, inputFile):
    try:
      with open(inputFile, "rU") as csvFile:
        csvReader = csv.reader(csvFile)
        if csvReader == []:
          print "empty reader trying to read distance of run %s" % (inputFile)
          time.sleep(100)
        for row in csvReader:
          return float(row[0])
    except IOError:
      print "IOERROR is raised. Error opening file %s with logger.py" % (str(inputFile)) 


  # given a list of lists to save and a file name will save csv of lists to name
  def saveRun(self, distance, outputData, outputFile):
    with open(outputFile, 'w+') as writeFile:
      csvWriter = csv.writer(writeFile)
      csvWriter.writerow([distance])
      for row in outputData:
        print row
        csvWriter.writerow(row)


  def findNClosestRuns(self, distance, n):
    closestRunsList = []
    for runString in self.runFiles:
      closestRunsList.append([self.readRunDistance(runString), runString])

    #print closestRunsList
    #print distance
    closestRunsList = sorted(closestRunsList, key=lambda x: abs(x[0]-distance))

    #print closestRunsList

    if n > len(closestRunsList):
      print "error trying to return %d closest graphs" % (n)
    if n == 1:
      return closestRunsList[0:1]
    else:
      return closestRunsList[0:n-1]







# example usage

# find the n closest runs to a given distance to use for calculating
#storage = Storage()
#x = storage.findNClosestRuns(5000.0, n)


# save a run
#storage = Storage()
#storage.saveRun(5000.0 #meters, [[x,y][x,y]], 'filename.csv')
#






