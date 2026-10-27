
def calculadora():
    while True:
        print("\n" + "=" * 40)
        print("       CALCULADORA EM PYTHON")
        print("=" * 40)
        print("1 - Adição (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        print("0 - Sair")
        print("-" * 40)

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Programa encerrado.")
            break

        if opcao not in ("1", "2", "3", "4"):
            print("Opção inválida!")
            continue

        try:
            numero1 = float(
                input("Primeiro número: ").replace(",", ".")
            )
            numero2 = float(
                input("Segundo número: ").replace(",", ".")
            )
        except ValueError:
            print("Erro: digite números válidos.")
            continue

        if opcao == "1":
            resultado = numero1 + numero2
            simbolo = "+"
        elif opcao == "2":
            resultado = numero1 - numero2
            simbolo = "-"
        elif opcao == "3":
            resultado = numero1 * numero2
            simbolo = "*"
        else:
            if numero2 == 0:
                print("Erro: divisão por zero não é permitida.")
                continue

            resultado = numero1 / numero2
            simbolo = "/"

        print(
            f"\nResultado: {numero1} {simbolo} "
            f"{numero2} = {resultado}"
        )


if __name__ == "__main__":
    calculadora()

