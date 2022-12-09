def calculaSalario(salarioBruto):

    descontoINSS = salarioBruto * 0.11
    salario = salarioBruto-descontoINSS
    descontoIR = salario * 0.15
    salarioLiquido = salario - descontoIR
    print("Salário Bruto:",salarioBruto)
    print("Desconto do INSS:",descontoINSS)
    print("Desconto IR:", descontoIR)
    print("Salário Líquido",salarioLiquido)
    print(salarioBruto,"-",descontoINSS,"-",descontoIR,"=",salarioLiquido)
    
calculaSalario(5000)    