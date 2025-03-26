age = int(input("Qual a sua idade?\n"))
if age <= 0:
    print("Você não existe")
elif age <= 3:
    print("Você é um bêbê")
elif age <= 11:
    print("Você é uma criança")
elif age <= 17:
    print("Você é um adolescente")
elif age <= 30:
    print("Você é um jovem")
elif age <= 64:
    print("Você é um adulto")
else:
    print("Você é um idoso")
        
