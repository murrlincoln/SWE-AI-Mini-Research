import json
import openai

# Initialize the OpenAI API client
openai.api_key = "your-openai-api-key-here"

# Read the JSON file containing the problems
with open('all_problems.json', 'r') as f:
    problems = json.load(f)

# Loop through each problem and each type of prompt
for problem in problems:
    problem_id = problem['problem_id']
    for prompt in problem['prompts']:
        prompt_type = prompt['type']
        prompt_content = 'Generate code adhereing to the following prompt: ' +  prompt['content']

        # Send the prompt to the OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt_content,
            max_tokens=100
        )

        # Extract and print the generated code
        generated_code = response.choices[0].text.strip()
        print(f"Generated code for {problem_id}, prompt type {prompt_type}:")
        print(generated_code)
        print('-' * 60)

        # Save or process the generated code as you wish
