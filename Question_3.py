import requests

base_url = "https://petstore3.swagger.io/v3/user"

def create_user(username, email):
    user_data = {
        "id": 0,
        "username": username,
        "email": email,
        # ... other user data ...
    }
    response = requests.post(base_url, json=user_data)
    return response

def read_user(username):
    response = requests.get(f"{base_url}/{username}")
    return response

def update_username(username, new_username):
    updated_data = {
        "username": new_username,
        # ... other updated data ...
    }
    response = requests.put(f"{base_url}/{username}", json=updated_data)
    return response

def delete_user(username):
    response = requests.delete(f"{base_url}/{username}")
    return response

# Test Flow
if __name__ == "__main__":
    try:
        # Create a new user
        create_response = create_user("testuser", "testuser@example.com")
        create_response.raise_for_status()
        print("New user created")

        # Read the created user
        read_response = read_user("testuser")
        read_response.raise_for_status()
        print("Read created user")

        # Update the user's username
        update_response = update_username("testuser", "newtestuser")
        update_response.raise_for_status()
        print("Username updated")

        # Read the updated user
        read_response = read_user("newtestuser")
        read_response.raise_for_status()
        print("Read updated user")

        # Delete the user
        delete_response = delete_user("newtestuser")
        delete_response.raise_for_status()
        print("User deleted")

        # Verify the user is deleted
        verify_response = read_user("newtestuser")
        if verify_response.status_code == 404:
            print("User deletion verified")
        else:
            print("User deletion verification failed")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
