def obter_mais_longa_substring(s):
#criação de variaveis para execução da função 
#um abc minusculo e um maiusculo caso a string possua letras maiusculas
    alfamin="abcdefghijklmnopqrstuvwxyz"
    alfamai="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#3 flags para serem utilizadas no codigo 
    flag1 = len(s) #Tamanho da string original
    flag2 = len(alfamai) #Tamanho do alphabeto
    flag3 = 0 #Contador para saber quando recomeçou o alphabeto
    lista1 = [] # Lista contendo substrng
    lista2 = [] # Lista Contendo a primeria maior sub_string
    z = 0 # Declaração da variavel que ira contar os caracteres da string s
    #Uso um while para passar por todas as letras da string S
    while z<flag1:
        #uso o for para que cada letra da rodada do while seja passada por todo o alphabeto
        for i in range(0, flag2):
            #Uso um if para comparar a letra atual da posição equivalente a Z a posição equivalente a i nos alfabetos 
            if s[z]==alfamin[i] or s[z]==alfamai[i]:
                #se uma das opções resultar em igualdade ele realiza uma comparação se a posição do alfabeto é menor que a flag 
                if i<flag3:
                    #se for menor então ele zerá a lista 1 e adiciona o caracter na lista 1 e então iguala a flag3 a posição i
                    #Assim se a proxima letra for uma letra anerior o flg ira sinalizar e novamente ira zerar a lista 1 
                    lista1=[]
                    lista1.append(s[z])
                    flag3 = i 
                #Se o i for maior que a flg significa que ou é o primeiro caracter ou é uma letra mais a frente do alphabeto então
                #ele somente adiciona esse caracter na lista 1 e atuaiza a posição do flag
                #Com isso se tiver letras iguais ele so adicionara uma vez que ele so zera se o flag for maior que i
                else:
                    lista1.append(s[z])
                    flag3 = i
            #nesse if comparamos se o tamanho da lista 1 é maior que a lista2 
            if ((len(lista1))>(len(lista2))):
                #se for então atualizamos a lista 2 para lista 1 
                # se não for não fazemos nada mantendo as duas como estão 
                lista2 = lista1
        pass
        z = z + 1
    #Aqui convertemos o resultado da lista dois em uma string
    snova=("".join(lista2)) 
    #aqui retonamos a nova substring
    return snova
#Sting Dada em aula
strig="azcbobobegghakl"
#uma nova string sera formada pela função e seu valor atribuido ao roulo sub_string
sub_string=(obter_mais_longa_substring(strig))
#imprimir na tela o resultado
print(sub_string)
