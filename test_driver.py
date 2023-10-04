import sys
import os
from contexts import ModelContext, FunctionPrototype
from typing import *
import traceback
import tempfile
import multiprocessing
import json

def add_line_numbers(text):
	lines = text.split("\n")
	numbered_lines = ["{}: {}".format(i+1, line) for i, line in enumerate(lines)]
	return "\n".join(numbered_lines)
	
def executor_script(function_code_file, parameters_file, result_file):
	try:
		# Load the function code
		with open(function_code_file, 'r') as file:
			function_code = file.read()
		
		# Load the parameters
		with open(parameters_file, 'r') as file:
			parameters = json.load(file)
		
		# Add necessary imports
		function_code = f"from typing import *\n\n{function_code}"
		
		# Execute the function code to define the function(s)
		exec_globals = {}
		exec(function_code, exec_globals)
		
		# Get the name of the last defined function
		last_function_name = [name for name in exec_globals if callable(exec_globals[name])][-1]
		function = exec_globals[last_function_name]
		# Call the function with the parameters
		result = function(*parameters)
		
		# Write the result to the result file
		# Write the result to the result file as a dictionary
		with open(result_file, 'w') as file:
			json.dump({'result': result}, file)
	except Exception as e:
		# Write any exception to the result file as a dictionary
		with open(result_file, 'w') as file:
			json.dump({'result': None, 'error': str(e), 'traceback': traceback.format_exc()}, file)
	

def execute_function(function_code, parameters):
	# try:
		# Create temporary files for function_code, parameters, and result
		function_code_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.py')
		parameters_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json')
		result_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json')
		
		# Write function_code and parameters to temporary files
		function_code_file.write(function_code)
		function_code_file.close()  # Close the file to ensure it's written to disk
		
		json.dump(parameters, parameters_file)
		parameters_file.close()  # Close the file to ensure it's written to disk
		
		# Create a separate Python process to run the executor_script
		process = multiprocessing.Process(target=executor_script, args=(function_code_file.name, parameters_file.name, result_file.name))
		process.start()
		process.join()
		
		# Load the result from the result file
		with open(result_file.name, 'r') as file:
			result_data = json.load(file)
		
		# Clean up temporary files
		# os.unlink(function_code_file.name)
		# os.unlink(parameters_file.name)
		# os.unlink(result_file.name)
		
		# Check for an error in the result data
		if 'error' in result_data:
			error_info = {
				"exception": result_data['error'],
				"traceback": result_data['traceback'],
				"parameters": parameters,
				"function_code": function_code
			}
			# print(f"An error occurred: {error_info}")
			# print(add_line_numbers(function_code))
			# input("Press Enter to continue…")

			return error_info
		
		# Return the result
		return result_data['result']
		
	# except Exception as e:
	# 	error_info = {
	# 		"exception": str(e),
	# 		"parameters": parameters,
	# 		"function_code": function_code
	# 	}
	# 	return error_info

def test_solution_run(problemContext, runContext):
	with open('debug.txt', 'a') as f:
		f.write("Inside test_solution_run\n")
	generated_path = runContext.generatedPath()
	function_prototype = problemContext.functionPrototype()
	
	# Dictionary to keep track of test results per solution file
	test_results = {}
	
	for solution_file in os.listdir(generated_path):
		print(f"*****{problemContext.problemName()} - {solution_file}:")
		if os.path.splitext(solution_file)[1] == '.py':
			with open(os.path.join(generated_path, solution_file)) as f:
				solution_code = f.read()
			
			# Initialize counters for this solution file
			tests_passed = 0
			total_tests = 0
			
			for test_case in problemContext.testCases():
				parameters = function_prototype.get_ordered_parameter_values(test_case)
				expected_output = function_prototype.get_return_values(test_case)
				result = execute_function(solution_code, parameters)
				
				total_tests += 1
				if (expected_output == result):
					tests_passed += 1
				else:
					print(f"Parameters: {parameters}")
					print(f"Expected: {expected_output}")
					print(f"Actual: {result}")
					print(add_line_numbers(solution_code))
					# input("Press Enter to continue…")
			
			# Update the test results dictionary for this solution file
			test_results[solution_file] = {
				'tests_passed': tests_passed,
				'total_tests': total_tests
			}

			# write to debug.txt that we're at the end of this
			with open('debug.txt', 'a') as f:
				f.write(f"Tests passed: {tests_passed}/{total_tests}\n")
			
	return test_results


def get_args(arguments):
    args = {}
    for i, arg in enumerate(arguments):
        if arg == "--model" and i+1 < len(arguments):
            args['model'] = arguments[i+1]
    return args

if __name__ == "__main__":
	args = get_args(sys.argv)
	# Check if the user has provided a command-line argument
	if len(sys.argv) < 2:
		print("Please provide correct arguments.")
		sys.exit(1)


		
	folder_path = sys.argv[1]
	model_name = args['model']
	print(f"{folder_path} {model_name}")
	# Dictionary to aggregate test results across all solution files
	aggregate_test_results = {}
	
	if os.path.exists(folder_path):
		modelContext = ModelContext(model_name, folder_path)        
		for problemContext in modelContext.GetProblemContexts():
			for runContext in problemContext.GetExistingRunContexts():
				run_test_results = test_solution_run(problemContext, runContext)
				
				# Merge the test results from this run with the aggregate results
				for solution_file, test_counts in run_test_results.items():
					if solution_file in aggregate_test_results:
						aggregate_test_results[solution_file]['tests_passed'] += test_counts['tests_passed']
						aggregate_test_results[solution_file]['total_tests'] += test_counts['total_tests']
						with open('debug.txt', 'a') as f:
							f.write(f"Tests passed for {problemContext}: {aggregate_test_results[solution_file]['tests_passed']}/{aggregate_test_results[solution_file]['total_tests']}\n")
					else:
						aggregate_test_results[solution_file] = test_counts.copy()
	else:
		with open('debug.txt', 'a') as f:
			f.write("The provided folder path does not exist.\n")
	
	with open('debug.txt', 'a') as f:
		f.write("Finished testing all solution files.\n")
	# Print the final score for each solution file
	tests_passed = 0
	total_tests = 0
	for solution_file, test_counts in aggregate_test_results.items():
		print(f"{solution_file}: {test_counts['tests_passed']}/{test_counts['total_tests']}")
		tests_passed += test_counts['tests_passed']
		total_tests += test_counts['total_tests']
	with open('debug.txt', 'a') as f:
		f.write(f"Overall: {tests_passed}/{total_tests}\n")
	print(f"Overall: {tests_passed}/{total_tests}")

	# CODE FOR COMPATABILITY WITH DAVID/NISALA/LINCOLN AUTOMATED GRADER/FRAMEWORK
	# Might want to move it to a separate file where the framework can specify the model name and folder path
	# Calculate the decimal value
	if total_tests == 0:  # To avoid division by zero
		decimal_value = 0
	else:
		decimal_value = tests_passed / total_tests

	# Write the decimal value to output.json
	with open('output.json', 'w') as outfile:
		json.dump({'output': decimal_value * 100}, outfile)
