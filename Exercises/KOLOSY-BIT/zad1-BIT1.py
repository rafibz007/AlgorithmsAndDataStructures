from random import  randint, shuffle
def distance(point):
    return (point[0]**2 + point[1]**2)**0.5

def insertion_sort(T, f):
    for i in range(1, len(T)):
        j = i
        x = T[i]
        while j-1 >= 0 and f(T[j-1]) > f(x):
            T[j] = T[j-1]
            j -= 1
        T[j] = x



def sort(points_list, k):
    for i in range(len(points_list)): points_list[i] = (points_list[i][0], points_list[i][1], distance(points_list[i]))
    # print(points_list)
    areas = [ [] for _ in range(len(points_list))]
    r1 = k/(len(points_list)**0.5)

    # for i in range(len(points_list)+1): print((i)**0.5*r1)
    # print("end")

    for point in points_list:
        # d = distance(point)
        d = point[2]
        ratio = (d/r1)**2
        diff = ( ratio - int(ratio) )
        # print(d, int(ratio), diff, r1)

        if diff == 0 and int(ratio) >= 1:
            areas[ int(ratio)-1 ].append(point)
        else: areas[ int(ratio) ].append(point)

    # print(areas)

    p_index = 0
    for area in areas:
        # insertion_sort(area, distance)
        insertion_sort(area, lambda x: x[2])
        for i in range(len(area)):
            points_list[p_index] = area[i]
            p_index += 1

    # print(T)
    for i in range(len(points_list)): points_list[i] = (points_list[i][0], points_list[i][1])


n = 10
k = 100
T = [ (randint(0, k), randint(0, k)) for _ in range(n) ]
print(T)
sort(T, k*(2**0.5)+1)
print(T)
