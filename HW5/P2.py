def P2(input_filename: str, output_filename: str) -> None:        
    ##### Write your Code Here #####
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            name, number, weight = line.split()
            output_file.write(f'{name}\'s atomic number is {number} and atomic weight is {weight}\n')
    ##### End of your code #####