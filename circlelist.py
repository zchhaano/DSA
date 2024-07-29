#%%
from collections import deque

def circular_shift_part_of_list(lst, positions, direction='right'):
    if not lst:
        return lst
    
    # Extract the elements at the specified positions
    elements_to_shift = [lst[pos] for pos in positions]

    # Use deque to perform the circular shift
    d = deque(elements_to_shift)
    if direction == 'left':
        d.rotate(-1)
    elif direction == 'right':
        d.rotate(1)
    else:
        raise ValueError("Direction must be 'left' or 'right'")

    # Place the shifted elements back into the original list
    for i, pos in enumerate(positions):
        lst[pos] = d[i]
    
    return lst

# Example usage:
orientation = ['', 'U', '', '', 'L', 'F', 'R', 'B', '', 'D', '', '']

def spinCube(direction,orientation):
    circlePos = [4,5,6,7]
    if direction == 'left':
        circular_shift_part_of_list(orientation,circlePos,direction = 'left')
    elif direction == 'right':
        circular_shift_part_of_list(orientation,circlePos,direction = 'right')   
     
def rollCube(orientation):
    circlePos = [4, 1, 6, 9]
    circular_shift_part_of_list(orientation,circlePos)

# %%
import re

# Original string
original_string = 'U1 B2 D3 B3 R3 L3 U1 L2 B2 R1 D3 R3 B1 L3 U2 B2 R1 D3 (18f*)'

# Remove the part inside parentheses
cleaned_string = re.sub(r'\s*\(.*\)', '', original_string)

# Split the cleaned string into individual commands
commands = cleaned_string.split()

# Print the result
print(commands)

# %%
print(original_string)
print(orientation)
for command in commands:
    char = command[0]  # Get the character part of the command
    print(command)
    if char in orientation:
        position = orientation.index(char)   # Find the position (1-based index)
        if position == 9:
            print ('spinCube',command[1])
        elif position in [5, 7]:
            print ('spinCube left if 7, right if 5, then rollCube, then spinCube',command[1])
        elif position in [1, 4, 6]:
            print(f'rollCube till {char} in position 9')
# %%
