# %%
print("SISTEMA DE ANÁLISE DE CRÉDITO")
print("Coloque as informações pedidas abaixo.")

# %%
score = int(input("Digite o seu score (0 a 1000): "))
print("Seu score é de: ", score)
tempcont = float(input("Digite o tempo da conta corrente (Ex: 0.6 para 6 meses, 1 para 1 ano): "))
print("Seu tempo de conta corrente é: ", tempcont)
temptra = float(input("Digite o tempo de trabalho (Ex: 0.6 para 6 meses, 1 para 1 ano): "))
print("Seu tempo de trabalho é: ", temptra)
renda = int(input("Digite sua renda mensal: "))
print("Sua renda mensal é: ", renda)



# %%
if score >= 1000:
    print("Você foi aprovado para a próxima etapa.")
elif score <= 700:
    print("Você passou para a próxima etapa, contanto que nos dê algo como garantia do empréstimo.")

# %%
if tempcont >= 1:
    print("Você foi aprovado para a próxima etapa.")
else:
    print("Tempo de conta inválido.")

# %%
if temptra >= 0.6:
    print("Você foi aprovado para a próxima etapa.")
elif temptra <= 0.6:
    print("Você passou para a próxima etapa, contanto que nos dê algo como garantia do empréstimo.")

# %%
if renda >= 1500:
    print("Você poderá pegar um empréstimo de até 1000 reais.")
elif renda <= 1000:
    print("Você poderá pegar um empréstimo de até 500 reais, nos dando algo de garantia que irá nos pagar.")


