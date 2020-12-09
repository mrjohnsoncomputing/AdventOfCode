import helper
print("Advent of Code: Day 8")

def run_instruction(instruction, accumulator):
    # "nop +0"
    # ["nop", "+0"]
    instruction = instruction.split(" ")
    command = instruction[0]
    argument = int(instruction[1])
    
    if command == "nop":
        return [1, accumulator]
    elif command == "acc":
        accumulator += argument
        return [1, accumulator]
    elif command == "jmp":
        return [argument, accumulator]
    else:
        print("DANGER")
        return [1, accumulator]

def part1(program):
    accumulator = 0
    current_instruction_position = 0
    instructions_run = []

    while current_instruction_position not in instructions_run:
        instruction = program[current_instruction_position]
        #print(instruction)
        instructions_run.append(current_instruction_position)
        results = run_instruction(instruction, accumulator)
        current_instruction_position += results[0]
        accumulator = results[1]
    print("Part 1 Accumulator Value:", accumulator)

def program_is_valid(program):
    accumulator = 0
    current_instruction_position = 0
    instructions_run = []
    program_length = len(program)

    # This while loop had a bad condition <= != <
    while current_instruction_position < program_length:
        
        instruction = program[current_instruction_position]
        
        instructions_run.append(current_instruction_position)
        results = run_instruction(instruction, accumulator)
        current_instruction_position += results[0]
        accumulator = results[1]
        
        # Took a condition out of the while and into the loop
        if current_instruction_position in instructions_run:
            return False
        
    
    if current_instruction_position == program_length:
        return accumulator
    else:
        return False
    

def swap_commands(old_command, new_command, program):
    valid_program = False
    position = 0
    programs = 0
    while valid_program == False:
        updated_program = program.copy()
        programs += 1
        
        # change nop - jmp
        #found = False
        if position >= len(updated_program):
            return False

        for i in range(position, len(updated_program)):
            command = updated_program[i].split(" ")[0]
            #print(updated_program)
            if command == old_command:
                updated_program[i] = updated_program[i].replace(old_command, new_command)
                #print(updated_program)
                valid_program = program_is_valid(updated_program)
                if valid_program != False:
                    print("Part 2 Accumulator Value:", valid_program)
                    return True
                #found = True
                position = i+1
                break
            
            if i == len(updated_program)-1:
                return False
    return True

def part2(program):
    found = swap_commands("nop", "jmp", program)
    found = swap_commands("jmp", "nop", program)
                 

        


test_data = [
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",
    "acc +6",
    ]


# 
puzzle_data = helper.readfile("2020/day8data.txt")
part1(puzzle_data)

part2(puzzle_data)
