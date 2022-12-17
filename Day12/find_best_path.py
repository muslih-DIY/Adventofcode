import numpy as np


def inputarray():
    inputarray = []

    with open('Day12\input.txt') as input_file:
        data = 1
        while data:
            data = input_file.readline()
            if not data:break
            inputarray.append([ord(c)-96 for c in data if 96<ord(c)<123])
    return np.array(inputarray,dtype=object)

FINAL_STATE = 26
ROW_MAX = inputarray().shape[0]
COL_MAX = inputarray().shape[0]
LARGE_ROUTE = ROW_MAX*COL_MAX
visted_location = []

def valid_state(row = ROW_MAX,col = COL_MAX,next_state:tuple=(0,0),pre_state=(0,0)):
    # print(next_state,pre_state)
    # print(next_state != pre_state)
    # print(0<=next_state[0]<=row )
    # print(0<=next_state[1]<=col)    
    # print(row,col)    
    global visted_location
    if next_state != pre_state and 0<=next_state[0]<row and  0<=next_state[1]<col and next_state not in visted_location :
        return next_state

def find_next_paths(grid = inputarray(),state:tuple=(0,0),pre_state=(0,0)):
    get_state = lambda state : state and  grid[state[0]][state[1]] or -1
    
    current = get_state(state)
    states = (
        valid_state(next_state=(state[0]+1,state[1]),pre_state=pre_state),
        valid_state(next_state=(state[0],state[1]+1),pre_state=pre_state),
        valid_state(next_state=(state[0]-1,state[1]),pre_state=pre_state),
        valid_state(next_state=(state[0],state[1]-1),pre_state=pre_state)
        )
    state_vals = (get_state(state) for state in states)
    
    valid_states = [(a,b) for a,b in zip(states,state_vals) if b in (current,current+1)]
    
    valid_higer_state = [a for a,b in valid_states if b==(current+1)]

    if valid_higer_state :return valid_higer_state
    return [a for a,b in valid_states]


def best_path(grid = inputarray(),current_state:tuple=(0,0),pre_state=(0,0),cost = 0):
    get_state = lambda state : grid[state[0]][state[1]]
    global visted_location 
    visted_location.append(current_state)
    if get_state(current_state) == FINAL_STATE:return cost+1
    states = find_next_paths(state=current_state,pre_state=pre_state)
    if not states: return LARGE_ROUTE
    print(states)
    costs = [
        best_path(current_state=stat,pre_state=current_state,cost=cost)
        for stat in states]
    return min(costs)


if __name__=='__main__':

    print(best_path(current_state=(0,0)))
