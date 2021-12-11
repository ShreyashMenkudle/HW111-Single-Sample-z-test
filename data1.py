import plotly.figure_factory as ff
import csv
import statistics
import pandas as pd
import plotly.graph_objects as go
import random

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)

    return mean


mean_list = []
for i in range(1,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)
mean = statistics.mean(mean_list)
print("Sampling Distribution",mean)
std_deviation = statistics.stdev(mean_list)
print("Standard Deviation",std_deviation)

    



first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation 
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation) 
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist() 
mean_of_sample = statistics.mean(data) 
print("Mean of sample:- ",mean_of_sample)

fig = ff.create_distplot([mean_list], ["reading time"], show_hist=False) 
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 
fig.add_trace(go.Scatter(x=[mean_of_sample, mean_of_sample], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE")) 
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END")) 
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END")) 
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END")) 
fig.show()

z_score = ( mean_of_sample - mean )/std_deviation 
print("The z score is = ",z_score)