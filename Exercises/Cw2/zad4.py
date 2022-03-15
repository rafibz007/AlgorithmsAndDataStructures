def height_to_liters(list_of_containers, height):
    amount_of_flooded = 0
    liters = 0

    # list_of_containers = [((x1, y1),(x2, y2)), ((x3,y3),(x4,y4)),...]
    for container in list_of_containers:
        left_top = container[0]
        right_down = container[1]
        c_height = left_top[1] - right_down[1]
        c_width = left_top[0] - right_down[0]

        if left_top[1] <= height:
            liters += c_width*c_height
            amount_of_flooded += 1
        elif right_down[1] < height < left_top[1]:
            flooded_height = height - right_down[1]
            liters += c_width*flooded_height


    # print(height, liters, amount_of_flooded, end='')
    return liters, amount_of_flooded


def find_amount_of_flooded(list_of_containers, liters):
    max_height = 0
    min_height = 999
    for container in list_of_containers:
        max_height = max(max_height, container[0][1])
        min_height = min(min_height, container[1][1])

    top = max_height
    bottom = min_height
    amount_flooded = 0

    prev_found_liters = 0
    prev_amount_flooded = 0

    while bottom <= top:
        mid = (bottom+top)//2
        found_liters, amount_flooded = height_to_liters(list_of_containers, mid)
        # print(" --",bottom, top)

        if found_liters < liters: bottom = mid + 1
        elif found_liters > liters: top = mid - 1
        else: return amount_flooded

        if prev_found_liters < liters < found_liters: return prev_amount_flooded

        prev_found_liters = found_liters
        prev_amount_flooded = amount_flooded

    return amount_flooded


T = [((2, 3), (0, 2)), ((7, 5),(3, 1)) ]
for i in range(100): print(i,find_amount_of_flooded(T, i))
# print(find_amount_of_flooded(T, 11))
# print(height_to_liters(T, 2))