# Open the output file for writing
output = open('Output_File.txt', 'w')

# Task 1: Open the file and print the contents of the file
file = open('Sample_File.txt', 'r')
content = file.read()
output.write("1. Full content of the file:\n\n")
output.write(content + "\n")
file.close()

# Task 2: Print the first ten characters of the file
file = open('Sample_File.txt', 'r')
first_ten = file.read(10)
output.write("2. First 10 characters of the file:\n\n")
output.write(first_ten + "\n")
file.close()

# Task 3: Print the first line of the file
file = open('Sample_File.txt', 'r')
first_line = file.readline()
output.write("3. First line of the file:\n\n")
output.write(first_line.strip() + "\n")
file.close()

# Task 4: Print the first four lines of the file
file = open('Sample_File.txt', 'r')
output.write("4. First 4 lines of the file:\n\n")
for i in range(4):
    output.write(file.readline().strip() + "\n")
file.close()

# Task 5: Loop through the contents of the file and print all the lines one by one
file = open('Sample_File.txt', 'r')
output.write("5. All lines printed one by one:\n\n")
for line in file:
    output.write(line.strip() + "\n")
file.close()

# Task 6: Confirmation of closing files
output.write("\n6. All files have been closed properly after use.\n")

# Close the output file
output.close()
