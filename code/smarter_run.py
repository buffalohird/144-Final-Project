#stringing all components together
import average, predict, weighting, running, storage
from plotter import Plotter
from random import randint

#time, distance, total distance, num
def smarter_predict(x=300,y=1000,z=5000.0,n=5, runs=None):
	#finds the n closest runs to start off
	data = storage.Storage()

	if runs:
		data.setRuns(runs)	

	closest = data.findNClosestRuns(z, n)

	#now reads in the actual data for these runs
	lists = []
	for distance,name in closest:
		current_data = data.readRun(name)[1:]
		lists.append(current_data)

	#calculates the weights for these runs
	weights = []
	for distance,name in closest:
		weights.append(weighting.weightDistance(z,distance))	

	#now calculates the average runs
	combined = average.averageN(lists,1000,weights)

	#now gives a prediction
	prediction = predict.secant_prediction(combined,y,x,z)
	sec_pred = prediction["prediction"]
	multiple = prediction["multiple"]

	#un-normalizes the data
	rescaled = [(time*multiple,distance) for (time,distance) in combined]

	plotter = Plotter()
	#plotter.createGraph([rescaled,[(x,y)]],['r', 'bo'])

	return {"prediction": sec_pred}


def test(n=1):	
	for i in range(n):
		data = storage.Storage()

		runs = ["10minute1.csv","10minute5.csv","5minute4.csv",  "fast10minute3.csv", "10minute2.csv","5minute1.csv","5minute5.csv","fast10minute4.csv","10minute3.csv","5minute2.csv","fast10minute1.csv","fast10minute5.csv","10minute4.csv","5minute3.csv","fast10minute2.csv"]
		index = randint(0,len(runs)-1)		
		current = runs.pop(index)
		current_data = data.readRun(current)[1:]
		
		#get the last time and distance from the current run
		last_time = current_data[-1][0]
		last_distance = current_data[-1][1]

		#generate a random number in this range 
		random_time = randint(1,last_time-1)
		random_distance = current_data[random_time][1]

		prediction = smarter_predict(random_time, random_distance, last_distance, 5, runs)
		actual = smarter_predict(random_time, random_distance, last_distance, 1, [current])

		#print current, random_time, random_distance, prediction, actual
		print current, random_distance, last_distance, actual["prediction"], prediction["prediction"]

test(5000)

#print smarter_predict(600,1000,5000,5)

