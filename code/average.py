from plotter import Plotter

#Given an individual tuple of the form (time,distance) and a start,end value,
#Returns that tuple normalized WRT time
def normalize_point(tuple,start,end):
	if start==end:
		return tuple	
	return (float(tuple[0] - start) / float(end - start),tuple[1])

#Given a list of tuples of the form (time,distance),
#Returns the same data with time normalized from 0 to 1
def normalize(l1):
	#first makes sure that the list is sorted
	sort = sorted(l1, key=lambda x:x[0])
	start = sort[0][0]
	end = sort[-1][0]

	normalized = []
	for current in l1:
		normalized.append(normalize_point(current,start,end))

	return normalized

#Given a list of tuples of the form (time,distance) and a time value,
#Returns the tuples directly before and after it
def before_after(l1,time):
	for i in range(len(l1)):
		if l1[i][0] > time:
			return (l1[i-1], l1[i]) 	
	return (l1[-1], l1[-1])

#Given a before and an after tuple and a time value,
#Returns the simulated value at the time value between the two
def simulated(before,after,time):
	sim = before[1] + float(time - before[0])/float(after[0] - before[0]) * (after[1] - before[1])
	return sim

#averages a list of points
def averageList(l1):
	return float(sum(l1))/len(l1)

#weighted average of list of points
def weightedAverageList(l1,weights):
	weighted = []
	for i in range(len(l1)):
		weighted.append(float(l1[i]) * weights[i])
	return float(sum(weighted))/sum(weights)

#Given two lists of tuples of the form (time, distance),
#Returns the 'average' line between them at a given sample rate
def average2(l1,l2,step):
	norm1 = normalize(l1)
	norm2 = normalize(l2)

	result = []

	for i in [float(x)/step for x in range(0,int(step))]:
		before1, after1 = before_after(norm1,i)
		before2, after2 = before_after(norm2,i)

		#creates the simulated values based on a line between before and after
		sim1 = simulated(before1,after1,i)
		sim2 = simulated(before2,after2,i)

		#now averages these two simulated values 
		result.append((i,(sim1 + sim2)/2))
	return result

#Given a list of lists of tuples of the form (time,distance),
#Returns the 'average' line between them at a given sample rate
#Using a weighting based on distance
def averageN(lists,step,weights=[]):
	if weights == []:
		weights = [1 for i in range(len(lists))]		
	normalized = []
	for current in lists:
		normalized.append(normalize(current))	

	result = []

	for i in [float(x)/step for x in range(0,int(step))]:	
		#calculates before/after now
		beforeAfter = []
		for current in normalized:
			beforeAfter.append(before_after(current,i))
		
		#creates the simulated values based on a line between before and after
		simulatedResults = []
		for (before,after) in beforeAfter:
			simulatedResults.append(simulated(before,after,i))

		#now averages these two simulated values 
		result.append((i,weightedAverageList(simulatedResults,weights)))
	
	#graphs
	#plotter = Plotter()
	#plotter.createGraph(lists)
	#plotter.createGraph(normalized)
	#plotter.createGraph(normalized + [result])

	return result

