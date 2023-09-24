import numpy as np

processes = ['P1', 'P2', 'P3', 'P4']
arrival_times = [0, 4, 5, 6] 
burst_times = [24, 3, 3, 12]
priorities = [3, 1, 4, 2]

def fcfs(processes, burst_times):
    waiting_times = [0] * len(processes) 
    turnaround_times = [0] * len(processes)
    
    for i in range(1, len(processes)):
        waiting_times[i] = burst_times[i-1] + waiting_times[i-1]
        turnaround_times[i] = burst_times[i] + waiting_times[i]
        
    return waiting_times, turnaround_times

def sjf(processes, burst_times, arrival_times):
    waiting_times = [0] * len(processes)
    turnaround_times = [0] * len(processes)
    
    ready_queue = []
    current_time = 0
    
    while len(ready_queue) != len(processes):
        
        for i in range(len(processes)):
            if arrival_times[i] <= current_time and i not in ready_queue:
                ready_queue.append(i)
                
        if ready_queue:
            shortest = ready_queue[np.argmin(burst_times[i] for i in ready_queue)]
            burst_times[shortest] -= 1
            current_time += 1
            
            if burst_times[shortest] == 0:
                waiting_times[shortest] = current_time - arrival_times[shortest] 
                turnaround_times[shortest] = current_time - arrival_times[shortest]
                ready_queue.remove(shortest)
                
    return waiting_times, turnaround_times

def priority(processes, burst_times, arrival_times, priorities):
    waiting_times = [0] * len(processes)
    turnaround_times = [0] * len(processes)
    
    ready_queue = []
    current_time = 0
    
    while len(ready_queue) != len(processes):
        
        for i in range(len(processes)):
            if arrival_times[i] <= current_time and i not in ready_queue:
                ready_queue.append(i)
                
        if ready_queue:
            highest = ready_queue[np.argmax(priorities[i] for i in ready_queue)] 
            burst_times[highest] -= 1
            current_time += 1
            
            if burst_times[highest] == 0:
                waiting_times[highest] = current_time - arrival_times[highest]
                turnaround_times[highest] = current_time - arrival_times[highest]
                ready_queue.remove(highest)
                
    return waiting_times, turnaround_times

def rr(processes, burst_times, arrival_times, quantum):
    waiting_times = [0] * len(processes)
    turnaround_times = [0] * len(processes)
    
    ready_queue = []
    current_time = 0
    
    while len(ready_queue) != len(processes):
        
        for i in range(len(processes)):
            if arrival_times[i] <= current_time and i not in ready_queue:
                ready_queue.append(i)
                
        if ready_queue:
            process = ready_queue.pop(0)
            burst_times[process] -= quantum
            current_time += quantum
            
            if burst_times[process] > 0:
                ready_queue.append(process)
            else:
                waiting_times[process] = current_time - arrival_times[process]
                turnaround_times[process] = current_time - arrival_times[process]
                
    return waiting_times, turnaround_times

# Calculate metrics for each algorithm
fcfs_wait, fcfs_turn = fcfs(processes, burst_times)  
sjf_wait, sjf_turn = sjf(processes, burst_times, arrival_times)
priority_wait, priority_turn = priority(processes, burst_times, arrival_times, priorities) 
rr_wait, rr_turn = rr(processes, burst_times, arrival_times, 4)

# Determine most suitable algorithm
algorithms = ["FCFS", "SJF", "Priority", "Round Robin"]
averages = [sum(fcfs_wait)/len(processes), sum(sjf_wait)/len(processes), 
           sum(priority_wait)/len(processes), sum(rr_wait)/len(processes)]
           
most_suitable = algorithms[averages.index(min(averages))]

print("Most suitable algorithm:", most_suitable)
