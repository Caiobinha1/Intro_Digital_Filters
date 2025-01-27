# Este codigo gera os coeficientes necessarios para os filtros simples
import numpy as np
import pylab

def hamming_window(i, valor):
    return 0.54 - 0.46 * np.cos(2 * np.pi * i / (valor - 1))

def sinc_function(fc, i, valor):
    if (i - (valor - 1) / 2) == 0:
        return 2 * np.pi * fc
    else:
        return (np.sin(2 * np.pi * fc * (i - (valor - 1) / 2))) / (i - (valor - 1) / 2)

def normalize(data, soma):
    return [x / soma for x in data]

def write_to_file(filename, data):
    with open(filename, "w") as coeficientes:
        for i in data:
            coeficientes.write("{:.12f}\n".format(i))

def plot_data(data):
    pylab.plot(data)
    pylab.show()

def passa_faixa(valor, FC, FC2):
    dadosalto = []
    dadosbaixo = []
    faixa = []
    soma = 0
    soma2 = 0

    for i in range(valor):
        dadosalto.append(sinc_function(FC, i, valor) * hamming_window(i, valor))
        dadosbaixo.append(sinc_function(FC2, i, valor) * hamming_window(i, valor))
        soma += dadosalto[i]
        soma2 += dadosbaixo[i]

    dadosalto = normalize(dadosalto, soma)
    dadosbaixo = normalize(dadosbaixo, soma2)

    for i in range(valor):
        dadosalto[i] = -dadosalto[i]
    dadosalto[int(valor / 2)] += 1

    for i in range(valor):
        faixa.append(-1 * (dadosalto[i] + dadosbaixo[i]))
    faixa[int(valor / 2)] += 1

    write_to_file("input\\coeficientesPF.txt", faixa)
    plot_data(faixa)
    return faixa

def rejeita_faixa(valor, FC, FC2):
    dadosalto = []
    dadosbaixo = []
    faixa = []
    soma = 0
    soma2 = 0

    for i in range(valor):
        dadosalto.append(sinc_function(FC, i, valor) * hamming_window(i, valor))
        dadosbaixo.append(sinc_function(FC2, i, valor) * hamming_window(i, valor))
        soma += dadosalto[i]
        soma2 += dadosbaixo[i]

    dadosalto = normalize(dadosalto, soma)
    dadosbaixo = normalize(dadosbaixo, soma2)

    for i in range(valor):
        dadosalto[i] = -dadosalto[i]
    dadosalto[int(valor / 2)] += 1

    for i in range(valor):
        faixa.append(dadosalto[i] + dadosbaixo[i])

    write_to_file("input\\coeficientesRF.txt", faixa)
    plot_data(faixa)

def passa_baixo(valor, FC):
    dadosbaixo = []
    soma = 0

    for i in range(valor):
        dadosbaixo.append(sinc_function(FC, i, valor) * hamming_window(i, valor))
        soma += dadosbaixo[i]

    dadosbaixo = normalize(dadosbaixo, soma)

    write_to_file("input\\coeficientesPB.txt", dadosbaixo)
    plot_data(dadosbaixo)
    return dadosbaixo

def passa_alto(valor, FC):
    dadosalto = []
    soma = 0

    for i in range(valor):
        dadosalto.append(sinc_function(FC, i, valor) * hamming_window(i, valor))
        soma += dadosalto[i]

    dadosalto = normalize(dadosalto, soma)

    for i in range(valor):
        dadosalto[i] = -dadosalto[i]
    dadosalto[int(valor / 2)] += 1

    write_to_file("input\\coeficientesPA.txt", dadosalto)
    plot_data(dadosalto)
    return dadosalto

def main():
    escolha = int(input("1-passa baixo\n2-Passa alto\n3-Passa Faixa\n4-Rejeita Faixa\n"))
    valor = int(input("Insira o numero de coef: "))
    FS = int(input("Insira a frequencia do audio: "))

    if valor % 2 == 0:
        print("Valor escolhido e par, logo nao tera uma precisao muito grande. ")

    FCorte = int(input('Insira a frequencia de corte baixo desejada: '))
    FC = FCorte / FS

    if escolha in [3, 4]:
        FCorte2 = int(input('Insira a frequencia de corte alto desejada: '))
        FC2 = FCorte2 / FS

    actions = {
        1: lambda: passa_baixo(valor, FC),
        2: lambda: passa_alto(valor, FC),
        3: lambda: passa_faixa(valor, FC, FC2),
        4: lambda: rejeita_faixa(valor, FC, FC2)
    }

    if escolha in actions:
        if escolha == 4 and FCorte2 > FCorte:
            print("Erro frequencia de corte baixo menor que frequencia de corte alto!")
        else:
            actions[escolha]()
    else:
        print('Escolha invalida')

if __name__ == "__main__":
    main()