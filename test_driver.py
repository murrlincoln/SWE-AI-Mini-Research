import sys
import os
from contexts import ModelContext

def execute_function(function_code: str, test_case: dict) -> bool:
	"""
	Executes the provided function code with parameters from the test case and checks if the return value is correct.
	
	Parameters:
	- function_code: The Python code for the function to be executed.
	- test_case: A dictionary containing the parameters and expected output for a test case.
	
	Returns:
	- True if the function's output matches the expected output, otherwise False.
	"""
	# Dynamically define and execute the function
	exec(function_code)
	
	# Get function name from the code (assuming the function name is the word after "def")
	function_name = function_code.split("def")[1].split("(")[0].strip()
	
	# Extract parameters from the test case
	parameters = eval(test_case['parameters'])
	
	# Call the function using extracted parameters
	result = eval(f"{function_name}(**parameters)")
	
	# Check if the result matches the expected output
	expected_output = eval(test_case['expected_output'])
	
	return result == expected_output

if __name__ == "__main__":
	# Check if the user has provided a command-line argument
	if len(sys.argv) < 3:
		print("Please provide correct arguments.")
		sys.exit(1)
		
	folder_path = sys.argv[1]
	model_name = sys.argv[2]	
	
	# Check if the given folder path exists
	if os.path.exists(folder_path):
		modelContext = ModelContext(model_name, folder_path)        
		for problemContext in modelContext.GetProblemContexts():
			for runContext in problemContext.GetExistingRunContexts():
				generated_path = runContext.generatedPath()
				for solution_file in os.listdir(generated_path):
					print(solution_file)
					if os.path.splitext(solution_file)[1] == '.py':
						with open(os.path.join(generated_path, solution_file)) as f:
							solution_code = f.read()
						print(solution_code)
						for test_case in problemContext.testCases():
							execute_function(solution_code, test_case)
	else:
		print("The provided folder path does not exist.")
