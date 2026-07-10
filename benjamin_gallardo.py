#op 1
def validar_genero(genero):return len(genero)>0
def cupos_genero(peliculas,cartelera):
    genero=input("Ingrese el genero de la pelicula: ").strip()
    total_cupos=0
    if validar_genero:
        for codigo in peliculas:
            if peliculas[codigo][1].lower()==genero.lower():
                if codigo in cartelera:
                    total_cupos+=cartelera[codigo][1]
                else:
                    print(f"El genero {genero} no se encuentra en cartelera")
            else:
                print(f"El genero {genero} no se encuentra registrado")
        print(f"El total de cupos del genero {genero} es de {total_cupos}")
#op 2
def validar_precio_minimo(p_min):return p_min>0
def validar_precio_maximo(p_max):return p_max>0
def busqueda_precio(peliculas,cartelera,p_min,p_max):
    lista=[]
    if validar_precio_minimo and validar_precio_maximo:
        for codigo in cartelera:
            if p_max>=cartelera[codigo][0]>=p_min:
                if cartelera[codigo][1]>0:
                    lista.append(f"{peliculas[codigo][0]}--{codigo}")
            else:
                print("No hay películas en ese rango de precios")
        lista.sort()
        print(lista)
    else:
        print("Debe ingresar un numero mayor a 0")
#op 3
def buscar_codigo(codigo,cartelera):
    if codigo.upper() in cartelera:
        return True
    return False
def validar_nuevo_precio(nuevo_precio):return nuevo_precio>0
def actualizar_precio(codigo,nuevo_precio,cartelera):
    posicion=buscar_codigo(codigo,cartelera)
    try:
        nuevo_precio=int(input("Ingrese el nuevo precio:    "))
    except ValueError:
        print("Debe ingresar valores enteros")
    if validar_nuevo_precio(nuevo_precio):
        if posicion:
            cartelera[codigo.upper()][0]=nuevo_precio
            return True
        else:
            return False
    else:
        print("Debe ingresar un numero mayor a 0")
#op 4
def validar_codigo(codigo):return len(codigo)>0
def validar_titulo(titulo):return len(titulo)>0
def validar_genero(genero):return len(genero)>0
def validar_duracion(duracion):return duracion>0
def validar_idioma(idioma):return len(idioma)>0
def validar_3d(es_3d):
    if es_3d.lower()=="s":
        return True
    else:
        return False
def validar_precio(precio):return precio>0
def validar_cupos(cupos):return cupos>0

def agregar_pelicula(codigo, titulo, genero, duracion,clasificacion, idioma, es_3d, precio, cupos,cartelera,peliculas):
    if not validar_codigo(codigo): print("No debe dejar vacio el ingreso")
    elif not validar_titulo(titulo):print("No debe dejar vacio el ingreso")
    elif not validar_genero(genero):print("No debe dejar vacio el ingreso")
    elif not validar_duracion(duracion):print("El numero debe ser mayor a 0")
    elif not validar_idioma(idioma):print("No debe dejar vacio el ingreso")
    elif not validar_3d(es_3d):print("No debe dejar vacio el ingreso")
    elif not validar_precio(precio):print("El numero debe ser mayor a 0")
    elif not validar_cupos(cupos):print("El numero debe ser mayor a 0")
    elif buscar_codigo(codigo,cartelera):
        return False
    else:
        peliculas[codigo.upper()]=[titulo,genero,duracion,clasificacion,idioma,es_3d]
        cartelera[codigo.upper()]=[precio,cupos]
        return True






    







def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("===========================================================")
def leer_opcion():
    try:
        opcion=int(input(""))
        if 0>=opcion>=7:
            print("debe ingresar un numero entre 1 y 6")
    except ValueError:
        print("Debe ingresar valores enteros")
def main():
    peliculas = {
        'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
        'P102': ['Noche Neón', 'accion', 125, 'C', 'Ingles', True],
        'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
        'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
        'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
        'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
    }
    cartelera = {
        'P101': [5990, 40],
        'P102': [7990, 0],
        'P103': [4990, 25],
        'P104': [6990, 12],
        'P105': [8990, 8],
        'P106': [7490, 3],
    }
    while True:
        menu()
        op=leer_opcion()
        if op==1: cupos_genero(peliculas,cartelera)
        elif op==2:
            try:
                p_min=int(input("ingrese el precio minimo:  "))
                p_max=int(input("ingrese el precio maximo:  "))
            except ValueError:
                print("Debe ingresar valores enteros")
            busqueda_precio(peliculas,cartelera,p_min,p_max)
        elif op==3:
            if actualizar_precio():
                print("Precio actualizado")
            else:
                print("El codigo no existe")
        elif op==4:
            codigo=input("Ingrese un codigo:    ").strip()
            titulo=input("Ingrese un titulo:    ").strip()
            genero=input("Ingrese un genero:    ").strip()
            duracion=int("input(Ingrese la duracion")
            clasificacion=input("Ingrese una clasificacion:    ").strip()
            idioma=input("Ingrese un idioma:    ").strip()
            es_3d=input("Es 3D? s/n:    ").strip()
            precio=int(input("ingrese un precio"))
            cupos =int(input("ingrese cantidad de cupos"))
            agregar_pelicula(codigo, titulo, genero, duracion,clasificacion, idioma, es_3d, precio, cupos,cartelera,peliculas)
            if agregar_pelicula(codigo, titulo, genero, duracion,clasificacion, idioma, es_3d, precio, cupos,cartelera,peliculas):
                print("Película agregada")
            else:
                print("El código ya existe")



            



