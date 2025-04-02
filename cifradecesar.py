# Criptografia de Texto com Cifra de César : IDEAÇÃO E PROTOTIPAÇÃO DE SOFTWARES

# Solicitar o texto a ser encriptado
texto = input("Texto a ser encriptado: ")

# Chave a ser utilizada
chave = int(input('Valor da chave (deslocamento): '))

# Processo de confirmação de encriptação
output = input('Aperte E para confirmar a encriptação: ').upper()  # Converte para maiúsculo

# Verificar se o usuário apertou "E"
while output != 'E':
    print('Opção inválida. Por favor, aperte E para confirmar a encriptação.')
    output = input('Aperte E para confirmar a encriptação: ').upper()

# Caracteres a serem utilizados
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Variável para armazenar o texto criptografado
convertido = ''

# Código que será executado em cada caractere do texto
for caractere in texto:
    if caractere.upper() in letras:  # Verifica se o caractere é uma letra
        num = letras.find(caractere.upper())  # Pega o índice da letra (convertendo para maiúscula)

        # Deslocamento da chave
        num = num + chave

        # Manipular a rotação se o valor de num for maior do que o comprimento de letras ou menor que 0
        if num >= len(letras):
            num = num - len(letras)
        elif num < 0:
            num = num + len(letras)

        # Verificar se a letra original era minúscula e converter de volta, se necessário
        if caractere.islower():
            convertido += letras[num].lower()  # Converter para minúsculo se necessário
        else:
            convertido += letras[num]  # Se for maiúsculo, mantém maiúsculo
    else:
        # Concatenar o caractere sem efetuar criptografia
        convertido += caractere

# Mostrar o texto encriptado na tela
print('O texto criptografado é:', convertido)
