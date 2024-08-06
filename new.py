
# read from file
# file saved locally
# files structure is pre-specified - must have a column named "drug_name", rest any other column will be ignored

# parse each row from csv
# create data for request parameters
    # "client_request_id": create a sequential number starting with 001,
    # "threshold": accept float values >= 0.0,
    # "match_field_pref": <default value> "input_term"
# for each row in csv start capturing this information
    # "record_id": create a sequential number - concatenate clientrequest id with a sequential number starting with 001,
    # "domain": <default value> "Medication",
    # "input_term": "chest pain",
    # "input_code": <default value> "",
    # "input_code_system": <default value> ""

# create POST request call
# specify url
# url should be specified as a config parameter and not shared on github
# POST https://www.eksplexus2.crohnscolitisfoundation.org/precision/normalize
# Sample request must be formatted like this json
    # Body
    # {
    # "client_request_id": "1",
    #   "preferences": {
    #     "threshold": 0,
    #     "match_field_pref": "input_term"
    #   },
    #   "requests": [
    #     { use data in one row of the csv to populate here
    #       "record_id": "10001",
    #       "domain": "Problem",
    #       "input_term": "chest pain",
    #       "input_code": "R07.9",
    #       "input_code_system": "ICD-10-CM"
    #     },
    #     { use data in second row of csv to populate here, and so on..
    #       "record_id": "10001",
    #       "domain": "Problem",
    #       "input_term": "chest pain",
    #       "input_code": "R07.9",
    #       "input_code_system": "ICD-10-CM"
    #     }
    #   ]
    # }
# define headers for the request
    # headers = {
    #     'Content-Type': 'application/json'
    # }

# Make API Call
    # response = requests.request("POST", url, headers=headers, data=payload)

# receive and parse the response into a csv
    # parse the response as a json file
    # one input record can have more than one response, arrange the response in csv form
    # structure it as input term, response 1 on one row and subsequent responses on subsequent rows
    # save csv locally