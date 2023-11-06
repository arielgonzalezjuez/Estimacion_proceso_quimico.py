# Definici�n de reglas
def estimar_proceso_quimico(parametro1, parametro2):
    if parametro1 > 5 and parametro2 < 10:
        return "Proceso qu�mico probablemente eficiente."
    elif parametro1 <= 5 and parametro2 >= 10:
        return "Proceso qu�mico probablemente ineficiente."
    else:
        return "No se puede determinar la eficiencia del proceso qu�mico con los datos proporcionados."

# Datos de entrada
parametro1 = float(input("Ingrese el valor del primer par�metro: "))
parametro2 = float(input("Ingrese el valor del segundo par�metro: "))

# Estimaci�n del proceso qu�mico
resultado = estimar_proceso_quimico(parametro1, parametro2)
print(resultado)
