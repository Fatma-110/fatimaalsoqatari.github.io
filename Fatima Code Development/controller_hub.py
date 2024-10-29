# controller_hub.py

class ControllerHub:
    def __init__(self, server_nodes):
        self.server_nodes = server_nodes
        self.current_server_index = 0

    def load_balance(self, request):
        """
        Simulates load balancing by distributing requests among server nodes.

        Parameters:
        - request (str): The request to be processed by the distributed system.

        Returns:
        - str: The response received from the selected server node.
        """
        if not self.server_nodes:
            return "No available servers to handle the request"

        selected_server = self.server_nodes[self.current_server_index]
        self.current_server_index = (self.current_server_index + 1) % len(self.server_nodes)

        return selected_server.process_request(request)

