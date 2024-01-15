import requests
from bs4 import BeautifulSoup

# Replace 'your_url' with the actual URL you want to connect to
url = 'https://www.one.co.il'

try:
# Send a GET request to the URL
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(e)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Specify the encoding if needed (for example, 'utf-8' or 'windows-1255' for Hebrew)
    response.encoding = 'utf-8'  # Change the encoding according to your needs

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

     # Replace 'your_hebrew_word' with the specific Hebrew word you want to find
    target_word = 'כדור'

     # Find all occurrences of the target word in the text
    occurrences = soup.text.count(target_word)

    # Print the number of occurrences
    print(f'The word "{target_word}" appears {occurrences} times.')
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")