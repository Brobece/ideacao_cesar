def encriptar (message, key):
    alfabeto = "abcdefghijklmnopqrstuvwxyz" #pegar o alfabeto
    encriptada = "" #criar uma string vazia para fazer os saltos

    for i in message:
        letra_criptografada = ((ord(i) - ord('a'))+key)%26 #equação para fazer o loop no array do alfabeto
        encriptada += alfabeto[letra_criptografada]
    return encriptada 

message = input("Qual é a sua mensagem? ") #inserção da mensagem a ser encriptada
desloc = int(input("Quantas casas você deseja pular? ")) #inserção da chave de deslocamento
mensagem_encriptada = encriptar(message, desloc) #aqui vai pegar a minha mensagem e a quantidade de saltos que eu quero
print(mensagem_encriptada)
