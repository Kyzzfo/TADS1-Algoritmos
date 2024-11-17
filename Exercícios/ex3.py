print("====== Exercício 3 ======\nConversor de graus Celsius para graus Fahrenheit\n")

def convert(grau):
    try:
        fahr = float(grau)*1.8 + 32
        
        return fahr
    except ValueError:
        print(" Esse número não é válido.")
        return None

while True:
    cels = (input("Digite a temperatura em ºC para realizarmos a conversão para ºF: ")).strip()
    if convert(cels) is not None:
        fahr = convert(cels)
        break

print(f"A temperatura de {cels}ºC é equivalente a {fahr}ºF")

print("Final do programa")