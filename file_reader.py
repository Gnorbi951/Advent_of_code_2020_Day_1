def read_file_to_list(filename):
    file = open(filename, "r")
    input_list = [int(line.split('\n')[0]) for line in file]
    print(input_list)
