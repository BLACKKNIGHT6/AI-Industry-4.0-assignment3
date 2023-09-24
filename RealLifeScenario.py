# Patient data
patients = ["A", "B", "C", "D"]
arrival_time = [0, 10, 15, 20]
treatment_time = [30, 20, 40, 15]
urgency_level = [3, 5, 2, 4]

# Initialize variables to store results
waiting_time = {p: 0 for p in patients}
turnaround_time = {p: 0 for p in patients}

# FCFS Scheduling
current_time_fcfs = 0
for i in range(len(patients)):
    waiting_time[patients[i]] = max(current_time_fcfs - arrival_time[i], 0)
    current_time_fcfs += treatment_time[i]
    turnaround_time[patients[i]] = current_time_fcfs - arrival_time[i]

# SJF Scheduling
sorted_patients_sjf = [p for _, p in sorted(zip(treatment_time, patients))]
current_time_sjf = 0
for patient in sorted_patients_sjf:
    index = patients.index(patient)
    waiting_time[patient] = max(current_time_sjf - arrival_time[index], 0)
    current_time_sjf += treatment_time[index]
    turnaround_time[patient] = current_time_sjf - arrival_time[index]

# Priority Scheduling
sorted_patients_priority = [p for _, p in sorted(zip(urgency_level, patients))]
current_time_priority = 0
for patient in sorted_patients_priority:
    index = patients.index(patient)
    waiting_time[patient] = max(current_time_priority - arrival_time[index], 0)
    current_time_priority += treatment_time[index]
    turnaround_time[patient] = current_time_priority - arrival_time[index]

# Assess the results
min_waiting_time = min(waiting_time.values())
min_turnaround_time = min(turnaround_time.values())

# Determine the best scheduling method based on the results
best_method = None
if min_waiting_time == min_turnaround_time:
    best_method = "SJF (Shortest Job First)"
elif min_waiting_time < min_turnaround_time:
    best_method = "SJF (Shortest Job First)"
else:
    best_method = "Priority Scheduling"

# Print results and assessment
for patient in patients:
    print(f"{patient}: Waiting Time = {waiting_time[patient]}, Turnaround Time = {turnaround_time[patient]}")

print(f"The best scheduling method according to the results is {best_method}.")
