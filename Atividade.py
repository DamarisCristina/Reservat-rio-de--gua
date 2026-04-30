# Atividade DS - Níveis de um reservatório

# O programa solicita ao usuário a quantidade de litros em um reservatório e classifica o nível de água com base em faixas predefinidas, utilizando cores para destacar a situação.
diga = float(input("Nos informe quantos litros possui o reservatório: "))

# Definição dos níveis e suas respectivas faixas
niveis = ["Nível 1", "Nível 2", "Nível 3", "Nível 4", "Nível 5"]

# Função para determinar a cor, número do nível e situação com base na quantidade de litros1!

from colorama import Fore, Style

# Função para determinar a cor, número do nível e situação com base na quantidade de litros
def definir_cor(litros):
    if litros <= 20:
        return Fore.RED, niveis[0], "Muito baixo (crítico)"
    elif litros <= 40:
        return Fore.YELLOW, niveis[1], "Baixo"
    elif litros <= 60:
        return Fore.GREEN, niveis[2], "Médio"
    elif litros <= 80:
        return Fore.CYAN, niveis[3], "Alto"
    else:
        return Fore.BLUE, niveis[4], "Muito alto (alerta)"
    

# Cor, número do nível e situação = definir_cor(diga) - Chama a função para obter a cor, número do nível e situação com base na quantidade de litros fornecida pelo usuário
cor, nivel_numero, situacao = definir_cor(diga)

# Exibe resultado!!!
print(cor + f"A situação atual do reservatório é {nivel_numero} - {situacao}" + Style.RESET_ALL)