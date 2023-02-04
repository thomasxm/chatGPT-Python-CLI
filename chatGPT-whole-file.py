import openai
import sys

# Replace "YOUR-API" with your OpenAI API key
openai.api_key = "YOUR-API"

# Check if a filename was provided as a command-line argument
if len(sys.argv) < 2:
    print("Error: Please specify a file name.")
    sys.exit()

file_name = sys.argv[1]

# Read the input file
with open(file_name, "r") as file:
    text = file.read()

# Submit the entire text to the OpenAI API for parsing:
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Please parsing this text and give me feedback and suggestion " + text,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the corrected version of the entire text
print(response["choices"][0]["text"])
