#!/usr/bin/python3
"""Here we export the data in the JSON format.."""

import json
import requests
import sys


if __name__ == "__main__":
    # Get the employee ID from the command-line argument
    user_id = sys.argv[1]

    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # This fetchs user information using the provided employee ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # We fetch the to-do list for the employee using the provided employee ID
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params).json()

    # This creates a dictionary containing the user and to-do list information
    data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    # We write the data to a JSON file with the employee ID as the filename
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4) 
