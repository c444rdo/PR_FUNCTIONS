print("Martínez Estrada Ricardo")
print(" ")

# Parámetros o Argumentos
# Los términos parámetro y argumento pueden usarse para referirse a lo mismo: información que se pasa a una función.

# Desde la perspectiva de una función:
# Un parámetro es la variable listada dentro de los paréntesis en la definición de la función.
# Un argumento es el valor que se envía a la función cuando se llama.

# Número de Argumentos
# Por defecto, una función debe ser llamada con el número correcto de argumentos. 
# Esto significa que si tu función espera 2 argumentos, debes llamarla con 2 argumentos, ni más, ni menos.
def mi_funcion(nombre, apellido):
    print(nombre + " " + apellido)

mi_funcion("Emil", "Refsnes")
print(" ")

# Si intentas llamar a la función con 1 o 3 argumentos, obtendrás un error.
# Ejemplo: esta función espera 2 argumentos, pero recibe solo 1.
def mi_funcion(nombre, apellido):
    print(nombre + " " + apellido)

# mi_funcion("Emil")  # Esto generará un error.
print(" ")

# Argumentos Arbitrarios, *args
# Si no sabes cuántos argumentos se pasarán a tu función, agrega un * antes del nombre del parámetro en la definición de la función.
def mi_funcion(*niños):
    print("El hijo menor es " + niños[2])

mi_funcion("Emil", "Tobias", "Linus")
print(" ")

# Los argumentos arbitrarios a menudo se acortan a *args en la documentación de Python.

# Argumentos de Palabra Clave
# También puedes enviar argumentos con la sintaxis key = value.
# De esta manera, el orden de los argumentos no importa.
def mi_funcion(hijo3, hijo2, hijo1):
    print("El hijo menor es " + hijo3)

mi_funcion(hijo1="Emil", hijo2="Tobias", hijo3="Linus")
print(" ")

# La frase Argumentos de Palabra Clave se acorta a kwargs en la documentación de Python.

# Argumentos Arbitrarios de Palabra Clave, **kwargs
# Si no sabes cuántos argumentos de palabra clave se pasarán a tu función, agrega dos asteriscos: ** antes del nombre del parámetro en la definición de la función.
def mi_funcion(**niño):
    print("Su apellido es " + niño["apellido"])

mi_funcion(nombre="Tobias", apellido="Refsnes")
print(" ")

# Los Argumentos Arbitrarios de Palabra Clave a menudo se acortan a **kwargs en la documentación de Python.

# Valor de Parámetro Predeterminado
# El siguiente ejemplo muestra cómo usar un valor de parámetro predeterminado.
def mi_funcion(pais="Noruega"):
    print("Soy de " + pais)

mi_funcion("Suecia")
mi_funcion("India")
mi_funcion()
mi_funcion("Brasil")
print(" ")

# Pasar una Lista como Argumento
# Puedes enviar cualquier tipo de datos como argumento a una función (cadena, número, lista, diccionario, etc.), y se tratará como el mismo tipo de datos dentro de la función.
def mi_funcion(comida):
    for x in comida:
        print(x)

frutas = ["manzana", "banana", "cereza"]
mi_funcion(frutas)
print(" ")

# Valores de Retorno
# Para permitir que una función devuelva un valor, usa la sentencia return.
def mi_funcion(x):
    return 5 * x

print(mi_funcion(3))
print(mi_funcion(5))
print(mi_funcion(9))
print(" ")

# La sentencia pass
# Las definiciones de funciones no pueden estar vacías, pero si por alguna razón tienes una definición de función sin contenido, usa la sentencia pass para evitar un error.
def mi_funcion():
    pass

# Argumentos solo posicionales
# Puedes especificar que una función solo puede tener argumentos posicionales, o solo argumentos de palabra clave.
# Para especificar que una función solo puede tener argumentos posicionales, agrega , / después de los argumentos.
def mi_funcion(x, /):
    print(x)

mi_funcion(3)
print(" ")

# Sin el , / puedes usar argumentos de palabra clave incluso si la función espera argumentos posicionales.
def mi_funcion(x):
    print(x)

mi_funcion(x=3)
print(" ")

# Sin embargo, al agregar el , / obtendrás un error si intentas enviar un argumento de palabra clave.
def mi_funcion(x, /):
    print(x)

# mi_funcion(x=3)  # Esto generará un error.
print(" ")

# Argumentos Solo de Palabra Clave
# Para especificar que una función solo puede tener argumentos de palabra clave, agrega *, antes de los argumentos.
def mi_funcion(*, x):
    print(x)

mi_funcion(x=3)
print(" ")

# Sin el *, puedes usar argumentos posicionales incluso si la función espera argumentos de palabra clave.
def mi_funcion(x):
    print(x)

mi_funcion(3)
print(" ")

# Pero al agregar el *, obtendrás un error si intentas enviar un argumento posicional.
def mi_funcion(*, x):
    print(x)

# mi_funcion(3)  # Esto generará un error.
print(" ")

# Combinar Argumentos Solo Posicionales y Solo de Palabra Clave
# Puedes combinar los dos tipos de argumentos en la misma función.
def mi_funcion(a, b, /, *, c, d):
    print(a + b + c + d)

mi_funcion(5, 6, c=7, d=8)
print(" ")

# Recursión
# Python también acepta la recursión de funciones, lo que significa que una función definida puede llamarse a sí misma.
# La recursión es un concepto común en matemáticas y programación. Significa que una función se llama a sí misma.
def tri_recursion(k):
    if k > 0:
        resultado = k + tri_recursion(k - 1)
        print(resultado)
    else:
        resultado = 0
    return resultado

print("\n\nResultados del Ejemplo de Recursión")
tri_recursion(6)