# Función para validar los caracteres permitidos de cada base
def validar_caracteres(num_str, base):
    num_str = num_str.lower()  #Con esto aceptamos que el cliente ingrese minusculas o mayusculas
    if base == 2:
        permitidos = '01'
    elif base == 8:
        permitidos = '01234567'
    elif base == 10:
        permitidos = '0123456789'
    elif base == 16:
        permitidos = '0123456789abcdef'
    else:
        return False
# Bucle que recorre el numero ingresado y revisa que los caracteres correspondan a la base origen seleccionada
# Duvuelve un False si no esta permitido y True si esta todo ok con los caracteres
# Este booleano se va a utilizar en el bucle while de la linea 129 cuando valide si los caracteres ingresados estan incluidos en la base correspondiente
    for caracteres in num_str:
        if caracteres not in permitidos:
            return False
    return True


def decimal_a_binario(decimal):
    binario = ''
    if decimal == 0:
        return '0'
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2 
    return binario

def decimal_a_octal(decimal):
    octal = ''
    if decimal == 0:
        return '0'
    while decimal > 0:
        residuo = decimal % 8 
        octal = str(residuo) + octal
        decimal = decimal // 8
    return octal

def decimal_a_hex(decimal):
    hexadecimal = ''
    digitos_hex = '0123456789ABCDEF' #cadena de valores . Indices del 0 al 15
    
    if decimal == 0:
        return '0'
    
    while decimal > 0:
        residuo = decimal % 16 #me da el indice entre 0 y 15
        hexadecimal = digitos_hex[residuo] + hexadecimal #uso el indice del residuo y recorro la cadena

        decimal = decimal // 16
    
    return hexadecimal.upper()

def decimal_a_decimal(decimal):
    return str(decimal)

# Diccionario de las funciones a la que se va a convertir

funciones_conversion = {
    2: decimal_a_binario,
    8: decimal_a_octal,
    10: decimal_a_decimal,
    16: decimal_a_hex

}

# Diccionario del menu con su base correspondiente. Dos elementos (menu + base)

tipos_conversion = {
    '1': ('Decimal', 10),
    '2': ('Binario', 2),
    '3': ('Octal', 8),
    '4': ('Hexadecimal', 16)
}

opcion_exit = '5'

# Bucle principal del conversor

while True:
    print("\nMenu Principal:")
    print("1. Decimal")
    print("2. Binario")
    print("3. Octal")
    print("4. Hexadecimal")
    print("5. Salir")
    menu_opciones = input("Elegi el tipo de numero origen (1-5): ")
    
    # Salida del sistema con la opcion 5
    if menu_opciones == opcion_exit:
        print("Gracias, vuelva pronto...")
        break
    
    # Extraigo el tipo de conversion seleccionado en el menu
    origen_nombre, origen_base = tipos_conversion[menu_opciones]
    
    # Destino de la conversion y se excluye la opcion origen 
    destino_conversion = []
    for opcion in tipos_conversion:
        if opcion != menu_opciones:
            destino_conversion.append(tipos_conversion[opcion])
    
    # Lista las opciones disponibles en base a la logica anterior
    print("\nSelecciona el tipo de conversion:")
    for i, (nombre, base) in enumerate(destino_conversion, 1):
        print(f"{i}. {nombre}")
        
    # Se captura la opcion elegida
    opcion_elegida = input("Elegi una opcion (1-3): ")
    
    # Se convierte a int y resta 1 al indice para que comience en 0 y coincida con la lista de destinos. Sino, me paso 1
    opcion_indice = int(opcion_elegida) - 1
    
    # Se obtiene el nombre y la base destino de la conversion
    destino_nombre, destino_base = destino_conversion[opcion_indice]
    
    # Se eliminan espacios de la entrada
    # num_str = input(f"Ingresa el numero en formato {origen_nombre}: ").strip()

    #Armamos bucle para validar espacios en blanco o que sean caracteres permitidos
    while True:
        num_str = input(f"Ingresa el numero en formato {origen_nombre}: ").strip()
        if num_str == '':
            print("El campo no puede estar vacio")
        elif not validar_caracteres(num_str, origen_base):
            print(f"No se permite el ingreso de dichos caracteres para la base {origen_nombre}. Intenta de nuevo")
        else:
            break

    # Convierte el numero a entero y decimal con el parametro base de origen
    valor_decimal = int(num_str, origen_base)
    
    # Imprime el resultado final de la converion
    resultado = funciones_conversion[destino_base](valor_decimal)
    print(f"\nEl resultado de la conversion de {origen_nombre} a {destino_nombre} es: {resultado}\n")