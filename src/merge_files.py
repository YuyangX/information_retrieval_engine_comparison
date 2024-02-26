def merge_text_files(input_files, output_file):
    with open(output_file, 'w') as outfile:
        for input_file in input_files:
            with open(input_file, 'r') as infile:
                outfile.write(infile.read())

# List of input .txt files
input_files = ['documents/qrels.1-50.AP8890.txt', 'documents/qrels.51-100.AP8890.txt', 'documents/qrels.101-150.AP8890.txt']

# Output file
output_file = 'documents/qrels.1-150.AP8890.txt'

# Merge the input files into the output file
merge_text_files(input_files, output_file)

print("Files merged successfully!")
