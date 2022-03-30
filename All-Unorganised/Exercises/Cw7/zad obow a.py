from random import randint

def tank_a( P, S, L ):
    counter = 0
    R = []
    """
    Na kazdej stacji tankujemy do pelna i jedziemy tak daleko jak damy rade
    
    Jezeli nasze optymalne rozwiazanie w pierwszym kroku nie jedzie tak daleko jak da rade, a my ten ruch wykonamy
    znaczy to ze skoro z poprzedniej stacji dalo sie wskoczyc na optymalne rozwiazanie, to z pola dalszego tez damy rade
    wiec odtworzymy to najlepsze rozwiazanie
    """

    n = len(S)
    i = 0
    R.append(i)
    while i < n-1:
        k = 1
        while i+k+1 <= n-1 and S[i+k+1] - S[i] <= L: k+=1
        i += k
        counter += 1
        R.append(i)

    return counter, R

def tank_b1( P, S, L ):

    def min_index_in_range( P, i, j ):
        result = i
        for x in range( i+1, j+1 ):
            if P[result] > P[x]: result = x
        return result

    """
    Na kazdej stacji patrzymy w przod na kazda stacje do ktorej potencjalnie jestesmy w stanie dojechac
    Jezeli jakas stacja w naszym zasiegu ma tansze paliwo to tankujemy tyle zeby do niej dojechac i jedziemy do niej
    Natomiast jesli nasza stacja ma najtansze paliwo wsrod wszystkich w zasiegu to tankujemy w niej do pelna
    i jedziemy do najtanszej nastepnej stacji
    
    Zalozmy ze mamy optymalna trase ktora jest inna niz wybralby algorytm
    przejezdzamy w niej z pkt A->C, podczas gdy na stacji B jest tansze paliwo niz w C
    zatem odcinek B->C pokonujemy wiekszym kosztem, poniewaz teraz bedziemy musieli je uzupelnic C, a gdybysmy to zrobili
    w B, wyszloby taniej, zatem nasze optymalne rozwiazanie nie bylo optymalne, sprzecznosc
    - nasz algorytm dziala
    """
    R = []
    current_fuel = L
    total_cost = 0
    n = len(P)
    i = 0
    R.append(i)
    while i < n-1:
        if i+1 < n and S[i+1]-S[i] > L: return False
        our_range = 1 #maksymalnie o ile stacji jestesmy w stanie pojechac do przodu
        while i + our_range + 1 <= n - 1 and S[i+our_range+1] - S[i] <= L: our_range += 1

        #szukam najtanszej stacji w okolicy
        min_prize = min_index_in_range( P, i, i+our_range )

        #jesli koniec w zasiegu i nie trzeba juz robic przystankow i tankowac aby dotrzec do celu
        if i+our_range >= n-1 and min_prize == i:
            total_cost += max( 0, ((S[n-1] - S[i])-current_fuel)*P[i] )
            current_fuel = max(current_fuel, S[n-1] - S[i])
            destination = n-1

        # jesli u nas najtaniej to tankuje do pelna i jedzie na nastepna najtansza
        elif min_prize == i:
            total_cost += (L-current_fuel)*P[i]
            current_fuel = L
            destination = min_index_in_range( P, i+1, i+our_range )

        #inaczej tankuje tyle zeby dojechac do najtanszej stacji
        else:
            total_cost += max( 0, ( ((S[min_prize] - S[i]) - current_fuel )*P[i]) )
            current_fuel = max( current_fuel, S[min_prize] - S[i] )
            destination = min_prize

        # print(f"i:{i}   dest:{destination}    cost:{total_cost}    fuel:{current_fuel}    what will left:{current_fuel - (S[destination]-S[i])}")
        current_fuel -= S[destination]-S[i]
        i = destination
        R.append(i)

    return total_cost, R

