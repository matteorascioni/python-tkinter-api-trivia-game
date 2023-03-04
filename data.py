import requests

# You can cofigure your endpoint here: https://opentdb.com/api_config.php

# Parameters for the call
parameters = {
    "amount": 10,
    "type": "boolean"
}

# Fetch the data here and handling the response.
response = requests.get(f"https://opentdb.com/api.php?", params=parameters)
response.raise_for_status()
data = response.json()
# Get the list of JSON from the results key.
question_data = data["results"]