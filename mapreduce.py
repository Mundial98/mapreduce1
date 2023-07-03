import sys
import subprocess


def map_operation(map_script, src_file, dst_file):
    # Read input file
    with open(src_file, 'r') as file:
        lines = file.readlines()

    # Apply map script to each line
    output = []
    for line in lines:
        command = ["python", map_script]  # Use "python" to run the map_script
        process = subprocess.run(command, input=line.encode(), capture_output=True, shell=True)  # Add shell=True for Windows
        output.append((line.strip(), process.stdout.decode().strip()))

    # Write output to destination file
    with open(dst_file, 'w') as file:
        for key, value in output:
            file.write(f"{key}\t{value}\n")






def reduce_operation(reduce_script, src_file, dst_file):
    # Read input file
    with open(src_file, 'r') as file:
        lines = file.readlines()

    # Group entries by key
    data = {}
    for line in lines:
        line = line.strip()
        if '\t' in line:
            key, value = line.split('\t', 1)  # Split the line into two parts
            if key in data:
                data[key].append(value)
            else:
                data[key] = [value]

    # Apply reduce script to each group
    output = []
    for key, values in data.items():
        input_data = '\n'.join(values)
        command = ["python", reduce_script]  # Use "python" to run the reduce_script
        process = subprocess.run(command, input=input_data.encode(), capture_output=True, shell=True)  # Add shell=True for Windows
        output.append((key, process.stdout.decode().strip()))

    # Write output to destination file
    with open(dst_file, 'w') as file:
        for key, value in output:
            file.write(f"{key}\t{value}\n")





def main():
    if len(sys.argv) < 5:
        print("Usage: python mapreduce.py <operation> <script> <src_file> <dst_file>")
        return

    operation = sys.argv[1]
    script = sys.argv[2]
    src_file = sys.argv[3]
    dst_file = sys.argv[4]

    if operation == "map":
        map_operation(script, src_file, dst_file)
    elif operation == "reduce":
        reduce_operation(script, src_file, dst_file)
    else:
        print("Invalid operation. Supported operations: 'map' or 'reduce'")


if __name__ == '__main__':
    main()