# f(i) - min koszt aby dojechac na pole i, pod warunkiem ze zawsze tankujemy do pelna
# f(i) = min{ f(i-v)+(S[i]-S[i-v])*P[i] | S[i]-S[i-v] <= L and i-v >= 0 }
# min{ f(k) | S[n-1]-S[k] <= L } 0<=k<n-1 - rozw
# rozw zapisze sobie w F[n-1] dla wygody, bo i tak nie uzywalem tego pola
def tank_b2_dynamic( P, S, L ):

    def get_solution( i, R ):
        if R[i] > -1:
            return get_solution( R[i], R ) + [i]
        return [i]

    n = len(P)
    inf = sum(S)*sum(P)
    F = [inf]*n

    R = [-1]*n

    F[0] = 0
    for i in range( 1, n-1 ):
        if S[i] - S[i-1] > L: return False
        F[i] = F[i-1] + (S[i] - S[i-1])*P[i]
        R[i] = i-1
        v=2
        while i-v >= 0 and S[i]-S[i-v] <= L:
            q = F[i-v]+(S[i]-S[i-v])*P[i]
            # print(i, i-v, q, S[i]-S[i-v], S[i], S[i-v])
            if q < F[i]:
                F[i] = F[i-v]+(S[i]-S[i-v])*P[i]
                R[i] = i-v
            v += 1

    v=2
    i = n-1
    if S[i]-S[i-1] > L: return False
    F[i] = F[i-1]
    R[i] = i-1
    while i-v >= 0 and S[i] - S[i-v] <= L:
        if F[i-v] < F[i]:
            F[i] = F[i-v]
            R[i] = i-v
        v += 1

    return F[n-1], get_solution(i, R)


def tank_b2( P, S, L ):

    def min_index_in_range( P, S, i, j ):
        curr_min = i
        index = i-1
        for x in range( i+1, j+1 ):
            q = (S[x]-S[index])*P[x]
            if (S[curr_min]-S[index])*P[curr_min] > q:
                curr_min = x
        return curr_min



    """
    dla kazdego pola pola licze ile wyniesie mnie skok na to pole i wybieram najmniejsza mozliwosc
    
    DALEJ NIE DZIALA :/
    PODDAJE SIE CHYBA NIESTETY
    
    """
    R = []
    current_fuel = 0
    total_cost = 0
    n = len(P)
    i = 0
    R.append(i)
    while i < n - 1:
        if i+1 < n and S[i+1] - S[i] > L: return False

        our_range = 1  # maksymalnie o ile stacji jestesmy w stanie pojechac do przodu
        while i + our_range + 1 <= n - 1 and S[i + our_range + 1] - S[i] <= L: our_range += 1

        # szukam najtanszej stacji w okolicy
        min_prize = min_index_in_range(P, S, i+1, i + our_range)

        # jesli koniec w zasiegu i nie trzeba juz robic przystankow i tankowac aby dotrzec do celu
        if i + our_range >= n - 1:
            total_cost += max(0, (L - current_fuel) * P[i])
            current_fuel = L
            destination = n - 1

        # jesli u nas najtaniej to tankuje do pelna i jedzie na nastepna najtansza
        else:
            total_cost += (L-current_fuel)*P[i]
            current_fuel = L
            destination = min_prize

        # print(f"i:{i}   dest:{destination}    cost:{total_cost}    fuel:{current_fuel}    what will left:{current_fuel - (S[destination]-S[i])}")
        current_fuel -= S[destination] - S[i]
        i = destination
        # print(i)
        R.append(i)

    return total_cost, R


S = [  0,  5,  7,  9, 12, 13, 20 ]
P = [ 10, 15, 23,  7,  8, 11, 16 ]
L = 8
print(tank_a(P,S,L))
print(tank_b1(P,S,L))
print(tank_b2_dynamic(P,S,L))


# for _ in range( 100 ):
#     S = [  0,  5,  7,  9, 12, 13, 20 ]
#     P = [ randint(1, 50) for _ in range(7) ]
#     L = randint(1, 10)
#
#     t1 = tank_b2(P,S,L)
#     t2 = tank_b2_dynamic(P,S,L)
#
#     if type(t1) is not bool and type(t2) is not bool and t1[1] != t2[1]:
#         print(f"t1:{t1}   t2:{t2}   S:{S}   P:{P}   L:{L}")
