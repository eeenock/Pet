def calculaduracao():
 hora_inicial = int(input("Insira em qual hora começou o jogo:"))
 minuto_inicial = int(input("Insira em qual minuto começou o jogo:"))
 hora_final = int(input("Insira em qual hora terminou o jogo:"))
 minuto_final = int(input("Insira em qual minuto terminou o jogo:"))

 hora_jogo = hora_final - hora_inicial
 minuto_jogo = minuto_final - minuto_inicial

 if hora_jogo == 0 and minuto_jogo == 0 :
    print("O jogo deve durar mais de 1 minuto!!!")
 else:

   if hora_final > hora_inicial and minuto_inicial > minuto_final :
    hora_jogo = hora_jogo - 1
    minuto_final = minuto_final + 60
    minuto_jogo = minuto_final - minuto_inicial

   if hora_inicial > hora_final and (minuto_inicial < minuto_final or minuto_inicial == minuto_final)  :
    hora_final = hora_final + 24
    hora_jogo = hora_final - hora_inicial
 
   if hora_inicial > hora_final and minuto_inicial > minuto_final  :
    minuto_final = minuto_final + 60
    minuto_jogo = minuto_final - minuto_inicial    
    hora_final = hora_final + 23
    hora_jogo = hora_final - hora_inicial
    
   print("O jogo durou:",hora_jogo,"hr(s) e",minuto_jogo,"minuto(s)")     
     

calculaduracao() 
   