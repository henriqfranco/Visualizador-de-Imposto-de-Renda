import matplotlib.pyplot as plt
import sys

def calcular_imposto_mensal(salario):
    if salario <= 1903.98:
        return 0
    elif salario >= 1903.99 and salario <= 2826.65:
        return salario * 0.075
    elif salario >= 2826.66 and salario <= 3751.05:
        return salario * 0.15
    elif salario >= 3751.06 and salario <= 4664.68:
        return salario * 0.225
    else:
        return salario * 0.275

if __name__ == "__main__":
    salario = float(sys.argv[1])
    salarios_mensais = range(int(salario) - 5000, int(salario) + 5001, 100)
    impostos = [calcular_imposto_mensal(salario) for salario in salarios_mensais]

    imposto_atual = calcular_imposto_mensal(salario)
    print(f"Para um salário de R${salario:.2f}, o imposto devido é R${imposto_atual:.2f}")

    plt.figure(figsize=(11, 6))
    plt.plot(salarios_mensais, impostos, label='Imposto Devido')
    plt.axvline(salario, color='r', linestyle='--', label=f'Salário R${salario:.2f}')
    plt.axhline(imposto_atual, color='b', linestyle='--', label=f'Imposto R${imposto_atual:.2f}')
    plt.xlabel('Salário Mensal (R$)')
    plt.ylabel('Imposto Mensal (R$)')
    plt.title('Imposto de Renda vs Salário Mensal')
    plt.legend()
    plt.grid(True)
    plt.show()