"""
f(v) - maks ilosc "wzietych krawedzi do skojarzenia", gdy biore jedno dziecko v

g(v) - maks ilosc wzietych krawedzi, gdzy nie biore dziekca v

f(v) = max( g(u) + max( f(w), g(w) ) +1 )
gdzie u,w sa dziecmi v ( bierzemy krawedz (u,v), a w to pozostale )

g(v) = sum( max( f(u), g(u) ) )
gdzie u to dziecki v

Uzywamy DFS
g(v) mozna obliczac przy przetwarzaniu wierzcholka v
f(v) obliczamy po przetworzeniue wierzcholka v

"""