class Exp:
    def __init__(self, numero, expoente):
        self.numero = numero
        self.expoente = expoente

    @property
    def expo(self):
        self.num_exp = "{}^{}".format(self.numero, self.expoente)
        num = self.num_exp.strip('"')
        return self.num_exp

def iniciar():
    vezes = 0
    repete = False
    divisores = []
    certo = False

    print("         FATORADOR DE NUMEROS \nApenas para números menores que 11 dígitos \n")
    while not certo:
        numero_ori = input("Digite o número que queres fatorar:").strip()
        if numero_ori.isdigit():
            certo = True
        else:
            print("Digite apenas números positivos \n")

    numero = int(numero_ori)
    divisor = 2

    while numero != 1:
        repete = False
        if numero % divisor == 0:
            numero = numero / divisor
            vezes += 1
            repete = True
            if vezes == 1 and numero % divisor != 0:
                divisor = str(divisor)
                divisores.append(divisor)
                divisor = int(divisor)
                divisor += 1
                vezes = 0
                continue
        if vezes >= 2 and numero % divisor != 0:
                ex = Exp(divisor, vezes)
                divisores.append(ex.expo)
                divisor += 1
                vezes = 0
                continue
        if not repete:
            divisor += 1

    divisores = ", ".join(divisores)
    print("Esta é a lista de divisores do número {}: \n{} \n".format(numero_ori, divisores), )
    print("Queres fatorar outro número? \n")
    confirma = input("S para sim, N para não: \n").upper()
    if confirma == "S":
        iniciar()


iniciar()
