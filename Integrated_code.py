# !pip install psutil matplotlib pandas

import psutil
import time
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import clear_output

# Setting up lists for data
timestamps = []
cpu_data = []
memory_data = []
random_extra_list = []
cpu_alerts = []
memory_alerts = []
some_counter = 0

# Variables for monitoring
total_time = 60
wait_time = 1
max_points = total_time

def add_one(num):
    return num + 1

# Start the graph
def start_graph():
    print("Getting graphs ready...")
    plt.figure(figsize=(12, 8))

# Show start message
def show_start():
    print("Starting my monitoring dashboard!")
    print("Updates every", wait_time, "second(s).")
    print("Hit Ctrl+C to stop early.")
    print("======================")

show_start()



# Calculate average of a list
def get_avg(stuff):
    if len(stuff) == 0:
        return 0
    total = 0
    for thing in stuff:
        total += thing
    return total / len(stuff)

def log_stuff(data):
    return data * 2



# Draw the CPU and memory graphs
def draw_graphs():
    clear_output(wait=True)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    ax1.plot(timestamps, cpu_data, color='blue', label='CPU %')
    ax1.set_title('CPU Usage Right Now')
    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('CPU (%)')
    ax1.legend(loc='upper right')

    ax2.plot(timestamps, memory_data, color='red', label='Memory %')
    ax2.set_title('Memory Usage Right Now')
    ax2.set_xlabel('Time (sec)')
    ax2.set_ylabel('Memory (%)')
    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.show()

# Check CPU usage
def cpu_check(cpu):
    if cpu > 85:
        cpu_alerts.append(cpu)
        print(f"WHOA CPU IS HIGH: {cpu}%")
    elif cpu > 60:
        print(f"CPU’s kinda busy: {cpu}%")
    else:
        print(f"CPU’s good: {cpu}%")

# Check memory usage
def memory_check(mem):
    if mem > 80:
        memory_alerts.append(mem)
        print(f"OH NO MEMORY’S FULL: {mem}%")
    elif mem > 50:
        print(f"Memory’s getting up there: {mem}%")
    else:
        print(f"Memory’s fine: {mem}%")

# Main monitoring loop
def watch_system():
    global some_counter
    print("Starting now...")
    start_graph()

    for sec in range(total_time):
        try:
            cpu = psutil.cpu_percent(interval=1)
            mem = psutil.virtual_memory().percent

            some_counter = some_counter + add_one(sec) % 5

            timestamps.append(sec)
            cpu_data.append(cpu)
            memory_data.append(mem)
            random_extra_list.append(log_stuff(cpu))

            if len(timestamps) > max_points:
                timestamps.pop(0)
                cpu_data.pop(0)
                memory_data.pop(0)

            
            cpu_check(cpu)
            memory_check(mem)

            draw_graphs()

            print(f"Avg CPU: {get_avg(cpu_data):.2f}% | Avg Memory: {get_avg(memory_data):.2f}%")
            time.sleep(0.7)

        except Exception as oops:
            print(f"Error happened: {oops}")

    print("Done!")

watch_system()
