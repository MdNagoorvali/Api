#Task: Create a python project that calls any public REST API and download the response into a file 

# Importing requests library
import requests

# Make a GET request to the Dog API to get a list of all breeds
response = requests.get("https://dog.ceo/api/breeds/list/all")  

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Define the file name to save the API response
    file_name = 'api_response.json'

    # Open the file in binary write mode and write the API response content to it
    with open(file_name, 'wb') as file:
        file.write(response.content)

    # Print a message indicating that the API response has been saved
    print(f"API response saved to {file_name}")
else:
    # Print an error message along with the HTTP status code if the request was not successful
    print(f"Error: {response.status_code}")

#uploaded to github