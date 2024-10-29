Distributed System Availability Enhancement Prototype
Overview
This Python prototype investigates the impact of redundancy mechanisms, specifically load balancing and failover protocols, on the availability of a distributed system. The system consists of a simulated device, a controller/hub, and multiple server nodes.

Instructions
Run the Prototype:

Execute main.py to run the prototype and simulate the interactions between the device, controller, and server nodes.
Data Analysis and Experiments:

Refer to the Data Analysis section for details on experiments, data collection, and analysis.
Model Components
Simulated Device:

Represents a user or client interacting with the system.
Sends requests to the controller/hub.
Controller/Hub:

Manages the distribution of requests among server nodes.
Implements load balancing and failover mechanisms.
Server Nodes:

Simulate individual servers in the distributed system.
Process requests and demonstrate failover capabilities.
Experiments
1. Baseline Test
Objective:

Simulate the system without redundancy mechanisms.
Measure availability, response time, and reliability.
Results:

Availability: [Insert Data]
Response Time: [Insert Data]
Reliability: [Insert Data]
2. Load Balancing Test
Objective:

Introduce load balancing mechanisms.
Gradually increase the request load.
Results:

Availability: [Insert Data]
Response Time: [Insert Data]
Reliability: [Insert Data]
3. Failover Test
Objective:

Simulate server failures and observe failover mechanisms.
Results:

Downtime during Failover: [Insert Data]
Impact on User Experience: [Insert Data]
4. Combined Test
Objective:

Integrate load balancing and failover mechanisms.
Assess overall system performance.
Results:

Availability: 
# Analyzing availability
total_uptime = 0
total_downtime = 0

# Simulated data, replace with actual data from experiments
availability_data = [0.95, 0.98, 0.92]

for availability in availability_data:
    total_uptime += availability * experiment_duration
    total_downtime += (1 - availability) * experiment_duration

final_availability = total_uptime / (total_uptime + total_downtime)
print(f"Final System Availability: {final_availability * 100}%")

# Analyzing response time
response_times = [2.5, 3.0, 4.2]  # Replace with actual response time data
average_response_time = sum(response_times) / len(response_times)
print(f"Average Response Time: {average_response_time} seconds")

Response Time:
# Analyzing availability


# Analyzing response time
response_times = [2.5, 3.0, 4.2]  # Replace with actual response time data
average_response_time = sum(response_times) / len(response_times)
print(f"Average Response Time: {average_response_time} seconds")



Reliability:
# Analyzing availability
total_uptime = 0
total_downtime = 0

# Simulated data, replace with actual data from experiments
availability_data = [0.95, 0.98, 0.92]

for availability in availability_data:
    total_uptime += availability * experiment_duration
    total_downtime += (1 - availability) * experiment_duration

final_availability = total_uptime / (total_uptime + total_downtime)
print(f"Final System Availability: {final_availability * 100}%")

# Analyzing response time
response_times = [2.5, 3.0, 4.2]  # Replace with actual response time data
average_response_time = sum(response_times) / len(response_times)
print(f"Average Response Time: {average_response_time} seconds")


Conclusion
This work, from its inception to the experimentation phase, 
has provided a holistic exploration of redundancy mechanisms' 
impact on the availability of distributed systems. 
The findings underscore the importance of thoughtful 
design and implementation of such mechanisms to address the 
challenges inherent in complex, distributed environments. 
As we conclude this exploration, we look forward to future 
research endeavors that build upon these insights, contributing 
to the continual evolution of distributed system architectures.


The code is organized into separate files for each component 
(simulated_device.py, controller_hub.py, server_node.py).