def desenhar_triangulo(n, atual=1):
    if atual > n:
        return
    else:
        print('*' * atual)
        desenhar_triangulo(n, atual + 1)
desenhar_triangulo(3)