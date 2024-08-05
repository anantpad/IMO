import json
import requests
import random

def normalize():
    # url
    url = "https://www.eksplexus2.crohnscolitisfoundation.org/precision/normalize"

    # Collect input data from the user
    client_request_id = str(input("Enter value for client_request_id: "))
    threshold = input("Enter value for threshold: ")
    if threshold != "":
        threshold = float(threshold) # needs to be some number either 0 or something else
    else:
        threshold = 0.0
    record_id = str(input("Enter value for record_id: "))
    input_term = str(input("Enter value for input_term: "))
    input_code = str(input("Enter value for input_code: "))
    input_code_system = str(input("Enter value for input_code_system: "))

    # Transform input data to expected json structure
    payload = json.dumps({
      "client_request_id": client_request_id,
      "preferences": {
        "threshold": threshold,
        "match_field_pref": "input_term"
      },
      "requests": [
        {
          "record_id": record_id,
          "domain": "Medication",
          "input_term": input_term,
          "input_code": input_code,
          "input_code_system": input_code_system
        }
      ]
    })

    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if (response.status_code == 200):
        # print(json.dumps(response.json(), indent=4))
        json_data = response.json()

        responses = json_data['requests']
        first_response = responses[0]
        items = first_response['response']['items']
        for item in items:
            lexical_title = item['lexical_title']
            print(f"lexical_title: {lexical_title}")
    else:
        # return jsonify({'error': 'Failed to fetch data'}), response.status_code
        print('error')

# run
normalize()
