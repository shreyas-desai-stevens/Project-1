import subprocess

program = 'gron.py'
input_path = 'test/gron.test_1.in'

cmd = f"python prog/{program} {input_path}"

result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

print(result)
# Check if the command was successful or not
if result.returncode == 0:
    print("Command executed successfully")
else:
    # Print the stderr content (error messages)
    print(f"Error: {result.stderr}")

# Print the stdout content
print("STDOUT:")
print(result.stdout)
