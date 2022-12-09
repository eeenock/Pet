idades = []
contaNegativo = 0

while contaNegativo == 0: 
    idadedigitada = int(input("Informe a idade do indivíduo:"))
    if idadedigitada >= 0:
     idades.append(idadedigitada)
    
    else :
     contaNegativo = 1
     total = 0
     
     for i in range(len(idades)) :
      total = total + idades[i]

   

print(idades)
print("total:",total,"Média:",total/len(idades))