def div():
    try:
        num1 = int(input('Digite um numero'))
        num2 = int(input('Digite um numero'))
        res = num1 / num2
    # Se o usuario tentar dividir um numero por ZERO cai nessa função e retorna
    except ZeroDivisionError:
        print('Oops Erro de divisão por zero')
    # Se o usuario digitar uma letra no lugar de um numero entra nessa fução
    except:
        print('Vixiiii algo de errado')
    else:
        return res
    finally: # O finally sempre vai executar os esta atrelado ao Try:
        print('Executar sempre')

#Programa principal
print(div()) # Imprimi se tudo estiver certo o codigo