def fibonacci(n):
    # Retorna o n-ésimo número da sequência de Fibonacci
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# lê o número informado pelo usuário
num = int(input("Informe um número: "))

# verifica se o número pertence à sequência de Fibonacci
pertence = False
i = 0
while (fibonacci(i) <= num):
    if (fibonacci(i) == num):
        pertence = True
        break
    i += 1

# exibe a sequência de Fibonacci até o número informado
seq_fibonacci = [fibonacci(u) for u in range(i+1)]
print(f"Sequência de Fibonacci até {num}: {seq_fibonacci}")

# exibe a mensagem se o número pertence ou não à sequência
if (pertence):
    print(f"{num} pertence à sequência de Fibonacci!")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")