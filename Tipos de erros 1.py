#x = int(input('Digite um numero:'))
while True:
    try:
        # Se usuario teclar um numero TRUE encerra o programa
        x = int(input('Digite um numero:'))
        break
        # Se usuario digitar uma letra entra nessa Função except ValueError, e pergunta de novo
    except ValueError:
        print('Oops! Numero invalido Tente novamente...')
