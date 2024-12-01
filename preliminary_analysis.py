from datetime import datetime, timedelta, time
import numpy as np
import pm4py
import statistics as stat
import os

log_1 = pm4py.read_xes(str(os.getcwd()) + "/input-logs/L1.xes.gz")
event_log_1 = pm4py.convert_to_event_log(log_1)


log_2 = pm4py.read_xes(str(os.getcwd()) + "/input-logs/L2.xes.gz")
event_log_2 = pm4py.convert_to_event_log(log_2)


print("There are " + str(len(event_log_2)) + " cases")
print("There are " + str(len(log_2)) + " events")
#print("There are " + str(len(set(log["concept:name"]))) + " unique activites")
#print("The earliest event happend on " + str(min(log["time:timestamp"])))
#print("The latest event happend on " + str(max(log["time:timestamp"])) +"\n")

print("There are " + str(len(pm4py.get_variants(log_2))) + " variants")
sum = 0
for order in log_1:
    sum += len(order)


all_case_durations = pm4py.get_all_case_durations(log_2)

print("4. he average number of events per case is " + str(sum/len(pm4py.get_variants(log_2))) +"\n")
print("6. is " + str(len(set(log_2["org:resource"]))))
print("7. Longest is: " + str(max(all_case_durations)))
print("8. Shortest is: " + str(min(all_case_durations)))
print("9. Median is: " + str(stat.median(all_case_durations)))
print("10. Mean is: " + str(stat.mean(all_case_durations)))
