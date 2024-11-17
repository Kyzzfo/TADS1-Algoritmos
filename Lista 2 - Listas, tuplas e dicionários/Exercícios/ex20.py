print("====== Exercício 20 ======\nSequência de Fibonacci\n")

def valida(num):
    try:
        if int(num)>0:
            return int(num)
        else:
            print("O número deve ser maior do que 0")
            return None
    except ValueError:
        print(" Esse valor é inválido")
        return None

def fibonacci(numf):
    num1, num2 = 0, 1
    for i in range (numf):
        print(f"{i} : {num1}")
        num1, num2 = num2, num1 + num2
        
while True:
    nums = input("Digite um número X e lhe serão mostrados os X primeiros números da sequência de Fibonacci: ")
    if valida(nums) is not None:
        numi = valida(nums)
        print(f"Certo, lhe mostrarei os {numi} primeiros números da sequência de Fibonacci a seguir")
        break
    
fibonacci(numi)
    
print("Final do programa")