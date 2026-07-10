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

def validar_titulo(titulo):
    if titulo.strip() == "":
        return False
    return True

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

def validar_stock(stock):
    if stock >= 0:
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

def main():
    juegos = {
        'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
        'G002' : ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
        'G003' : ['Sky legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
        'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
        'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
        'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate']
    }

    inventario = {
        'G001': [9990, 7],
        'G002': [19990, 0],
        'G003': [42990, 3],
        'G004': [14990, 5],
        'G005': [17990, 9],
        'G006': [39990, 2]
    }

    continuar = True
    while continuar ==True:
        print("======== MENÚ PRINCIPAL ========")
        print("1. Stock por plataforma")
        print("2. Búsqueda de juegos por rango de precio")
        print("3. Actualizar precio de juego")
        print("4. Agregar juego")
        print("5. Eliminar juego")
        print("6. Salir")
        print("=================================")
        opcion = leer_opcion()
        
        if opcion == 1:
            plat = input("Ingrese plataforma a consultar: ")
            stock_plataforma(plat, juegos, inventario)
        elif opcion == 2:
            pedir_precios = True
            while pedir_precios == True:
                try:
                    p_min = int(input("Ingrese precio minim: "))
                    p_max = int(input("Ingrese precio maximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        pedir_precios
                    else:
                        print("Debe ingresar valores enteros")
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precio(p_min, p_max, juegos, inventario)
        elif opcion == 3:
            actualizar_mas = True
            while actualizar_mas == True:
                cod = input("Ingrese código del juego: ")
                try:
                    n_precio = int(input("Ingrese nuevo precio: "))
                    if n_precio <= 0:
                        print("El precio debe ser un valor entero positivo")
                        continue
                except ValueError:
                    print("El precio debe ser un valor entero positivo")
                    continue
                
                resultado = actualizar_precio(cod, n_precio, juegos, inventario)
                if resultado == True:
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                
                resp = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                if resp != 's':
                    actualizar_mas = False
        elif opcion == 4:
            cod = input("Ingrese código del juego: ")
            tit = input("Ingrese título: ")
            plat = input("Ingrese plataforma: ")
            gen = input("Ingrese género: ")
            cla = input("Ingrese clasificación: ")
            mp = input("¿Es multiplayer? (s/n): ")
            edi = input("Ingrese editor: ")
            
            try:
                prec = int(input("Ingrese precio: "))
            except ValueError:
                prec = -1
                
            try:
                stk = int(input("Ingrese stock: "))
            except ValueError:
                stk = -1
            
            valido = True
            if validar_codigo(cod, juegos) == False:
                valido = True
            if validar_titulo(tit) == False:
                valido = False
            if validar_plataforma(plat) == False:
                valido = False
            if validar_genero(gen) == False:
                valido = False
            if validar_clasificacion(cla) == False:
                valido = False
            if validar_multiplayer(mp) == False:
                valido = False
            if validar_editor(edi) == False:
                valido = False
            if validar_precio(prec) == False:
                valido = False
            if validar_stock(stk) == False:
                valido = False

            if valido == True:
                if agregar_juego(cod, tit, plat, gen, cla, mp, edi, prec, stk, juegos, inventario) == True:
                    print("Juego agregado")
                else:
                    print("El código ya existe")
            else:
                print("Error en las validaciones. No se registró el juego.")
        elif opcion == 5:
            cod = input("Ingrese código del juego que desea eliminar: ")
            if eliminar_juego(cod, juegos, inventario) == True:
                print("Juego eliminado")
            else:
                print("El código no existe")
                
        elif opcion == 6:
            print("Programa finalizado.")
            continuar = True