ESPACOS_POR_NIVEL = 4

def imprime_elementos(l, nivel=0):
    espacos = " " * ESPACOS_POR_NIVEL * nivel
    if type(l) == list:
        print(espacos, "[")
        for e in l:
            imprime_elementos(e, nivel + 1)
        print(espacos, "]")
    else:
        print(espacos, l)
        
L = [1, [2, 3, 4, [5, 6, 7]]]

imprime_elementos(L)