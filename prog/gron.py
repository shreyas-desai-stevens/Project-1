import argparse
import json
import sys

def gron(json_data, parent_key='json', depth=0):
    result = []

    if isinstance(json_data, dict):
        result.append(f"{parent_key} = {{}};")
        for key, value in sorted(json_data.items()):
            new_key = f"{parent_key}.{key}" if parent_key else key
            result.extend(gron(value, new_key, depth=depth + 1))
    elif isinstance(json_data, list):
        result.append(f"{parent_key} = [];")
        for i, item in enumerate(json_data):
            new_key = f"{parent_key}[{i}]"
            result.extend(gron(item, new_key, depth=depth + 1))
    else:
        result.append(f"{parent_key} = {json.dumps(json_data)};")

    return [f"{line}" for line in result]

def main():
    parser = argparse.ArgumentParser(description="Return a JSON file structure in a flattened way")
    parser.add_argument("input_json", nargs='?', type=argparse.FileType("r"), default=sys.stdin, help="File to flatten JSON from (default is stdin)")
    
    args = parser.parse_args()
    try:
        with args.input_json as json_file:
            json_data = json.load(json_file)

        result_lines = gron(json_data)

        for line in result_lines:
            print(line)
                
    except Exception as e:
        sys.stderr.write(f"Error: {e}")
        sys.exit(1)
    

if __name__ == "__main__":
    main()
