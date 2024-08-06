import json
import requests
import csv

def normalize():
    file_path = 'C:/Users/SridharRamachandra/Documents/IBDMedications.csv'
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)

        # Skip the header row
        next(csv_reader)

        # Process each row
        for row in csv_reader:
            if row:
                print(type(row))
                print(row[0])
                # Collect input data from the user
                client_request_id = str(input("Enter value for client_request_id: "))
                threshold = input("Enter value for threshold: ")
                if threshold != "":
                    threshold = float(threshold) # needs to be some number either 0 or something else
                else:
                    threshold = 0.0
                record_id = str(input("Enter value for record_id: "))
                input_term = row[0]
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

                # url
                url = "https://www.eksplexus2.crohnscolitisfoundation.org/precision/normalize"
                response = requests.request("POST", url, headers=headers, data=payload)
                # print(type(response)) #'requests.models.Response'

                if (response.status_code == 200):
                    # print(json.dumps(response.json(), indent=4))
                    json_data = response.json()
                    # print('json_data:', type(json_data)) # 'dict'

                    responses = json_data['requests']
                    # print('responses: ', type(responses)) # 'list'

                    # print(responses)
                    first_response = responses[0]
                    # print('first_response: ', type(first_response))  # 'dict'
                    items = first_response['response']['items']
                    # print('items: ', type(items))  # 'dict'
                    # print(items)
                    for item in items:
                        lexical_title = item['lexical_title']
                        print(f"lexical_title: {lexical_title}")
                        rx_codes = item['metadata']['mappings']['rxnorm']['codes']
                        for rx_code in rx_codes:
                            rxnorm_code = rx_code['rxnorm_code']
                            print(f"rxnorm_code: {rxnorm_code}")
                            rxnorm_titles = rx_code['rxnorm_titles']
                            for rxnorm_title in rxnorm_titles:
                                title =rxnorm_title['title']
                                print(f"title: {title}")
                                title_type = rxnorm_title['title_type']
                                print(f"title_type: {title_type}")
                        ndc_codes = item['metadata']['mappings']['ndc']['codes']
                        cvx_codes = item['metadata']['mappings']['cvx']['codes']
                        print(rx_codes)
                        print(ndc_codes)
                        print(cvx_codes)

                else:
                    # return jsonify({'error': 'Failed to fetch data'}), response.status_code
                    print('error')

# run
normalize()