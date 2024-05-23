#!/usr/bin/python3
"""
So, python script exports data in the JSON format.
"""
import json
import requests


def fetch_user_data():
    """Fetch user information and to-do lists for all employees."""
    # Now the Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # This fetchs the list of all users (employees)
    users = requests.get(url + "users").json()

    # This creates a dictionary containing to-do list
    # information of all employees
    data_to_export = {}
    for user in users:
        user_id = user["id"]
        user_url = url + f"todos?userId={user_id}"
        todo_list = requests.get(user_url).json()

        data_to_export[user_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username"),
            }
            for todo in todo_list
        ]

    return data_to_export


if __name__ == "__main__":
    data_to_export = fetch_user_data()

    # This writes the data to a JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
