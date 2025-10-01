def verificar_palindromo(palavra):
    if len(palavra) <= 1:
        return True
    else:
        return palavra[0] == palavra[-1] and verificar_palindromo(palavra[1:-1])
print(verificar_palindromo("radar"))
print(verificar_palindromo("python"))