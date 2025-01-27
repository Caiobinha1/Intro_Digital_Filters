import numpy as np
import struct
import os

# Define diretórios fixos, ter certeza que o terminal esta na pasta correta
INPUT_DIR = "input"
OUTPUT_DIR = "output"

# Função para carregar os coeficientes de acordo com o filtro selecionado
def carregar_coeficientes():
    opcoes = {
        1: "coeficientesPB.txt",
        2: "coeficientesPA.txt",
        3: "coeficientesPF.txt",
        4: "coeficientesRF.txt"
    }

    print("Escolha o tipo de filtro a ser aplicado:")
    print("1 - Passa-baixo")
    print("2 - Passa-alto")
    print("3 - Passa-faixa")
    print("4 - Rejeita-faixa")

    escolha = int(input("Digite o número da sua escolha: "))

    if escolha not in opcoes:
        raise ValueError("Escolha inválida! Por favor, selecione um número entre 1 e 4.")

    arquivo_coef = opcoes[escolha]
    caminho_coef = os.path.join(INPUT_DIR, arquivo_coef)

    if not os.path.exists(caminho_coef):
        raise FileNotFoundError(f"Arquivo de coeficientes '{arquivo_coef}' não encontrado em '{INPUT_DIR}'.")

    with open(caminho_coef, "r") as f:
        coeficientes = [float(linha.strip()) for linha in f]

    return np.array(coeficientes)

# Função para aplicar os coeficientes a um arquivo .pcm
def aplicar_filtro(input_file, output_file, coeficientes, bits):
    # Determina o formato dos dados com base na profundidade de bits
    formato = "h" if bits == 16 else "i"
    tamanho_amostra = 2 if bits == 16 else 4

    caminho_input = os.path.join(INPUT_DIR, input_file)
    caminho_output = os.path.join(OUTPUT_DIR, output_file)

    if not os.path.exists(caminho_input):
        raise FileNotFoundError(f"Arquivo de entrada '{input_file}' não encontrado em '{INPUT_DIR}'.")

    with open(caminho_input, "rb") as arquivo_entrada:
        audio = arquivo_entrada.read()

    # Converte bytes para array de amostras
    amostras = np.array(struct.unpack(f"{len(audio)//tamanho_amostra}{formato}", audio))

    # Aplica o filtro usando convolução
    amostras_filtradas = np.convolve(amostras, coeficientes, mode="same").astype(np.int32)

    # Clipa os valores para evitar estouro ao salvar
    max_valor = 2**(bits - 1) - 1
    min_valor = -2**(bits - 1)
    amostras_filtradas = np.clip(amostras_filtradas, min_valor, max_valor).astype(formato)

    # Converte array filtrado de volta para bytes
    audio_filtrado = struct.pack(f"{len(amostras_filtradas)}{formato}", *amostras_filtradas)

    # Salva o áudio filtrado
    with open(caminho_output, "wb") as arquivo_saida:
        arquivo_saida.write(audio_filtrado)

    print(f"Arquivo filtrado salvo em: {caminho_output}")

# Programa principal
if __name__ == "__main__":
    # Carrega coeficientes
    coeficientes = carregar_coeficientes()

    # Solicita parâmetros ao usuário
    input_file = input("Digite o nome do arquivo de áudio (.pcm) a ser processado (ex: input.pcm): ")
    output_file = input("Digite o nome do arquivo de saída (.pcm) (ex: output.pcm): ")
    bits = int(input("Digite a profundidade de bits (16 ou 32): "))

    if bits not in [16, 32]:
        raise ValueError("Profundidade de bits inválida! Escolha 16 ou 32.")

    aplicar_filtro(input_file, output_file, coeficientes, bits)
