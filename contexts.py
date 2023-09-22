import os
import json
import ast
from typing import Dict, Any

class FunctionPrototype:
	def __init__(self, data):
		self.function_name = data["function_name"]
		self.parameters = [Parameter(p) for p in data["parameters"]]
		self.return_values = [ReturnValue(r) for r in data["return_values"]]

	def __str__(self):
		params_str = ", ".join([str(p) for p in self.parameters])
		return_values_str = ", ".join([str(r) for r in self.return_values])
		return f"{self.function_name}({params_str}) -> {return_values_str}"
	
	def get_python_type(self, param_type, input):
		# Based on the type, convert the string representation to the appropriate Python object
		if param_type == "int":
			return int(input)
		elif param_type == "float":
			return float(input)
		elif param_type.startswith("List[int]"):
			# Using ast.literal_eval to safely evaluate the string representation
			return ast.literal_eval(input)
	
	def get_parameter_values(self, test_case: Dict[str, str]) -> Dict[str, Any]:
		converted_params = {}
		
		for param in self.parameters:
			converted_params[param.name] = self.get_python_type(param.type, test_case["parameters"][param.name])
		
		return converted_params
		
		
	def get_return_values(self, test_case: Dict[str, str]) -> Dict[str, Any]:
		converted_retvals = []
		
		expectedOutput = test_case["expected_output"]
		
		for retval, expected in zip(self.return_values, expectedOutput):
			# Extract the type of the parameter
			converted_retvals.append(self.get_python_type(retval.type, expected))
			
		if len(converted_retvals) == 1:
			return converted_retvals[0]
		elif len(converted_retvals) > 1:
			return tuple(converted_retvals)
		else:
			return None	




class Parameter:
	def __init__(self, data):
		self.name = data["name"]
		self.type = data["type"]

	def __str__(self):
		return f"{self.name}: {self.type}"

class ReturnValue:
	def __init__(self, data):
		self.type = data["type"]

	def __str__(self):
		return self.type

class ModelContext:
	def __init__(self, model, rootDirectory):
		self.__model = model
		self.__rootDirectory = rootDirectory

	def __repr__(self):
		return f"ModelContext(Model: {self.__model})"

	def model(self):
		return self.__model

	def __get_path(self, sub_directory, *args):
		path = os.path.join(self.__rootDirectory, sub_directory, *args)
		if not os.path.exists(path):
			os.makedirs(path)
		return path

	def problemPath(self):
		return self.__get_path('problems')

	def generatedPath(self):
		return self.__get_path('generated', self.__model)

	@classmethod
	def ModelContextsForDirectory(cls, rootDirectory):
		modelContexts = []
		
		generatedPath = os.path.join(rootDirectory, 'generated')
		if os.path.exists(generatedPath):
			for model in os.listdir(generatedPath):
				if os.path.isdir(os.path.join(generatedPath, model)):
					modelContext = cls(model, rootDirectory)
					modelContexts.append(modelContext)
		return modelContexts

	def GetProblemContexts(self):
		problem_contexts = []
		
		def is_numeric(n):
			try:
				int(n)
				return True
			except ValueError:
				return False
		
		# Filter and sort the problem numbers in ascending order
		problemNumbers = sorted(filter(is_numeric, os.listdir(self.problemPath())), key=lambda x: int(x))
		
		for problemNumber in problemNumbers:
			if os.path.isdir(os.path.join(self.problemPath(), problemNumber)):
				problemContext = ProblemContext(self.__model, problemNumber, self.__rootDirectory)
				problem_contexts.append(problemContext)
		
		return problem_contexts

