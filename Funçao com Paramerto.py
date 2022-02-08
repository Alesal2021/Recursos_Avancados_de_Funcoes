def imprime_com_condicao(num, s1):
    if s1(num):
        print(num)
def par(x):
    return x % 2 == 0
def impar(x):
    return not par(x)
#Programa Principal
imprime_com_condicao(3,impar) # Aqui pedindo a função par ou impar a mostrar o print
