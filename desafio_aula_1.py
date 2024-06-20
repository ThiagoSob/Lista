print("----------" * 10)
print("\n\n")
print("Para continuar a adicionar produtos e valores digite 1")
print("\n")
print("Para parar de adicionar produtos e valores digite 2")
print("\n\n")
decisao = 0
dados = []
produtos = []
valores = []

print("----------" * 10)
print("\n")

while True:
    print("\n")
    produto = input("Produto: ")
    valor = float(input("Valor: R$ "))
    produtos.append(produto)
    valores.append(valor)
    tupla = (produto, valor)
    dados.append(tupla)
    print("\ny7y")
    decisao = int(input("Voce deseja continuar? "))
    if (decisao == 2):
        break

print("----------" * 10)
print("\n\n")

soma = sum(valores)
print(f"Total de gastos na compra é: R${soma:.2f}")

print("\n")
qmaior = 1000
filtro_valor = [c for c in valores if c > qmaior]

print(f"A quantidade de produtos com valor acima de R$1000,00 é: {len(filtro_valor)}")

print("\n")
menor_valor = min(dados, key = lambda x: x[1])
print(f"O produto de menor valor é: {menor_valor[0]}") 

print("\n\n")
print("----------" * 10)