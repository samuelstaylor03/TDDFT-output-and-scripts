# Open the input file
with open('-40_GDD_pulse1.dat', 'r') as infile:
    # Read the content of the file
    lines = infile.readlines()

# Process the lines and multiply the last three columns by 10
processed_lines = []
for line in lines[1:]:  # Skip the first line (header)
    values = line.split()
    multiplied_values = [float(values[0])] + [float(val) * (5.75) for val in values[1:]]
    processed_lines.append('\t'.join(map(str, multiplied_values)))

# Write the processed data to the output file (pulse10.dat)
with open('-40_GDD_pulse5_75.dat', 'w') as outfile:
    # Write the header
    outfile.write(lines[0])
    # Write the processed lines
    outfile.write('\n'.join(processed_lines))

print("Data has been processed and written to output file")
