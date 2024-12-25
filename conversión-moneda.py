# Paso 1: Definir el valor actual del Euro y Dolar con respecto a Peso Mexicano:

tipo_cambio_eur_mxn = 23.70  # Nota: En un caso realista  habría que consumir información actualizada de una BDD O API.
tipo_cambio_usd_mxn = 20.75  # Nota: En un caso realista  habría que consumir información actualizada de una BDD O API.

# Paso 2: Solicitar al usuario el tipo de conversión. (euro a mex o dolar a mex)

tipo_conversion = input("Ingrese la moneda de origen para la conversión (EUR/USD): ")


# Paso 3: Solicitar al usuario el monto a convertir

monto_a_convertir = float(input("Ingrese el monto a convertir: "))


# Paso 4: Realizar la conversión  utilizando  el tipo de cambio  correspondiente
# Paso 5: Mostrar el resultado  de la conversión  al usuario

if tipo_conversion.upper() == "EUR":
    resultado = monto_a_convertir * tipo_cambio_eur_mxn
    print("El resultado de la conversion de EUR a MXN es: ", resultado)
elif tipo_conversion.upper() == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_mxn
    print("El resultado de la conversion de USD a MXN es: ", resultado)
else:
    print("No está disponible este tipo de conversión actualmente")



