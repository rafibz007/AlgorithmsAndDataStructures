def pack( W, K ):
    W.sort(reverse=True)
    S = []

    for w in W:
        if K<=0: break
        if w<=K:
            S.append(w)
            K-=w

    return sum(S), S



W = [2,2,4,8,1,8,16]
K = 27

print( pack(W,K) )