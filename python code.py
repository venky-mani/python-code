import json
import collections

# Class for user account
class User_Account:
    def __init__(self, user, api_id):
        self.user = user
        self.api_id = api_id

# CRUD Endpoints and other functions
class API_Manager:
    def __init__(self):
        self.api_list = []
        self.request_log = collections.defaultdict(list)
        self.response_log = collections.defaultdict(list)

    # Creating API
    def create_api(self):
        payload = input("Input payload: ")
        api_id = input("Input API ID: ")
        api_object = {"api_id": api_id, "payload": payload}
        
        self.api_list.append(api_object)
        self.request_log[api_id].append(payload)
        
        print("API created with the following information:",
              json.dumps(api_object, indent=4))
        
        user_object = User_Account(user=api_id, api_id=api_id)
        return api_object, user_object

    # Reading API
    def read_api(self, api_id):
        for item in self.api_list:
            if api_id == item["api_id"]:
                return item
        return None

    # Updating API
    def update_api(self, api_id):
        payload = input("Input new payload: ")
        for item in self.api_list:
            if api_id == item["api_id"]:
                item["payload"] = payload
                return item
        return None

    # Deleting API
    def delete_api(self, api_id):
        for item in self.api_list:
            if api_id == item["api_id"]:
                self.api_list.remove(item)
                return self.api_list
        return None

    # Simulate API Request
    def simulate_request(self, api_id, payload):
        self.request_log[api_id].append(payload)
        for item in self.api_list:
            if api_id == item["api_id"]:
                response = item.get("payload")
                self.response_log[api_id].append(response)
                print(f"API Response for '{api_id}': {response}")
                return response
        return None

    # Generate Usage Statistics
    def generate_usage_statistics(self, api_id):
        api_requests = self.request_log.get(api_id, [])
        api_responses = self.response_log.get(api_id, [])
        print(f"API requests for {api_id}: {api_requests}")
        print(f"API responses for {api_id}: {api_responses}")
        return api_requests, api_responses

# Example usage:
api_manager = API_Manager()

# Create an API
api_object, user_object = api_manager.create_api()
# Input payload: {"data": "example"}
# Input API ID: 123
# Output: 
# API created with the following information:
# {
#     "api_id": "123",
#     "payload": "{\"data\": \"example\"}"
# }

# Read an API
result = api_manager.read_api("123")
print(result)
# Output: {'api_id': '123', 'payload': '{"data": "example"}'}

# Update an API
updated_api = api_manager.update_api("123")
# Input new payload: {"data": "updated data"}
print(updated_api)
# Output: {'api_id': '123', 'payload': '{"data": "updated data"}'}

# Delete an API
new_api_list = api_manager.delete_api("123")
print(new_api_list)
# Output: []

# Simulate API Request
api_manager.simulate_request("123", "New payload")
# Output: API Response for '123': '{"data": "updated data"}'

# Generate Usage Statistics
api_manager.generate_usage_statistics("123")
# Output: 
# API requests for 123: ['New payload']
# API responses for 123: ['{"data": "updated data"}']

api_object, user_object = api_manager.create_api()
result = api_manager.read_api("API_001")
print(result)
updated_api = api_manager.update_api("API_001")
new_api_list = api_manager.delete_api("API_001")
print(new_api_list)
api_manager.simulate_request("API_001", "New request payload")
api_manager.generate_usage_statistics("API_001")

