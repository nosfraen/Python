def calcular(num1, num2, operacion):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multi":
        return num1 * num2
    elif operacion == "div":
        if num2 == 0:
                return "No se puede dividir entre 0"
        return num1 / num2
    else:
        return "Operación no válida"


def main():
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))
    operacion = input("Operación (suma, resta, multi, div):").strip().lower()
    print("Resultado:", calcular(num1, num2, operacion))

if __name__ == "__main__":
    main()