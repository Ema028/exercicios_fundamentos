#calcula quantos dias entre uma data e outra
dias_meses = {"janeiro" : 31, "fevereiro" : 28, "março" : 31, "abril" : 30, "maio" : 31, "junho": 30, "julho" : 31, "agosto" : 31, "setembro" : 30, "outubro" : 31, "novembro" : 30, "dezembro" : 31}

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

def main():
    data1 = input("qual a primeira data?\n")
    data1 = check_data(data1)
    data2 = input("qual a segunda data?\n")
    data2 = check_data(data2)
    
    d1 = int(data1[0])
    d2 = int(data2[0])
    a1 = data1[2]
    a2 = data2[2]
    m1 = data1[1]
    m2 = data2[1]
    
    a1 = check_ano(int(a1))
    a2 = check_ano(int(a2))
    
    m1 = check_meses(m1)
    m2 = check_meses(m2)
    
    dias = 0
    if(a2 > a1):
        dias  += (a2 - a1 - 1) * 365
        for i in range(a1 + 1, a2):
            if(i % 4 == 0):
                dias += 1
            
    index = m1 - 1
    while((index % 12) != (m2 - 1)):
        if(index < 11 and a1 % 4 == 0):
            dias_meses["fevereiro"] = 29
        elif(index > 11 and a2 % 4 == 0):
            dias_meses["fevereiro"] = 29
        else:
            dias_meses["fevereiro"] = 28
        dias += dias_meses[meses[index % 12]]
        index += 1
        
    dias = dias - d1 + 1
    dias += d2
    
    print(f"há {dias} dias entre eles")
    
def check_data(data):
    if '\\' in data:
        return data.split('\\')
    elif 'de' in data:
        return data.split('de')
    else:
        return data.split()
        
def check_ano(ano):
    if(ano < 100):
        if (ano > 30):
            return ano + 2000
        else:
            return ano + 1900
    else:
        return ano
            
def check_meses(mes):
    mes = mes.strip().lower()
    for i in range(len(meses)):
        if (mes == meses[i]):
            return i + 1
    return int(mes)
 
if _name_ == '_main_':   
    main()
