color_actual = 0

def adoquinar(grid, top_left, bottom_right, special):
    global color_actual
    dx, dy = (bottom_right[0] - top_left[0]) // 2, (bottom_right[1] - top_left[1]) // 2
    if dx == dy == 1:
        for i in range(top_left[0], bottom_right[0]):
            for j in range(top_left[1], bottom_right[1]):
                if (i, j) != special:
                    grid[i][j] = str(color_actual)
        color_actual += 1
    else:
        centers = [(top_left[0]+dx-1, top_left[1]+dy-1), (top_left[0]+dx, top_left[1]+dy-1),
                   (top_left[0]+dx-1, top_left[1]+dy), (top_left[0]+dx, top_left[1]+dy)]
        for center in centers:
            if center != special:
                grid[center[0]][center[1]] = str(color_actual)
        color_actual += 1
        new_specials = [
            (top_left[0] + dx - 1, top_left[1] + dy - 1),
            (top_left[0] + dx, top_left[1] + dy - 1),
            (top_left[0] + dx - 1, top_left[1] + dy),
            center  # The correct new special for the bottom right quadrant
        ]
        adoquinar(grid, top_left, (top_left[0]+dx, top_left[1]+dy), new_specials[0])
        adoquinar(grid, (top_left[0], top_left[1]+dy), (top_left[0]+dx, bottom_right[1]), new_specials[1])
        adoquinar(grid, (top_left[0]+dx, top_left[1]), (bottom_right[0], top_left[1]+dy), new_specials[2])
        adoquinar(grid, (top_left[0]+dx, top_left[1]+dy), bottom_right, new_specials[3])

if __name__ == "__main__":
    import sys
    k = int(sys.argv[1])
    m = 2**k
    grid = [[' ' for _ in range(m)] for _ in range(m)]
    special = (0, 1)
    grid[special[0]][special[1]] = 'e'
    adoquinar(grid, (0, 0), (m, m), special)
    for row in grid:
        print(''.join(row))