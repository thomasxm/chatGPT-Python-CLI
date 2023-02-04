import openai
import sys

# Replace "YOUR-API" with your OpenAI API key, apply it through OpenAI website.
openai.api_key = "YOUR-API"

# Read the input file
# Check if a filename was provided as a command-line argument
if len(sys.argv) < 2:
    print("Error: Please specify a file name.")
    sys.exit()

file_name = sys.argv[1]

with open(file_name, "r") as file:
    lines = file.readlines()

# Submit each line to the OpenAI API for parsing
for line in lines:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Please give me feedback:" + line,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

# Print the corrected version of each line
print(response["choices"][0]["text"])
