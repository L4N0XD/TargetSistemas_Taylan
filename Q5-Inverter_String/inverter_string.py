string = input("Digite uma string para ser invertida: ")
string_invertida = ""

for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

print("String invertida:", string_invertida)