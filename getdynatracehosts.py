import requests
import csv

url = '*******dynatrace.com/api/v1/oneagents?includeDetails=true'
headers = {
    'accept': 'application/json; charset=utf-8',
    'Authorization': 'Api-Token ***********'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    # Writing JSON data to a CSV file
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([key for key in data])  # Writing JSON keys as the first row
        csv_writer.writerow([value for value in data.values()])  # Writing corresponding values as the second row
    print("CSV file 'output.csv' created successfully!")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
