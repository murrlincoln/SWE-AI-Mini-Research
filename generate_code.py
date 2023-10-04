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
llm = get_llm(args['model'])  # Use the parsed model name

def handle_problem(problemContext, querier, solutions_per_problem):
    for runContext in problemContext.GetRunContexts(solutions_per_problem):
        prompts = problemContext.prompts()
        # print(prompts)
        
        for type, content in prompts.items():
            outputPath = os.path.join(runContext.generatedPath(), type + ".py")
            if not os.path.exists(outputPath):
                print(f"Prompting for problem {problemContext.problemName()} with prompt type {type}")
                
                functionPrototype = problemContext.functionPrototype()
                if "generic" in type:
                    functionPrototype = functionPrototype.genericize()
                
                instructions = f"Generate a Python function adhering to the following prompt: {content}\n\nUse the following prototype: {functionPrototype}\n\nProvide only the function asked for. If you need to use helper functions, they should be defined before the function. Do not include tests or any other information. Your response will be directly executed and tested."
            
                response = querier.performQuery(instructions)
                print('-' * 60)
                print(response)
                print('-' * 60)
                
                with open(outputPath, 'w') as f:
                    f.write(response)
            

if __name__ == "__main__":
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
        # todo: switch this to the LLM model compatible with the framework
        querier = OpenAIQuerier(llm)
    else:
        print(f"Querier type {querier_type} unknown.")
        sys.exit(1)
    
    # Check if the given folder path exists
    if os.path.exists(folder_path):
        modelContext = ModelContext(model_name, folder_path)        
        for problemContext in modelContext.GetProblemContexts():
            handle_problem(problemContext, querier, solutions_per_problem)
    else:
        print("The provided folder path does not exist.")
