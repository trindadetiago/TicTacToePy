quadro = ({"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "})
vez = "X"
zev = "O"
acabou = False
vencedor = " "
def desenharquadro():

    print(quadro['7'] + "|" + quadro['8'] + "|" + quadro['9'])
    print("-+-+-")
    print(quadro['4'] + "|" + quadro['5'] + "|" + quadro['6'])
    print("-+-+-")
    print(quadro['1'] + "|" + quadro['2'] + "|" + quadro['3'])


def checar_se_possivel(pos):
    if not pos.isdigit():
        print("Digite um número!")
        return False
    elif int(pos) < 1 or int(pos) > 9:
        print("Jogada impossivel! Jogue entre 1 e 9")
        return False
    elif quadro[str(pos)] != " ":
        print("Lugar já tomado! Escolha outro")
        return False
    elif 0 < int(pos) < 10:
        return True
    else:
        print("Digite a posição desejada")
        return False

def perguntar(vez):
    pos = input("Vez do jogador " + vez + ", onde irá jogar?")
    if checar_se_possivel(pos) == False:
        perguntar(vez)
    else:
        quadro[pos] = vez
        if vez != "X":
            return "X"
        elif vez != "O":
            return "O"
        else:
            return vez

def check_horiazontal():
    if (quadro["1"] != " " and quadro["1"] == quadro["2"] == quadro["3"]) or (quadro["4"] != " " and quadro["4"] == quadro["5"] == quadro["6"]) or (quadro["7"] != " " and quadro["7"] == quadro["8"] == quadro["9"]):
        if vez == "X":
            return "O"
        elif vez == "O":
            return "X"
    else:
        return False

def check_vertical():
    if (quadro["1"] != " " and quadro["1"] == quadro["4"] == quadro["7"]) or (quadro["2"] != " " and quadro["2"] == quadro["5"] == quadro["8"]) or (quadro["3"] != " " and quadro["3"] == quadro["6"] == quadro["9"]):
        if vez == "X":
            return "O"
        elif vez == "O":
            return "X"
    else:
        return False

def check_diagonal():
    if (quadro["1"] != " " and quadro["1"] == quadro["5"] == quadro["9"]) or (quadro["7"] != " " and quadro["7"] == quadro["5"] == quadro["3"]):
        if vez == "X":
            return "O"
        elif vez == "O":
            return "X"
    else:
        return False

def checar_vencedor():
    if check_horiazontal() != False:
        return check_horiazontal()
    if check_vertical() != False:
        return check_vertical()
    if check_diagonal() != False:
        return check_diagonal()
    return " "

def checar_velha():
    a = 0
    for q in quadro:
        if quadro[q] != " ":
            a += 1
    if a == 9:
        return True

def recom():
    res = input("Gostaria de recomeçar? sim/nao")
    if res == "sim" or res == "s" or res == "0":
        return True

while not acabou:
    desenharquadro()
    if str(vez) != "None":
        zev = vez
        vez = perguntar(str(vez))
    else:
        if zev == "X": vez = "O"
        if zev == "O": vez = "X"

    if checar_vencedor() != " ":
        desenharquadro()
        vencedor = checar_vencedor()
        print("Parabens " + vencedor + " voce venceu!")
        acabou = True
        if recom() == True:
            for q in quadro:
                quadro[q] = " "
                vez = "X"
                acabou = False
                vencedor = " "
    if checar_velha():
        print("Velha! Ninguem venceu essa")
        acabou = True
        if recom() == True:
            for q in quadro:
                quadro[q] = " "
                vez = "X"
                acabou = False
                vencedor = " "