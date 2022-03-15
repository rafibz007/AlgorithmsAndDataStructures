def first_n_sec_max( H ):
      first = -1
      second = 0
      if H[first] < H[second]: first, second = second, first
      for i in range( len(H) ):
            if H[i] > H[first]:
                  second = first
                  first = i
            elif H[i] > H[second]:
                  second = i

      return first, second

#przy obliczaniu zysku biore pod uwage takze jak zmieni sie najwyzsza wieza dodajac do Z(zysku) roznice zmian max wiezy
#zysk obliczam w pozostalych sprawdzajac biorac najwiekszy klocek
#biore to co daloby mi najwiekszy zysk
def steal( my_child, W ):
      counter = 0
      m = len(W)
      n = len(W[0])
      for i in range(m): W[i].sort()
      H = [ sum(W[i]) for i in range(m) ]
      Z = [-1]*m #zysk, ile nam da wziecie i-tego klocka
      flag = True
      # print(H)
      while flag:
            biggest, second_biggest = first_n_sec_max(H)

            for i in range(m):
                  if i == my_child: continue
                  if i == biggest:
                        new_max_height = max( H[biggest]-W[i][-1], H[second_biggest] )
                        max_height_change = H[biggest] - new_max_height
                        Z[i] = W[i][-1] + max_height_change
                  else:
                        Z[i] = W[i][-1]

            max_idx = 0
            for i in range( m ):
                  if Z[i] > Z[max_idx]: max_idx = i

            counter += 1
            H[my_child] += W[max_idx][-1]
            H[max_idx] -= W[max_idx][-1]
            W[my_child].append( W[max_idx][-1] )
            W[max_idx][-1] = 0
            W[max_idx].sort()

            flag = False
            for i in range( m ):
                  if H[my_child] <= H[i] and i != my_child:
                        flag = True
                        break

      return counter, H, W

W = [
  [2, 3, 5, 7],
  [8, 8, 8, 8],
  [10, 1, 2, 3],
  [1, 1, 2, 5]
]
print(steal(3, W))
W2 = [
  [7, 0],
  [5, 6],
  [2, 0]
]
print(steal(2, W2))
W3 = [
  [5, 4, 3],
  [11, 0, 0],
  [2, 0, 0]
]
print(steal(2, W3))









