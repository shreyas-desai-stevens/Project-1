import json
import sys

def generate_gron_structure(json_data, parent_key='json', depth=0):
    result = []

    if isinstance(json_data, dict):
        result.append(f"{parent_key} = {{}};")
        for key, value in sorted(json_data.items()):
            new_key = f"{parent_key}.{key}" if parent_key else key
            result.extend(generate_gron_structure(value, new_key, depth=depth + 1))
    elif isinstance(json_data, list):
        result.append(f"{parent_key} = [];")
        for i, item in enumerate(json_data):
            new_key = f"{parent_key}[{i}]"
            result.extend(generate_gron_structure(item, new_key, depth=depth + 1))
    else:
        result.append(f"{parent_key} = {json.dumps(json_data)};")

    return [f"{line}" for line in result]

def main():
    if len(sys.argv) == 2:
        # Read JSON from file
        input_file = sys.argv[1]
        with open(input_file, 'r') as file:
            json_data = json.load(file)
    else:
        # Read JSON from stdin
        json_data = json.load(sys.stdin)

    result_lines = generate_gron_structure(json_data)

    # Print the result
    for line in result_lines:
        print(line)

if __name__ == "__main__":
    main()
