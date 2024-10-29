# simulated_device.py

class SimulatedDevice:
    def __init__(self, device_id):
        self.device_id = device_id

    def send_request(self, request):
        """
        Simulates sending a request to the controller/hub.

        Parameters:
        - request (str): The request sent by the simulated device.

        Returns:
        - str: The response received from the distributed system.
        """
        print(f"Device {self.device_id} sending request: {request}")
        # In a real system, this is where you would send the request to the controller/hub
        # and receive a response from the distributed system.
        # For the sake of simulation, return a placeholder response.
        return f"Response from Device {self.device_id}: Request '{request}' processed successfully"
