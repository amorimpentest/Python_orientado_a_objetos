def tupla_par(tupla):
	lista = []
	for i in range(0, len(tupla)):
		if i%2==0:
			lista.append(tupla[i])
	t = tuple(lista)
	return t
tupla1 = ('oi', 'estou', 'estudando', 'poo')
tupla2 = (tupla_par(tupla1))
print(tupla2)
