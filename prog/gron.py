import argparse
import json
import sys

def gron(json_data, base_obj='json', depth=0):
    result = []

    if isinstance(json_data, dict):
        result.append(f"{base_obj} = {{}};")
        for key, value in sorted(json_data.items()):
            new_key = f"{base_obj}.{key}" if base_obj else key
            result.extend(gron(value, new_key, depth=depth + 1))
    elif isinstance(json_data, list):
        result.append(f"{base_obj} = [];")
        for i, item in enumerate(json_data):
            new_key = f"{base_obj}[{i}]"
            result.extend(gron(item, new_key, depth=depth + 1))
    else:
        result.append(f"{base_obj} = {json.dumps(json_data)};")

    return [f"{line}" for line in result]

def main():
    parser = argparse.ArgumentParser(description="Return a JSON file structure in a flattened way")
    parser.add_argument("input_json", nargs='?', type=argparse.FileType("r"), default=sys.stdin, help="File to flatten JSON from (default is stdin)")
    parser.add_argument("-o","--object",nargs='?',help="Add a base object of your choice (default is 'json')")
    args = parser.parse_args()
    try:
        with args.input_json as json_file:
            json_data = json.load(json_file)

        if args.object:
            result_lines = gron(json_data,base_obj=args.object)
        else:
            result_lines = gron(json_data)

        for line in result_lines:
            print(line)
                
    except Exception as e:
        sys.stderr.write(f"Error: {e}")
        sys.exit(1)
    

if __name__ == "__main__":
    main()
