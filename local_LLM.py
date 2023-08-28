import subprocess
import os

def choose_directory(base_path):
    # List all directories
    dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
    for idx, directory in enumerate(dirs, 1):
        print(f"{idx}. {directory}")
    while True:
        try:
            choice = int(input("Choose a directory by number: "))
            if 1 <= choice <= len(dirs):
                return dirs[choice-1]
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Please enter a valid number.")

def choose_model(models_path):
    models = [f for f in os.listdir(models_path) if os.path.isfile(os.path.join(models_path, f))]
    for idx, model in enumerate(models, 1):
        print(f"{idx}. {model}")
    while True:
        try:
            choice = int(input("Choose a model by number: "))
            if 1 <= choice <= len(models):
                return models[choice-1]
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Please enter a valid number.")


def append_error_suppression(cmd):
    choice = input("Do you want to enable system info display? (y/n): ")
    if choice.lower() == 'n':
        cmd.append("2> /dev/null")
    return cmd



def run_llm(sub_directory, model_name):
    base_path = "/Volumes/Tu_1TB_SSD/LlaMA/llama.cpp"
    model_path = os.path.join(base_path, "models", sub_directory, model_name)
    cmd = [
        os.path.join(base_path, 'main'),
        '-m', model_path,
        '-t', '8',
        '-n', '256',
        '-ngl', '1',
        '--color',
        '-i',
        '-r', '"User:"',
        '-f', '/Volumes/Tu_1TB_SSD/LlaMA/llama.cpp/prompts/alpaca.txt'
    ]
    
    cmd = append_error_suppression(cmd)
    cmd_str = ' '.join(cmd)
    print("Executing:", cmd_str)  # Print the constructed command
    subprocess.run(cmd_str, cwd=base_path, shell=True)  # Execute the command with shell=True

    # print the output of the command
    print(subprocess.check_output(cmd, cwd=base_path))
    
    # Execute the command and read its output line by line
    #process=subprocess.Popen(cmd, cwd=base_path, stdout=subprocess.PIPE, text=True)
    #for line in process.stdout:
    #    print(line)
    

if __name__ == "__main__":
    models_base_folder = "/Volumes/Tu_1TB_SSD/LlaMA/llama.cpp/models"
    selected_directory = choose_directory(models_base_folder)
    selected_model_folder = os.path.join(models_base_folder, selected_directory)
    selected_model = choose_model(selected_model_folder)
    if selected_model:
        run_llm(selected_directory, selected_model)

