def get_all_dot_positions(xsize, ysize):
    return [(x,y) for x in range(1, xsize-1) for y in range(1, ysize-1)]

def create_grid_string(dots, xsize, ysize):
    grid = ""
    for y in range(ysize):
        for x in range(xsize):
            print("in inner loop") #seeing if this inner part of the for loop is executing
            grid += "." if (x, y) in dots else "#"
        grid = "\n"  #SHOULD BE grid += "\n" --> if just =, reassigning the variable, not updating it and nothing is printed
    print(grid)
    return grid

positions = get_all_dot_positions(5, 5)
print(create_grid_string(positions, 5, 5))
