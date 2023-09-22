
import json
import os
import sys

def process_problems(json_file_path, output_dir_path):
    # Load the JSON content from the provided file path
    with open(json_file_path, "r") as file:
        problems_data = json.load(file)

    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)

    # Create individual prettified problem JSON files using 'id' key for directory, removing 'model' and 'id' keys
    for problem in problems_data['problem_set']:
        problem_id = problem['id']
        
        # Remove 'model' and 'id' keys
        problem.pop('model', None)
        problem.pop('id', None)
        
        problem_dir = os.path.join(output_dir_path, problem_id)
        os.makedirs(problem_dir, exist_ok=True)
        problem_file_path = os.path.join(problem_dir, "problem.json")
        with open(problem_file_path, 'w') as problem_file:
            json.dump(problem, problem_file, indent=4, sort_keys=True)

if __name__ == "__main__":
    # Check if the user has provided a command-line argument
    if len(sys.argv) < 3:
        print("Please provide correct arguments.")
        sys.exit(1)
        
    json_file_path = sys.argv[1]
    output_dir_path = sys.argv[2]
        
    process_problems(json_file_path, output_dir_path)
