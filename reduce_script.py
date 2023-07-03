with open(src_file, 'r') as file:
    lines = file.readlines()

word_counts = {}

for line in lines:
    key, value = line.strip().split('\t')
    if key in word_counts:
        word_counts[key] += int(value)
    else:
        word_counts[key] = int(value)

with open(dst_file, 'w') as file:
    for key, value in word_counts.items():
        file.write(f"{key}\t{value}\n")
