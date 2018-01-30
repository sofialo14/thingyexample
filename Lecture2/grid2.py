def get_all_dot_positions(xsize, ysize):
    return [(x,y) for x in range(1, xsize-1) for y in range(1, ysize-1)]

def create_grid_string(dots, xsize, ysize):
    for y in range(ysize):
        grid = ""  #this grid variable should NOT be initialized w/in the for loop (should be before it);
                   #it's being re-initiliazed in each loop
                   #so only the last line the for loop runs will be printed
        for x in range(xsize):
            grid += "." if (x, y) in dots else "#"
        grid += "\n"
    return grid

positions = get_all_dot_positions(5, 5)
print(create_grid_string(positions, 5, 5))
