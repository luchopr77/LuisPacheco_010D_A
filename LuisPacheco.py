def leer_opcion():
    while True:
        try:
            opc = input("Ingrese opción: ")
            opc_int = int(opc)
            if opc_int >= 1 and opc_int <= 6:
                return opc_int
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def stock_plataforma(plataforma, dic_juegos, dic_inventario):
    total = 0
    p_buscar = plataforma.strip().lower()
    for cod in dic_juegos:
        datos = dic_juegos[cod]
        if datos[1].lower() == p_buscar:
            if cod in dic_inventario:
                total = total + dic_inventario[cod][1]
    print("El total de stock disponibles es:", total)

def busqueda_precio(p_min, p_max, dic_juegos, dic_inventario):
    resultados = []
    for cod in dic_inventario:
        datos_inv = dic_inventario[cod]
        precio = datos_inv[0]
        stock = datos_inv[1]
        if precio >= p_min and precio <= p_max and stock > 0:
            if cod in dic_juegos:
                titulo = dic_juegos[cod][0]
                resultados.append(titulo + "--" + cod)
    if len(resultados) > 0:
        resultados.sort()
        print("Los juegos encontrados son:", resultados)
    else:
        print("No hay juegos en ese rango de precios.")

def buscar_codigo(codigo, dic_juegos):
    c_limpio = codigo.strip().upper()
    if c_limpio in dic_juegos:
        return True
    else:
        return False

def actualizar_precio(codigo, nuevo_precio, dic_juegos, dic_inventario):
    cod_up = codigo.strip().upper()
    if buscar_codigo(cod_up, dic_juegos) == True:
        if cod_up in dic_inventario:
            dic_inventario[cod_up][0] = nuevo_precio
            return True
    return False

def validar_codigo(codigo, dic_juegos):
    c = codigo.strip()
    if c == "":
        return False
    if c.upper() in dic_juegos:
        return False
    return True

def validar_plataforma(plataforma):
    if plataforma.strip() == "":
        return False
    return True 

def validar_genero(genero):
    if genero.strip() == "":
        return False
    return True

def validar_clasificacion(clasificacion):
    c = clasificacion.strip()
    if c == 'E' or c == 'T' or c == 'M':
        return True
    return False

def validar_multiplayer(multiplayer):
    m = multiplayer.strip().lower()
    if m == 's' or m == 'n':
        return True
    return False

def validar_editor(editor):
    if editor.strip() == "":
        return True
    return False

def validar_precio(precio):
    if precio > 0:
        return True
    return False

def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, dic_juegos, dic_inventario):
    cod_up = codigo.strip().upper()
    if cod_up in dic_juegos:
        return False
    if multiplayer.strip().lower() == 's':
        mp_bool = True
    else:
        mp_bool = False
    
    dic_juegos[cod_up] = [titulo.strip(), plataforma.strip(), clasificacion.strip(), mp_bool, editor.strip()]
    dic_inventario[cod_up] = [precio, stock]
    return True

def eliminar_juego(codigo, dic_juegos, dic_inventario):
    cod_up = codigo.strip().upper()
    if buscar_codigo(cod_up, dic_juegos) == True:
        if cod_up in dic_juegos:
            del dic_juegos[cod_up]
        if cod_up in dic_inventario:
            del dic_inventario[cod_up]
        return True
    return False

def mostrar_menu