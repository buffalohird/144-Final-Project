#average is a list of (time,distance) tuples
#first find the time closest to 'distance'
def closest(average,distance):
	for t,d in average:
		if d > distance:
			return t
	return average[-1][0]

# ---- Gives you the secant line for a given point
#Given an average run and your current distance, 
#Returns your predicted pace to stay on track
def secant_prediction(average,distance,time,goal):	

	cur_time = closest(average,distance) * (distance / goal)
	goal_time = closest(average,goal)	

	#if we need to discunt backwards
	if cur_time == goal_time:
		cur_time = cur_time * (distance / goal)

	#we know cur_time (from 0 to 1) actually matches to time	
	multiple = float(time) / cur_time
	cur_time *= multiple
	goal_time *= multiple	
		
	return {"prediction": (goal - distance) / (goal_time - cur_time), "multiple": multiple}
	
# ---- Gives you the tangent line for a given point
#Given an average run and your current distance, 
#Returns your predicted pace based on the current spot in past runs
#Time is actually not needed; nor is goal	
def tangent_prediction(average,distance,goal):
	return 1
