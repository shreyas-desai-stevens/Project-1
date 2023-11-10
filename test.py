import os
import subprocess
import sys
from pathlib import Path

test_directory = "test"

test_files = [filename for filename in os.listdir(test_directory) if filename.endswith(".in")]

def run_test(program, input_file):
    input_path = os.path.join(test_directory, input_file)
    # input_path = Path(input_path)
    # print(Path(input_path) )
    expected_output_path = os.path.join(test_directory, input_file.replace(".in", ".out"))
    # print(expected_output_path)
    expected_error_path = os.path.join(test_directory, input_file.replace(".in", ".err"))
    # print(expected_error_path)

    try:
        if 'stdin' in input_path:
                print(f"File: {input_path}")
                cmd = f"python prog/{program} < {input_path}"
        else:
                print(f"File: {input_path}")
                cmd = f"python prog/{program} {input_path}"

        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        if result.stderr:
            try:
                with open(expected_error_path, "r") as expected_error:
                    expected_result = expected_error.read()
                    # print(expected_result)   
                    if result.stderr.strip() == expected_result.strip():
                        return "PASS", None, 0, expected_result
                    else:
                        return "FAIL",f"Output Mismatch!\nGot:\n{result.stdout}", 1, expected_result
            except FileNotFoundError:
                return "FAIL", f"File not found!\n{expected_error_path}", 1, ''

        if result.stdout and not result.stderr:        
            try:
                with open(expected_output_path, "r") as expected_output:
                    print("No eror")
                    expected_result = expected_output.read()
                    if result.stdout.strip() == expected_result.strip():
                        return "PASS", None, result.returncode, expected_result
                    else:
                        return "FAIL", f"Output Mismatch!\nGot:\n{result.stdout}", 1, expected_result
            except FileNotFoundError:
                print("Error")
                return "FAIL", f"File Not Found!\n{expected_output_path}", 1, ''


    except Exception as e:
        return "ERROR", str(e)

def main():
    programs = ["wc.py","gron.py"]  
    errors = {"PASSED":0,"FAILED":0}
    total = 0
    print(test_files)
    for test_file in test_files:
        if test_file.startswith('wc'):
            program = "wc.py"
        if test_file.startswith('gron'):
            program = "gron.py"    
        status, error_message,exit_code,expected_result = run_test(program, test_file)
        if exit_code>0:
            errors['FAILED'] += 1
            total+=1
        else:
            errors['PASSED'] += 1
            total+=1
        print(f"{status} \n\tTest case: {test_file.split('.')[0]} {test_file.split('.')[1]}\n")
        print(f"\tExit Code:{exit_code}")

        if error_message:
            print(f"Output:\n{error_message.strip()}\n")
            print(f"Expected Output:\n{expected_result.strip()}\n")
        print("-----------------------------------------------------------------")
    print("-----------------------------------------------------------------")
    for i,j in errors.items():
        print(f"{i} : {j}")
    print(f"TOTAL  : {total}")
    if errors['FAILED']>0:
        sys.exit(1)

if __name__ == "__main__":
    main()
