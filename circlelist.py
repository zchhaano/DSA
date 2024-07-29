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
original_list = ['', 'U', '', '', 'L', 'F', 'R', 'B', '', 'D', '', '']

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
