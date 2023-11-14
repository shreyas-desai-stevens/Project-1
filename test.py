import os
import subprocess
import sys
from pathlib import Path

test_directory = "test"

test_files = [filename for filename in os.listdir(test_directory) if filename.endswith(".in")]

def run_test(program, input_file, run_type, flags):
    input_path = os.path.join(test_directory, input_file)
    expected_output_path = os.path.join(test_directory, input_file.replace(".in", f"{flags}.out"))
    if run_type=='stdin':
        expected_output_path = expected_output_path.replace('.out','.stdin.out')
    expected_error_path = os.path.join(test_directory, input_file.replace(".in", ".err"))

    try:
        print(f"File    : {input_path}")

        if run_type == "stdin":
            cmd = f"python prog/{program} {flags} < {input_path}"
        else:
            cmd = f"python prog/{program} {Path(input_path).as_posix()} {flags}"

        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        print("COMMAND :",result.args)
        # print(result.stderr)
        if result.stderr:
            print("Output  :",expected_error_path)
            try:
                with open(expected_error_path, "r") as expected_error:
                    expected_result = expected_error.read()   
                    if result.stderr == expected_result:
                        return "PASS", None, 0, expected_result
                    else:
                        return "FAIL", f"Output Mismatch!\nGot:\n{result.stderr}", 1, expected_result
            except FileNotFoundError:
                return "FAIL", f"File not found!\n{expected_error_path}", 1, ''

        if result.stdout and not result.stderr:  
            print("OUTPUT:",expected_output_path)      
            try:
                with open(expected_output_path, "r") as expected_output:
                    expected_result = expected_output.read()
                    if result.stdout == expected_result:
                        return "PASS", None, result.returncode, expected_result
                    else:
                        return "FAIL", f"Output Mismatch!\nGot:\n{result.stdout}", 1, expected_result
            except FileNotFoundError:
                return "FAIL", f"File Not Found!\n{expected_output_path}", 1, ''

    except Exception as e:
        return "ERROR", str(e)

def main(): 
    errors = {"PASSED": 0, "FAILED": 0,"WC_Tests":0,"GRON_Tests":0,"CIPHER_Tests":0}
    total = 0
    flags = {
                "wc":['','-l','-w','-c'],
                "gron":[''],
                "cipher":['','-e','-d']
            }   

    for test_file in test_files:
        if test_file.startswith('wc'):
            program = "wc.py"
            errors["WC_Tests"]+=1
            additional_flags = flags['wc']
        elif test_file.startswith('gron'):
            program = "gron.py"
            errors["GRON_Tests"]+=1
            additional_flags = flags['gron']
        elif test_file.startswith('cipher'):
            program = "cipher.py"
            errors["CIPHER_Tests"]+=1
            additional_flags = flags['cipher']

        for run_type in ["cli", "stdin"]:
            # if additional_flags:
            for i in additional_flags:
                status, error_message, exit_code, expected_result = run_test(program, test_file, run_type, i)
                total += 1
                if exit_code > 0:
                    errors['FAILED'] += 1
                else:
                    errors['PASSED'] += 1

                print(f"{status} \n\tTest case: {test_file.split('.')[0]} {test_file.split('.')[1]}\n")
                print(f"\tRun Type: {run_type.upper()}")
                print(f"\tExit Code: {exit_code}")

                if error_message:
                    print(f"Output:\n{error_message}\n")
                    print(f"Expected Output:\n{expected_result}\n")
                print("-----------------------------------------------------------------")

        print("-----------------------------------------------------------------")
    for i, j in errors.items():
        print(f"{i} : {j}")
    print(f"TOTAL  : {total}")
    if errors['FAILED'] > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
