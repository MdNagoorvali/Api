"""Task 1"""
#Task: Create a python project that calls any public REST API and download the response into a file

# Importing requests library
import requests

# Make a GET request to the Dog API to get a list of all breeds
response = requests.get("https://dog.ceo/api/breeds/list/all", timeout=5)

# Check if the request was successful (status code 200)
if response.status_code == 200:

    # Define the file name to save the API response
    FILE_NAME = 'api_response.json'

    # Open the file in binary write mode and write the API response content to it
    with open(FILE_NAME, 'wb') as file:
        file.write(response.content)

    # Print a message indicating that the API response has been saved
    print(f"API response saved to {FILE_NAME}")
else:

    # Print an error message along with the HTTP status code if the request was not successful
    print(f"Error: {response.status_code}")
    