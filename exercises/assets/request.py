import urllib.request
import urllib.error

import json 


data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["status_checking", "loan_duration", "credit_history", "purpose", 
                                    "credit_amount", "savings_amt", "emp_years", "percent_disp_income", 
                                    "status_sex", "other_debts", "residence_since", "property", "age", 
                                    "other_installments", "housing_status", "num_credits", "job_type", 
                                    "num_dependant", "own_telephone", "foreign_worker", "credit_risk"],
                    "Values": [ [ "A12","48","A32","A43","5951","A61","A73","2","A92","A101","2",
                                 "A121","22","A143","A152","1","A173","1","A191","A201","2"],
                              [ "A12","48","A32","A43","5951","A61","A73","2","A92","A101","2",
                                 "A121","22","A143","A152","1","A173","1","A191","A201","2"]]
                },        },
            "GlobalParameters": {}
    }

body = str.encode(json.dumps(data))

url = 'YOUR OWN API URL'
# Replace this with the API key for the web service
api_key = 'YOUR_OWN_API_KEY' 
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result) 
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))                 