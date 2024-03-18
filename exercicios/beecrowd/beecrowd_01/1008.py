numero = int(input("numero do funcionario: "))
horas_trabalhadas = int(input("horas trabalhadas: "))
ganho_hora = float(input("ganho por hora: "))
salario = (horas_trabalhadas * ganho_hora)

print("numero do trabalhador: ",numero)
print("Salario: R$ %.2f"%(salario))