def encriptar (message, key):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    encriptada = ""

    for i in message:
        letra_criptografada = ((ord(i) - ord('a'))+key)%26
        encriptada += alfabeto[letra_criptografada]
    return encriptada 

message = input("Qual é a sua mensagem?")
mensagem_encriptada = encriptar(message, 10)
print(mensagem_encriptada)