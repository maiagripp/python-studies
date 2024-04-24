def pesquise(lista, valor):
  if valor in lista:
    return print(lista.index(valor))
  return None


L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))