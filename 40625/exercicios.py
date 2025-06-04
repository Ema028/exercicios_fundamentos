#1
def main( ):
    while True:
        try:
            text = input("diga um dizer:\n")
            if(text.isalpha() == False):
                raise
            break
        except:
            print("inválido")
    text = to_upper(text)
    print(text)
    
def to_upper(string):
    return(string.upper())
    
main()
#2
def main():
    print("vamos popular a lista 1")
    nums1 = []
    populate_list(nums1)
    print("agora a lista 2")
    nums2 = []
    populate_list(nums2)
    print(f" lista 1: {nums1}\n lista 2: {nums2}\n soma: {soma_list(nums1, nums2)}")
    
def soma_list(lista1, lista2):
    soma = 0
    for numero in lista1:
        soma += numero
    for numero in lista2:
        soma += numero
    return soma
    
def populate_list(lista):
    while True:
        num = get_int()
        if (num == 0):
            break
        lista.append(num)
        print("adicionado")
    
def get_int():
    while True:
        try:
            num = int(input("diga um número, 0 para parar:\n"))
            break
        except:
            print("inválido")
    return num
    
main()
