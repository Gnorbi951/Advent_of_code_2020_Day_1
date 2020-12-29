def read_file_to_list(filename):
    input_file = open(filename, "r")
    input_list = [int(line.split('\n')[0]) for line in input_file]
    input_file.close()
    return input_list
