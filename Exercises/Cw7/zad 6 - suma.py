#szukany x bedzie mediana zbioru - bo ma z lewej i prawej tyle samo pkt wiec przesuwajac sie w lewo
#lub prawo nie zmienimy sumy, jesli z lewej mielibysmy mniej pkt i przesuwali sie w lewo
# to nasza suma by sie zwiekszala, wiec trzeba isc w prawo, analogicznie z prawej
# O(1)
def find_x( A ):
    n = len(A)
    if n%2 == 1: return A[int(n//2)]
    return (A[int(n//2)-1] + A[int(n//2)])/2
