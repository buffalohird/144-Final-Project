SmarteRun: The Coach You Didn’t Know You Had

Mark Grozen-Smith, Buffalo Hird, Neel Patel
{grozensmith, buffalohird, npatel}@college.harvard.edu

Our code is divided into multiple python .py files which each encapsulate a piece of our final software.  Our directory also includes mutliple .csv's which each contain the data of a sample run used in our analysis.  

##########
Below is a brief description of each file
###########
analyze.py:
  A set of functions to calculate the accuracy of our predictions versus actual run data using root mean squared, etc.
average.py:
  The main algorithmic component, this file contains many of the functions which help transform, normalize, and calculate runs based on the input of previous run data.
plotter.py
  This file contains the Plotter class, which serves the purpose of receiving run data and outputting it to graphs
predict.py
  This file contains functions which create our final predictions given a plot generated from input in average.py
running.py
  This is a test "main function" which shows a sample execution of reading in and graphing a sample run (saved as a .csv)
storage.py
  This is an input/output class Storage which serves the purpose of reading runs from .csv's to be used as input for our algorithms and as saving runs to .csv's to be used later as input (or as output to be presented to the user as their prediction)
tester.py
  This is a test data generating class which serves the purpose of generating reasonable run data given parameters of a starting speed.  We used real data in generating the relative probabilities for how a runner's pace might change over the course over an activity.
testerPace.py
  This is a test data generating class for generating graphs of a runner's pace over the course of a run.  Pace is beyond the scope of our project but we wanted to demonstrate its feasible utility in better predictions.

  ##########
  Layout of code / How-To run code
  ##########
  We have multiple components encapsulated in separate files / classes.  Most succintly, our code is orgnaized around the control flow:
    storage.py -> average.py -> predict.py -> plotter.py/storage.py

We provide a sample file, running.py, to show how these files can all be interfaced with iteratively from a given file.