T = [1,2,3,1,2,2,2]
counter = 0
j = None
for i in range(len(T)):
    if counter == 0:
        counter = 1
        j = 1
    elif T[j] == T[i]: counter += 1
    else: counter -= 1

counter = 0
for i in range(len(T)):
    if T[i] == T[j]: counter += 1

if counter > len(T)/2: print(T[j])
else: print("NO")