class ProblemContext:
	def __init__(self, model, problemNumber, rootDirectory):
		self.__model = model
		self.__problemNumber = problemNumber
		self.__rootDirectory = rootDirectory

	def __repr__(self):
		return f"ProblemContext(Model: {self.__model}, Problem: {self.__problemNumber})"
	
	def model(self):
		return self.__model
	
	def problemNumber(self):
		return self.__problemNumber

	def __get_path(self, sub_directory, *args):
		path = os.path.join(self.__rootDirectory, sub_directory, *args)
		if not os.path.exists(path):
			os.makedirs(path)
		return path

	def problemPath(self):
		return self.__get_path('problems', self.__problemNumber)
	
	def generatedPath(self):
		return self.__get_path('generated', self.__model, self.__problemNumber)	
		
	def __problemJSONPath(self):
		return os.path.join(self.problemPath(), "problem.json")
	
	def __problemJSON(self):
		with open(self.__problemJSONPath(), 'r') as f:
			return json.load(f)
	
	def prompts(self):
		return {item['type']: item['content'] for item in self.__problemJSON()['prompts']}			
			
	def category(self):
		return self.__problemJSON()['category']
		
	def problemName(self):
		return self.__problemJSON()['problem_id']
		
	def testCases(self):
		return self.__problemJSON()['test_cases']

	def functionPrototype(self):
		return FunctionPrototype(self.__problemJSON()['function_prototype'])
	
	@classmethod
	def ProblemContextsForDirectory(cls, rootDirectory):
		problemsData = []
		generatedPath = os.path.join(rootDirectory, 'generated')
		for model in os.listdir(generatedPath):
			for problemNumber in os.listdir(os.path.join(generatedPath, model)):
				problemContext = cls(model, problemNumber, rootDirectory)
				problemsData.append(problemContext)
		return problemsData
					
	def GetExistingRunContexts(self):
		run_contexts = []
		
		# Assuming the structure is: generatedPath/model/problemNumber/runNumber
		
		def is_numeric(n):
			try:
				int(n)
				return True
			except ValueError:
				return False
		
		# Filter and sort the run numbers in ascending order
		runNumbers = sorted(filter(is_numeric, os.listdir(self.generatedPath())), key=lambda x: int(x))
		
		for runNumber in runNumbers:
			if os.path.isdir(os.path.join(self.generatedPath(), runNumber)):
				run_context = RunContext(self.__model, self.problemNumber(), runNumber, self.__rootDirectory)
				run_contexts.append(run_context)
				
		return run_contexts
		
	def GetRunContexts(self, runCount):
		run_contexts = []
		
		# Assuming the structure is: generatedPath/model/problemNumber/runNumber
		for runNumber in range(1, runCount+1):
			# Construct paths for problem, generated, profiling and visualization
			run_number = f"{runNumber:02}"
			run_context = RunContext(self.__model, self.problemNumber(), run_number, self.__rootDirectory)
			run_contexts.append(run_context)
				
		return run_contexts

class RunContext:
	def __init__(self, model, problemNumber, runNumber, rootDirectory):
		self.__model = model
		self.__problemNumber = problemNumber
		self.__runNumber = runNumber
		self.__rootDirectory = rootDirectory

	def __repr__(self):
		return f"RunContext(Model: {self.__model}, Problem: {self.__problemNumber}, Run: {self.__runNumber})"
	
	def model(self):
		return self.__model
	
	def problemNumber(self):
		return self.__problemNumber

	def runNumber(self):
		return self.__runNumber
		
	def __get_path(self, sub_directory, *args):
		path = os.path.join(self.__rootDirectory, sub_directory, *args)
		if not os.path.exists(path):
			os.makedirs(path)
		return path

	def generatedPath(self):
		return self.__get_path('generated', self.__model, self.__problemNumber, self.__runNumber)	

	@classmethod
	def RunContextsForDirectory(cls, rootDirectory):
		runsData = []

		# Start by iterating through the 'generated' directory
		generatedPath = os.path.join(rootDirectory, 'generated')
		for model in os.listdir(generatedPath):
			for problemNumber in os.listdir(os.path.join(generatedPath, model)):
				for runNumber in os.listdir(os.path.join(generatedPath, model, problemNumber)):
					
					# Construct paths for problem, generated, profiling and visualization
					problemPath = os.path.join(rootDirectory, 'problems', problemNumber)
					generatedRunPath = os.path.join(generatedPath, model, problemNumber, runNumber)
					profilingRunPath = os.path.join(rootDirectory, 'profiling', model, problemNumber, runNumber)
					visualizationRunPath = os.path.join(rootDirectory, 'visualization', model, problemNumber, runNumber)
					
					runContext = cls(model, problemNumber, runNumber, problemPath, generatedRunPath, profilingRunPath, visualizationRunPath)
					runsData.append(runContext)
					
		return runsData
		
	def createProblemContext(self):
		# Remove the run number from the paths
		generatedPath = os.path.join(os.path.dirname(os.path.dirname(self.__generatedPath)))
		profilingPath = os.path.join(os.path.dirname(os.path.dirname(self.__profilingPath)))
		visualizationPath = os.path.join(os.path.dirname(os.path.dirname(self.__visualizationPath)))
		
		return ProblemContext(
			self.model(),
			self.problemNumber(),
			self.problemPath(),
			generatedPath,
			profilingPath,
			visualizationPath
		)
