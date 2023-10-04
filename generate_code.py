import os
import csv
import sys
from contexts import ModelContext, ProblemContext, RunContext
from querier import HumanQuerier, OpenAIQuerier
import sys
from llm_test_helpers import get_llm, get_args

# Modify the get_args function to correctly parse the --MODEL argument
def get_args(arguments):
    args = {}
    for i, arg in enumerate(arguments):
        if arg == "--model" and i+1 < len(arguments):
            args['model'] = arguments[i+1]
    return args

args = get_args(sys.argv)
# llm = get_llm(args['model'])  # Use the parsed model name

def handle_problem(problemContext, querier, solutions_per_problem):
    with open('debug.txt', 'a') as f:
        f.write("Inside handle_problem.\n")
    for runContext in problemContext.GetRunContexts(solutions_per_problem):
        prompts = problemContext.prompts()
        
        for type, content in prompts.items():
            outputPath = os.path.join(runContext.generatedPath(), type + ".py")
            
            if not os.path.exists(outputPath):
                print(f"Prompting for problem {problemContext.problemName()} with prompt type {type}")
                
                functionPrototype = problemContext.functionPrototype()
                if "generic" in type:
                    functionPrototype = functionPrototype.genericize()
                
                instructions = f"Generate a Python function adhering to the following prompt: {content}\n\nUse the following prototype: {functionPrototype}\n\nProvide only the function asked for. If you need to use helper functions, they should be defined before the function. Do not include tests or any other information. Your response will be directly executed and tested."
            
                response = querier.performQuery(instructions)
                with open('debug.txt', 'a') as f:
                    f.write(response + "\n")
                print('-' * 60)
                print(response)
                print('-' * 60)
                
                with open(outputPath, 'w') as f:
                    f.write(response)
            

if __name__ == "__main__":
    with open('debug.txt', 'a') as f:
        f.write("Inside main.\n")
    # Check if the user has provided a command-line argument
    if len(sys.argv) < 5:
        print("Please provide correct arguments.")
        sys.exit(1)
        
    folder_path = sys.argv[1]
    querier_type = sys.argv[2]
    solutions_per_problem = int(sys.argv[3])
    
    if querier_type == "human":
        querier = HumanQuerier()
    elif querier_type == "openai":
        querier = OpenAIQuerier(args['model'])
    else:
        print(f"Querier type {querier_type} unknown.")
        sys.exit(1)
    with open('debug.txt', 'a') as f:
        f.write("Upto if os.path.exists .\n")
    
    # Check if the given folder path exists
    if os.path.exists(folder_path):
        try:
            modelContext = ModelContext(args['model'], folder_path)
        except Exception as e:
            with open('debug.txt', 'a') as f:
                f.write(f"Error initializing ModelContext: {str(e)}\n")

        modelContext = ModelContext(args['model'], folder_path)       
        for problemContext in modelContext.GetProblemContexts():
            handle_problem(problemContext, querier, solutions_per_problem)
    else:
        with open('debug.txt','a') as f:
            f.write("The following folder path does not exist: " + folder_path + "\n")
