def interval( X ):

    X.sort()

    if len(X) == 0: return 0

    S = []
    S.append( [ X[0], X[0]+1 ] )

    for x in X:
        if x > S[-1][1]:
            S.append( [ x, x+1 ] )

    return len(S), S


X = [ 0.25, 0.5, 1.6, 2.6, 2.7 ]
print(interval(X))


