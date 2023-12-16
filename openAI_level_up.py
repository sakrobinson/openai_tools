# Load libraries to help with installing dependencies
import subprocess
import sys
import pkg_resources

# List of required packages
required_packages = {'openai', 'requests'}

# Get currently installed dependencies
installed_packages = {pkg.key for pkg in pkg_resources.working_set}

missing_packages = required_packages - installed_packages

# Install needed packages if they are missing =
if missing_packages:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing_packages], stdout=subprocess.DEVNULL)

import openai
import requests

# Set your OpenAI API key
openai.api_key = 'NONE'

# Set your preferred number of characters
num_characters = 33  # Number of characters to generate

# Prompt the user for a different number if the default is detected
if num_characters == 33:
    user_input = input(f"The default number of car characters to generate is {num_characters}. Would you like to change it? (yes/no): ")
    if user_input.lower() == 'yes':
        num_characters = int(input("How many car characters would you like to generate? "))

# Prompt the user for an API key if it's set to 'NONE'
if openai.api_key == 'NONE':
    openai.api_key = input("Please enter your OpenAI API key: ")

def generate_car_character_description():
    # Generate a descriptive sentence
    client = OpenAI()
    response = client.completions.create(engine="text-davinci-003",
      prompt="Give me a random descriptive sentence."
    )
    return response.choices[0].text.strip()

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)

def generate_car_character_image(description, i):
    # Generate an image based on the description
    response = openai.Image.create(
        model="dall-e-3",
        prompt=description,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url  # This line should be indented to match the block
    filename = f"random{i}.jpg"
    download_image(image_url, filename)
    return filename

num_characters = 33  # Number of characters to generate

for i in range(num_characters):
    description = generate_car_character_description()
    print(f"Car Character Description {i+1}: {description}")
    filename = generate_car_character_image(description, i+1)
    print(f"Downloaded Image: {filename}")
