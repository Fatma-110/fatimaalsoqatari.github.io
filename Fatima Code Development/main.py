#main.py
device1 = SimulatedDevice(device_id=1)
device2 = SimulatedDevice(device_id=2)

request1 = "Sample Request 1"
response1 = device1.send_request(request1)
print(response1)

request2 = "Sample Request 2"
response2 = device2.send_request(request2)
print(response2)


from simulated_device import SimulatedDevice
from controller_hub import ControllerHub
from server_node import ServerNode

# Create simulated devices, a controller/hub, and server nodes
device1 = SimulatedDevice(device_id=1)
device2 = SimulatedDevice(device_id=2)
server1 = ServerNode(server_id=1)
server2 = ServerNode(server_id=2)
server3 = ServerNode(server_id=3)
controller = ControllerHub(server_nodes=[server1, server2, server3])

# Simulate requests from devices and load balancing
request1 = "Sample Request 1"
response1 = controller.load_balance(request1)
print(response1)

request2 = "Sample Request 2"
response2 = controller.load_balance(request2)
print(response2)

# Example usage in main.py
from simulated_device import SimulatedDevice
from controller_hub import ControllerHub
from server_node import ServerNode

# Create simulated devices, a controller/hub, and server nodes
device1 = SimulatedDevice(device_id=1)
device2 = SimulatedDevice(device_id=2)
server1 = ServerNode(server_id=1)
server2 = ServerNode(server_id=2)
server3 = ServerNode(server_id=3)
controller = ControllerHub(server_nodes=[server1, server2, server3])

# Simulate requests from devices, load balancing, and processing by server nodes
request1 = "Sample Request 1"
response1 = controller.load_balance(request1)
print(response1)

request2 = "Sample Request 2"
response2 = controller.load_balance(request2)
print(response2)


