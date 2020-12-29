from file_reader import read_file_to_list 

def solve_dojo():
    input_list = read_file_to_list("input.txt")
    
    for i in range(len(input_list)):
        for j in range(len(input_list)):
            if i == j:
                continue
            outer_number = input_list[i]
            inner_number = input_list[j]
            if outer_number + inner_number == 2020:
                print(f"The solution is {outer_number}+{inner_number}={outer_number * inner_number}")
                return (outer_number * inner_number)


if __name__ == "__main__":
    solve_dojo()