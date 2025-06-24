from random import randint

A = 65 #ascii_value

def main():
    mensagem = input("Mensagem para criptografar:\n")
    chave = create_key(mensagem)
    criptografada = one_time_pad_encrypt(mensagem, chave)
    print(f"Cript: {criptografada}")
    print(f"Decript: {one_time_decrypt(criptografada, chave)}")

def one_time_pad_encrypt(mensagem, chave):
    encrypt = [((ord(chave[i]) + ord(mensagem[i])) % 26) + A for i in range(len(mensagem))]
    encrypted_mensagem = ""
    for num in encrypt:
        encrypted_mensagem += chr(num)
    return encrypted_mensagem

def one_time_decrypt(criptografada, chave):
    decrypt = [((ord(criptografada[i]) - ord(chave[i])) % 26) + A for i in range(len(criptografada))]
    decrypted_mensagem = ""
    for num in decrypt:
        decrypted_mensagem += chr(num)
    return decrypted_mensagem
    
def create_key(mensagem):
    lista_num = [randint(0, 25) for i in range(len(mensagem))]
    chave = ""
    for num in lista_num:
        chave += chr(A + num)
    return chave
    
main()
