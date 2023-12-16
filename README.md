# openai_tools
misc tools for openai api


---

# Character Generator

This script generates random descriptive sentences for characters and then creates corresponding images using OpenAI's DALL-E model. It's designed to be a fun and creative tool for generating unique character concepts... or to level up your openai api key!

## Prerequisites

Before you run the script, make sure you have the following prerequisites installed:

- Python 3.x
- `openai` Python package
- `requests` Python package

You can install the required packages using pip:

```bash
pip install openai requests
```

## Setup

1. Obtain an API key from OpenAI by signing up on their platform and accessing your account settings.
2. Clone this repository or download the script to your local machine.

## Usage

1. Run the script using Python:

```bash
python openAI_level_up.py
```

2. When prompted, enter your OpenAI API key. If you do not wish to be prompted each time, you can directly set your API key in the script by replacing `'NONE'` with your actual API key:

```python
openai.api_key = 'your-api-key-here'
```

3. The script will also prompt you to enter the number of car characters you wish to generate. The default is set to 33, but you can choose any number you prefer when prompted.

4. The script will generate a descriptive sentence for each car character and then create an image based on that description. The images will be downloaded to the same directory as the script.

## Output

The generated descriptions and images will be printed and saved with filenames in the format `random<i>.jpg`, where `<i>` is the index number of the character.

## Notes

- Each API call to OpenAI may incur costs, so be aware of your usage and the associated fees.
- The quality and creativity of the generated content may vary.

## License

This script is provided "as is", without warranty of any kind. Use at your own risk.

---
