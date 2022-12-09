
total = 0


contaPrestacao = 0

def relatorioDia():
    print("***********RELATÓRIO DO DIA***********")
    print("Total recebido no dia:",total)
    print("Total de prestações pagas no dia:",contaPrestacao)

def valorPagamento(valorPrestacao,diasAtraso):
    valorPrestacao = int(valorPrestacao)
    diasAtraso = int(diasAtraso)  

    if diasAtraso > 0 and valorPrestacao != 0  :
        i=0
        valorPrestacao = valorPrestacao + (valorPrestacao * 0.03) 
        while i != diasAtraso:
         valorPrestacao = valorPrestacao + (valorPrestacao * 0.001)
         i= i + 1
    
    global total
    total = total + valorPrestacao
    global contaPrestacao
    if valorPrestacao != 0 :
     contaPrestacao = contaPrestacao + 1 

    return valorPrestacao     

def pagaPrestacao():
 i = 0   
 while i == 0:
  global valor
  global dias 

  valor = input("Informe o Valor da Prestação:")
  dias = input("Informe os Dias de Atraso:")
  valorPagar = valorPagamento(valor,dias)
  if valorPagar > 0: 
   print("Valor a ser pago:",valorPagar)
  if valorPagar == 0:
    relatorioDia()
    i=i+1 


pagaPrestacao()  