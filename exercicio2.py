def tupla_par(tupla):
    #Crio uma lista em branco para preencher com os valores da tupla
    lista = []
    #Criar um for para pecorrer todos os elementos da tupla
	for i in range(0, len(tupla)):
	    #se a posição em que estu da tupla for par adiciono ao fim da lista o campo atual da tupla
		if i%2==0:
			lista.append(tupla[i])
	#Ao final do for tranformo a lista em uma tupla associada ao rotulo t
	t = tuple(lista)
    #Retorno uma tupla
	return t
#conteudo da tupla1 como no exemplo
tupla1 = ('oi', 'estou', 'estudando', 'poo')
#nova tupla com a tupla da função tulpa_par
tupla2 = (tupla_par(tupla1))
#printo na tela a nova tupla
print(tupla2)
