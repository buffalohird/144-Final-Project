import csv
import matplotlib.pyplot as plt
import math

def rmse(actual, predicted):
	resid = [(a-b)**2 for (a,b) in zip(actual, predicted)]
	total = float(sum(resid)) / len(resid)
	return math.sqrt(total)

with open("5000.txt") as file:
	reader = csv.reader(file, delimiter=' ')
	actual = []
	predicted = []
	data = []

	for row in reader:
		data.append({"name": row[0], "distance": float(row[1]), "total": float(row[2]), "actual": float(row[3]), "predicted": float(row[4])})		
		actual.append(float(row[3]))
		predicted.append(float(row[4]))

	short = [x for x in data if float(x["total"]) < 3000]
	long = [x for x in data if float(x["total"]) > 5000]
	
	short_pred = [x["predicted"] for x in short]
	short_act = [x["actual"] for x in short]
	long_pred = [x["predicted"] for x in long]
	long_act = [x["actual"] for x in long]

	first_half = [x for x in data if (x["distance"] / x["total"] < 0.5)]
	second_half = [x for x in data if (x["distance"] / x["total"] >= 0.5)]

	first_half_pred = [x["predicted"] for x in first_half]
	first_half_act = [x["actual"] for x in first_half]
	second_half_pred = [x["predicted"] for x in second_half]
	second_half_act = [x["actual"] for x in second_half]
	
	print "Short RMSE", rmse(short_act, short_pred), "over", len(short)
	print "Long RMSE", rmse(long_act, long_pred), "over", len(long)
	print "First 1/2 RMSE", rmse(first_half_act, first_half_pred), "over", len(first_half)
	print "Second 1/2 RMSE", rmse(second_half_act, second_half_pred), "over", len(second_half)
	print "All RMSE", rmse(actual, predicted), "over", len(data)	

	fig = plt.figure()
	fig.patch.set_facecolor("white")
	plt.xlabel("Actual pace in m/s")
	plt.ylabel("Predicted pace in m/s")

	#all
	#plt.scatter(actual, predicted, marker='.')
	#plt.savefig("all.png")

	#long vs short
	#plt.scatter(short_act, short_pred, marker='.', color = "b")
	#plt.scatter(long_act, long_pred, marker='.', color = "r")
	#plt.savefig("longshort.png")


	#first 1/2 vs second 1/2
	plt.scatter(first_half_act, first_half_pred, marker='.', color = "b")
	plt.scatter(second_half_act, second_half_pred, marker='.', color = "r")
	plt.savefig("halves.png")

	#plt.plot([0,7], [0,7], color=(1,.6,.0,.5), linestyle='-', linewidth=5)
	plt.show()	

