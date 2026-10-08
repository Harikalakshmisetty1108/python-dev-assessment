import requests


def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url)
        response.raise_for_status()
        users = response.json()

        for user in users[:num_users]:
            name = user["name"]
            email = user["email"]
            city = user["address"]["city"]

            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"City: {city}")
            print()

    except requests.exceptions.RequestException as error:
        print(f"Network or HTTP error: {error}")
        return None

    except (KeyError, TypeError, ValueError) as error:
        print(f"Unexpected JSON structure: {error}")
        return None


fetch_and_display_users(3)