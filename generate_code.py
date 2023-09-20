import os
import csv
import sys
from contexts import ModelContext, ProblemContext, RunContext
from querier import HumanQuerier, OpenAIQuerier
    
def handle_problem(problemContext, querier, solutions_per_problem):
    for runContext in problemContext.GetRunContexts(solutions_per_problem):
        prompts = problemContext.prompts()
        # print(prompts)
        
        for type, content in prompts.items():
            outputPath = os.path.join(runContext.generatedPath(), type + ".py")
            if not os.path.exists(outputPath):
                print(f"Prompting for problem {problemContext.problemName()} with prompt type {type}")
            
                response = querier.performQuery(content)
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
    model_name = sys.argv[2]
    querier_type = sys.argv[3]
    solutions_per_problem = int(sys.argv[4])
    
    if querier_type == "human":
        querier = HumanQuerier()
    elif querier_type == "openai":
        querier = OpenAIQuerier(model_name)
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
