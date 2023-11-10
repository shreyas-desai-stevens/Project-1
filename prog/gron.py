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
    try:
        if len(sys.argv) == 2:
            input_file = sys.argv[1]
            with open(input_file, 'r') as file:
                json_data = json.load(file)
        else:
            json_data = json.load(sys.stdin)
        result_lines = gron(json_data)
                
    except Exception as e:
        print(f"Error: {e}",file=sys.stderr)
        sys.exit(1)
        # print(e)
    
    for line in result_lines:
        print(line)

    

if __name__ == "__main__":
    main()
