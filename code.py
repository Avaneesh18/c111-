import csv
import plotly.figure_factroy as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

def randomsetofmean(counter):
  dataset = []
  for i in range(0,counter):
    randomindex = random.randint(0,len(data)-1)
    value = data[randomindex]
    dataset.append(value)

  mean = statistics.mean(dataset)
  return mean
meanlist = []

for i in range(0,1000):
  setofmean = randomsetofmean(100)
  meanlist.append(setofmean)

# calculate mean and std of sampling distibution
mean = statistics.mean(meanlist)
std = statistics.stdev(meanlist)

print("Mean is:",mean)
print("Standerd deviation is:",std)

#finding the std for starting and ending values
first_std_start,first_std_end = mean - std , mean + std
second_std_start,second_std_end = mean - (std*2), mean + (std*2)
third_std_start,third_std_end = mean - (std*3), mean + (std*3)

print("std 1 = ",first_std_start,first_std_end)
print("std 2 = ",second_std_start,second_std_end)
print("std 3 = ",third_std_start,third_std_end)

#mean of students giving extra time to mathlab
df = pd.read_csv("data1")
data = df["Math_score"].tolist()
meanofsample1 = statistics.mean(data)
print("Mean is",meanofsample1)

fig = ff.create_distplot([meanlist],["student marks"],show_hist = False)
fig.add_trace(do.Scatter(x = [mean,mean], y = [0,0.17],mode = "lines",name = "mean"))
fig.add_trace(do.Scatter(x = [meanofsample1,meanofsample1], y = [0,0.17],mode = "lines",name = "Mean of students ho took Mathlab seriously"))
fig.add_trace(do.Scatter(x = [first_std_end,first_std_end], y = [0,0.17],mode = "lines",name = "Mean of std 1 (end)"))
fig.add_trace(do.Scatter(x = [third_std_end,third_std_end], y = [0,0.17],mode = "lines",name = "Mean of std 3 (end)"))
fig.add_trace(do.Scatter(x = [second_std_end,second_std_end], y = [0,0.17],mode = "lines",name = "Mean of std 2 (end)"))
fig.show()

#mean of students who use math practice app
df = pd.read_csv("data2")
data = df["Math_score"].tolist()
meanofsample2 = statistics.mean(data)
print("Mean is",meanofsample2)

fig = ff.create_distplot([meanlist],["student marks"],show_hist = False)
fig.add_trace(do.Scatter(x = [mean,mean], y = [0,0.17],mode = "lines",name = "mean"))
fig.add_trace(do.Scatter(x = [meanofsample2,meanofsample2], y = [0,0.17],mode = "lines",name = "Mean of students how took math prctice app seriously"))
fig.add_trace(do.Scatter(x = [first_std_end,first_std_end], y = [0,0.17],mode = "lines",name = "Mean of std 1 (end)"))
fig.add_trace(do.Scatter(x = [third_std_end,third_std_end], y = [0,0.17],mode = "lines",name = "Mean of std 3 (end)"))
fig.add_trace(do.Scatter(x = [second_std_end,second_std_end], y = [0,0.17],mode = "lines",name = "Mean of std 2 (end)"))
fig.show()

#mean of student who were forced to do extra homework
df = pd.read_csv("data3")
data = df["Math_score"].tolist()
meanofsample3 = statistics.mean(data)
print("Mean is",meanofsample3)

fig = ff.create_distplot([meanlist],["student marks"],show_hist = False)
fig.add_trace(do.Scatter(x = [mean,mean], y = [0,0.17],mode = "lines",name = "mean"))
fig.add_trace(do.Scatter(x = [meanofsample3,meanofsample3], y = [0,0.17],mode = "lines",name = "Mean of students how lied to the teacher"))
fig.add_trace(do.Scatter(x = [first_std_end,first_std_end], y = [0,0.17],mode = "lines",name = "Mean of std 1 (end)"))
fig.add_trace(do.Scatter(x = [third_std_end,third_std_end], y = [0,0.17],mode = "lines",name = "Mean of std 3 (end)"))
fig.add_trace(do.Scatter(x = [second_std_end,second_std_end], y = [0,0.17],mode = "lines",name = "Mean of std 2 (end)"))
fig.show()

#find the Z score using the formule
z_score = (mean-meanofsample2)/std
print("z score is: ",z_score)



