totalpar = 0 
totalimpar = 0
totalnumbers = 0

def paridade():
 global totalpar 
 global totalimpar 
 global totalnumbers
 
 totalnumbers = totalnumbers + 1
 number = int(input("digite um numero:"))
 if number % 2 == 0 :
    totalpar = totalpar + 1
 elif number % 2 == 1:
    totalimpar = totalimpar + 1

def exibetotal():
    print("Total de números digitados:",totalnumbers) 
    print("Total de números pares:",totalpar)        
    print("Total de números ímpares:",totalimpar)     


paridade()
paridade()
paridade()
paridade()
paridade()

exibetotal()


