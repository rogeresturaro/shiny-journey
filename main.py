## 📄 main.py
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b


if __name__ == "__main__":
    print("Calculadora")
    print("2 + 3 =", soma(2, 3))
    print("10 - 4 =", subtracao(10, 4))
    print("6 * 7 =", multiplicacao(6, 7))
    print("8 / 2 =", divisao(8, 2))
