"""
f(h) - zwraca ilosc litrow oraz kontenerow zalanych dla danej wysokosci h
strzelam binarnie od hmin do hmax, przestaje gdy jakas zmiana strzalu nie zmienila liczby kontenerow
ale podana liczba litrow miesci sie miedzy tymi przedzialami
"""

def find_amount_of_flooded(A,liters):

    def amount_of_flooded( height ):
        nonlocal A

        liters = 0
        flooded_cont = 0

        for i in range(len(A)):
            p1, p2 = A[i]

            # print(p1, p2)

            cont_flood_liters = 0
            if p1[1] <= height:
                cont_flood_liters = (p2[0]-p1[0])*(p1[1]-p2[1])
                flooded_cont += 1
            elif p2[1] < height < p1[1]:
                cont_flood_liters = (p2[0]-p1[0])*(height-p2[1])

            liters += cont_flood_liters

        return flooded_cont, liters


    min_height = float("inf")
    max_height = -float("inf")
    max_liters = 0
    for i in range( len(A) ):
        min_height = min(min_height, A[i][0][1], A[i][1][1])
        max_height = max(max_height, A[i][0][1], A[i][1][1])
        p1, p2 = A[i]
        max_liters += (p2[0]-p1[0])*(p1[1]-p2[1])

    if liters >= max_liters: return len(A)

    top = max_height+1
    bot = min_height-1
    prev_flooded_cont = float("inf")
    prev_flooded_liters = float("inf")

    # if liters == 0: return 0

    while bot <= top:
        mid = (top+bot)/2

        flooded_cont, flooded_liters = amount_of_flooded(mid)

        # print(flooded_cont, flooded_liters, "-",bot, top, mid)

        if (flooded_liters < liters < prev_flooded_liters or\
            prev_flooded_liters < liters < flooded_liters)\
            and flooded_cont == prev_flooded_cont: return flooded_cont

        # print("--", liters)

        if flooded_liters > liters: top = mid
        elif flooded_liters < liters: bot = mid
        else: return flooded_cont

        prev_flooded_cont = flooded_cont
        prev_flooded_liters = flooded_liters

        if top == bot: break


    return 0




T = [((0, 3), (2, 2)), ((3, 5),(7, 1)) ]
for i in range(100): print(i,find_amount_of_flooded(T, i))
# find_amount_of_flooded(T, 18)