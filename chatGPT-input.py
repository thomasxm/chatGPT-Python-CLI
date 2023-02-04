import openai
import sys

# Apply the API key
openai.api_key = "API-KEY"

# Define the parameters for the text generation
model_engine = "text-davinci-002"

# Get user input from command line arguments
prompt = " ".join(sys.argv[1:])

# Generate the response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Get the generated text
generated_text = completion.choices[0].text

# Print the generated text
print(generated_text)
