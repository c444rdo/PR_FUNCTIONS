print("Martínez Estrada Ricardo")
print(" ")

def suma_recursiva(k):
    if k > 0:
        resultado = k + suma_recursiva(k - 1)
        print(resultado)
    else:
        resultado = 0
    return resultado

print("\nResultados de Ejemplo de Recursión")
suma_recursiva(6)
