import requests
import json

def register_user(username, password):
    """
    Registers a user via the /register endpoint.

    Args:
        username (str): The username to register.
        password (str): The password for the user.

    Returns:
        requests.Response: The response from the API.
    """
    url = "http://localhost:8000/register"
    user_data = {"username": username, "password": password}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(user_data), headers=headers)
    return response

if __name__ == "__main__":
    # Example usage:
    # Create a new user with a unique username
    new_username = "testuser1"
    new_password = "testpassword"
    
    print(f"Attempting to register user: {new_username}")
    registration_response = register_user(new_username, new_password)

    if registration_response.status_code == 200:
        print("User registered successfully!")
        print("Response:", registration_response.json())
    else:
        print(f"Error registering user. Status code: {registration_response.status_code}")
        try:
            print("Error message:", registration_response.json())
        except json.JSONDecodeError:
            print("Error message:", registration_response.text)