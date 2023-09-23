import sys
import os
from contexts import ModelContext, FunctionPrototype
from typing import *

def add_line_numbers(text):
	lines = text.split("\n")
	numbered_lines = ["{}: {}".format(i+1, line) for i, line in enumerate(lines)]
	return "\n".join(numbered_lines)

def execute_function(function_code, parameters):
	"""
	Executes the provided function code with parameters from the test case and checks if the return value is correct.
	
	Parameters:
	- function_code: The Python code for the function to be executed.
	- test_case: A dictionary containing the parameters and expected output for a test case.
	
	Returns:
	- True if the function's output matches the expected output, otherwise False.
	"""
	
	try:
		# Dynamically define and execute the function
		exec(function_code)
		
		# Get function name from the code (assuming the function name is the word after "def")
		function_name = function_code.split("def")[1].split("(")[0].strip()
		
		# Call the function using extracted parameters
		return eval(f"{function_name}(**parameters)")
		
		return result
	except Exception as e:
		print(f"An exception occurred: {e}")
		print(f"Type: {type(e)}")
		print(f"Args: {e.args}")

def test_solution_run(problemContext, runContext):
	generated_path = runContext.generatedPath()
	function_prototype = problemContext.functionPrototype()
	
	tests_passed = 0
	total_tests = 0
	
	for solution_file in os.listdir(generated_path):
		# print(f"***** {solution_file}:")
		if os.path.splitext(solution_file)[1] == '.py':
			with open(os.path.join(generated_path, solution_file)) as f:
				solution_code = f.read()
			print(add_line_numbers(solution_code))
			for test_case in problemContext.testCases():
				parameters = function_prototype.get_parameter_values(test_case)
				expected_output = function_prototype.get_return_values(test_case)
				result = execute_function(solution_code, parameters)
				
				# print(f"Parameters: {parameters}")
				# print(f"Expected: {expected_output}")
				# print(f"Actual: {result}")
				
				total_tests += 1
				if (expected_output == result):
					tests_passed += 1
					
	return tests_passed, total_tests

if __name__ == "__main__":
	# Check if the user has provided a command-line argument
	if len(sys.argv) < 3:
		print("Please provide correct arguments.")
		sys.exit(1)
		
	folder_path = sys.argv[1]
	model_name = sys.argv[2]
	
	tests_passed = 0
	total_tests = 0
	
	# Check if the given folder path exists
	if os.path.exists(folder_path):
		modelContext = ModelContext(model_name, folder_path)        
		for problemContext in modelContext.GetProblemContexts():
			for runContext in problemContext.GetExistingRunContexts():
				run_tests_passed, run_total_tests = test_solution_run(problemContext, runContext)
				tests_passed += run_tests_passed
				total_tests += run_total_tests
	else:
		print("The provided folder path does not exist.")
		
	print(f"Final score: {tests_passed}/{total_tests}")
