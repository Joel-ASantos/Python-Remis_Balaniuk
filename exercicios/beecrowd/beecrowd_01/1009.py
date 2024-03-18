nome_vendedor = "João"
salario_fixo = 1500.00
taxa_venda = 0.15
qtd_venda = float(input("digite o total de vendas: "))
bonus = qtd_venda * taxa_venda
montante = salario_fixo + bonus

print("Nome do vendedor: ",nome_vendedor)
print("Salario: R$ %.2f"%salario_fixo)
print("Total Bônus: R$ %.2f"%bonus)
print("Total do salario mais o bônus: R$ %.2f"%montante)