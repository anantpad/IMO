import json

import requests

def normalize():
    # route
    url = "https://www.eksplexus2.crohnscolitisfoundation.org/precision/normalize"

    # Collect input data from the user
    client_request_id = str(input("Enter value for client_request_id: "))
    threshold = input("Enter value for threshold: ")
    if threshold != "":
        threshold = float(threshold) # needs to be some number either 0 or something else
    else:
        threshold = 0.0
    match_field_pref = str(input("Enter value for match_field_pref: ")) # needs to have something!
    record_id = str(input("Enter value for record_id: "))
    input_term = str(input("Enter value for input_term: "))
    input_code = str(input("Enter value for input_code: "))
    input_code_system = str(input("Enter value for input_code_system: "))

    payload = json.dumps({
      "client_request_id": client_request_id,
      "preferences": {
        "threshold": threshold,
        "match_field_pref": match_field_pref
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
        return response.json()
    else:
        # return jsonify({'error': 'Failed to fetch data'}), response.status_code
        print('error')

# {
# "client_request_id": "2",
#  "preferences": {
#   "threshold": 0.98,
#   "match_field_pref": "input_term"
#  },
#  "requests": [
#     {
#       "record_id": "10002",
#       "domain": "Medication",
#       "input_term": "adalimumab (inpatient special supply) 40 mg/0.8ml sq kit",
#       "input_code": "",
#       "input_code_system": ""
#     }
#   ]
# }

# run
print(normalize())

'''
1. you need create main function
2. In this main function, call function1.
3. Inside function1:
    headers = {
        'Authorization' = 'Bearer your_access_token',
        'Content-Type' = 'application/json'
    }
    parameters: input_term, input_code, input_code_sys
    payload = jsonify using json.dumps
    response = requests.post(url, json = payload, headers = headers)
    if (successful){
        data = response.json()
    }
    print(data)
    parse and read data into fields
'''



# import requests
# import json
#
# url = "https://www.eksplexus2.crohnscolitisfoundation.org/precision/normalize"
#
# payload = json.dumps({
#   "client_request_id": "2",
#   "preferences": {
#     "threshold": 0.3,
#     "match_field_pref": "input_term"
#   },
#   "requests": [
#     {
#       "record_id": "10002",
#       "domain": "Lab",
#       "input_term": "HEMATOCRIT",
#       "input_code": "",
#       "input_code_system": ""
#     }
#   ]
# })
# headers = {
#   'Content-Type': 'application/json'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.text)