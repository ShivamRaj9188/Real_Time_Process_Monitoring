# Module 3
# Check CPU usage
def cpu_check(cpu):
    if cpu > 80:
        print(f"Alert: CPU usage is critically high at {cpu}%")
    
      
    elif cpu > 60:
        print(f"Notice: CPU usage is moderately high at {cpu}%")
      
    else:
        print(f"Status: CPU usage is normal at {cpu}%")
      

# Check memory usage
def memory_check(mem):
    if mem > 80:
        print(f"Alert: Memory usage is critically high at {mem}%")
      
    elif mem > 50:
        print(f"Notice: Memory usage is moderately high at {mem}%")
      
    else:
        print(f"Status: Memory usage is normal at {mem}%")

# Calculate average of a list
def get_avg(stuff):
    if len(stuff) == 0:
        print("Warning: No data available for averaging.")
        return 0
    total = 0
    for thing in stuff:
        total += thing
    return total / len(stuff)
    
if __name__ == "__main__":
    # Test with dummy values
    cpu = 90
    mem = 85
  
    cpu_check(cpu)
    memory_check(mem)
  
    test_data = [50, 60, 70]
    print(f"Average: {get_avg(test_data):.2f}")
