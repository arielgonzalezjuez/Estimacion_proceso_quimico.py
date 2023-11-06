# Definición de reglas
def estimar_proceso_quimico(parametro1, parametro2):
    if parametro1 > 5 and parametro2 < 10:
        return "Proceso químico probablemente eficiente."
    elif parametro1 <= 5 and parametro2 >= 10:
        return "Proceso químico probablemente ineficiente."
    else:
        return "No se puede determinar la eficiencia del proceso químico con los datos proporcionados."

# Datos de entrada
parametro1 = float(input("Ingrese el valor del primer parámetro: "))
parametro2 = float(input("Ingrese el valor del segundo parámetro: "))

# Estimación del proceso químico
resultado = estimar_proceso_quimico(parametro1, parametro2)
print(resultado)
