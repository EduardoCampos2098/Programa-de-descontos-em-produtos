#Entrada de dados
valor_total = float(input("Insira o valor da compra para calcularmos possíveis opções de descontos🤑: "))

#Condições
if valor_total <200:
    print("Para essa compra é aplicável o cupom de 5% OFF💸.")
    d = valor_total * 0.05
elif valor_total <300>=200:
    print("Para essa compra é aplicável o cupom de 10% OFF💸.")
    d = valor_total * 0.10
else:
    print("Para essa compra é aplicável o cupom de 15% OFF💸.")
    d = valor_total * 0.15
valor_descontado = (valor_total - d)

#Exibição de dados
print(f"Valor do desconto: {d: .2f} R$.")
print(f"Valor total a ser pago com desconto:{valor_descontado: .2f} R$.")