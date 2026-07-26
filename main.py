while True:
 num1 = float(input("Digite o primeiro número: "))
 operacao = input("Digite a operação (+, -, *, /): ")
 num2 = float(input("Digite o segundo número: "))
 if operacao == "+":
   print (num1, "+", num2, "=", num1 + num2)
 elif operacao == "-":
    print (num1, "-", num2, "=", num1 - num2)
 elif operacao == "*":
    print (num1, "*", num2, "=", num1 * num2)
 elif operacao == "/":
   if num2 == 0:
     print ("Não é possivel dividir por zero.")
   else: 
    print (num1, "/", num2, "=", num1 / num2)
 continuar = input ("Deseja fazer outra conta? (s/n): ")
 if continuar == "n":
    break 
print ("Tenha um bom dia (: ")
