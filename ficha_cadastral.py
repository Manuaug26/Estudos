print("Cadastro de doadores de sangue")
nome = input("Por favor, informe seu nome completo: ")
peso = float(input("Informe seu peso em kg: "))
altura = int(input("Informe a sua altura em cm: "))
ano_nascimento = int(input("Informe a sua data de nascimento: "))

idade = 2026 - ano_nascimento
tem_peso_minimo = peso > 50 
tem_idade_minima = idade >= 16

texto_saida = f"\tNOME: {nome}\n\tPESO: {peso} kg\n\tALTURA: {altura} cm\n\tIDADE: {idade} anos\n\tPOSSUI PESO MINIMO: {tem_peso_minimo}\n\tPOSSUI IDADE MINIMA: {tem_idade_minima}"

print(texto_saida)
