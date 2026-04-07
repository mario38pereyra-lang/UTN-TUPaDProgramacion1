#Ejercicio 1— “Caja del Kiosco”
#Objetivo: Simular una compra con validaciones y cálculo de total
#Requisitos
#1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).

nombre = input("Ingrese su nombre: ")

while not nombre.isalpha():
    print("Error: solo se permiten letras.")
    nombre = input("Ingrese su nombre nuevamente: ")

print("Nombre válido:", nombre)

#2. Pedir cantidad de productos a comprar (número entero positivo, validar con
#.isdigit() en while).

productos = input("Ingrese la cantidad de productos a comprar: ")

while not productos.isdigit() or int(productos) <= 0:
    print("Error: solo se permiten números enteros positivos.")
    productos = input("Ingrese la cantidad de productos a comprar nuevamente: ")

print("Cantidad de productos válida:", int(productos))

total_sin_descuento = 0
total_con_descuento = 0

#3. Por cada producto (usar for):
#o Pedir precio (entero, validar .isdigit()).
#o Pedir si tiene descuento S/N (validar con while, aceptar s o n en cualquier mayuscula/minuscula).
#o Si tiene descuento: aplicar 10% al precio de ese producto.

for i in range(int(productos)):
    precio = input(f"Ingrese el precio del producto {i+1}: ")
    while not precio.isdigit() or int(precio) <= 0:
        print("Error: solo se permiten números enteros positivos.")
        precio = input(f"Ingrese el precio del producto {i+1} nuevamente: ")

    tiene_descuento = input("¿Tiene descuento? (S/N): ").lower()
    while tiene_descuento not in ['s', 'n']:
        print("Error: solo se permiten 'S' o 'N'.")
        tiene_descuento = input("¿Tiene descuento? (S/N): ").lower()

    if tiene_descuento == 's':
        precio = int(precio) * 0.9  # Aplicar 10% de descuento

    print(f"Precio final del producto {i+1}: {precio}")

    total_sin_descuento += int(precio) / 0.9 if tiene_descuento == 's' else int(precio)
    total_con_descuento += int(precio)

#4. Al final mostrar: o Total sin descuentos o Total con descuentos o Ahorro total
# o Promedio por producto (usar float y formatear con :.2f, ejem: x = 3.14159 print(f"{x:.2f}"))

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / int(productos)

print("--- RESUMEN DE COMPRA ---")
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

print("////////////////////////////////////////////////////////////////////////////////////////////////////")

#Ejercicio 2 — “Acceso al Campus y Menú Seguro” Objetivo: Login con intentos + menú de acciones con validación estricta.
#Requisitos 1. Definir credenciales fijas en el código: o usuario correcto: "alumno" o clave correcta: "python123"

usuario_correcto = "alumno"
clave_correcta = "python123"

#2. Permitir máximo 3 intentos para ingresar usuario y clave.

intentos = 3
while intentos > 0:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("¡Acceso concedido!")
        break
    else:
        intentos -= 1
        print(f"Credenciales incorrectas. Intentos restantes: {intentos}")

#3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.

if intentos == 0:
    print("Cuenta bloqueada.")  

#4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir: 1. Ver estado de inscripción (mostrar “Inscripto”)
#2. Cambiar clave (pedir nueva clave y confirmación; debencoincidir)
#3. Mostrar mensaje motivacional (1 frase)
#4. Salir

if intentos > 0:
    while True:
        print("\n--- MENÚ ---")
        print("1. Ver estado de inscripción")
        print("2. Cambiar clave")
        print("3. Mostrar mensaje motivacional")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("Estado de inscripción: Inscripto")
        elif opcion == '2':
            nueva_clave = input("Ingrese la nueva clave: ")
            confirmacion_clave = input("Confirme la nueva clave: ")
            if len(nueva_clave) < 6:
                print("Error: La nueva clave debe tener al menos 6 caracteres.") 

            elif nueva_clave == confirmacion_clave:
                clave_correcta = nueva_clave
                print("Clave cambiada exitosamente.")

            else:
                print("Error: Las claves no coinciden.")
        elif opcion == '3':
            print("¡ya eres todo un programador!")
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

#5. Validación del menú: o Debe ser número (.isdigit()) o Debe estar entre 1 y 4

        if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
            print("Error: Debe ingresar un número entre 1 y 4.")

print("////////////////////////////////////////////////////////////////////////////////////////////////////")   

#Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
#Contexto: Hay 2 días de atención: Lunes y Martes. Cada día tiene cupos fijos: • Lunes: 4 turnos • Martes: 3 turnos
#Reglas: 1. Pedir nombre del operador (solo letras).

operador = input("ingrese el nombre del operador: ")
while not operador.isalpha():
    print("Error: solo se permiten letras.")
    operador = input("Ingrese el nombre del operador nuevamente: ") 

#2. Menú repetitivo hasta salir: 1. Reservar turno/ 2. Cancelar turno (por nombre)/ 3. Ver agenda del día
#4. Ver resumen general/ 5. Cerrar sistema.

agenda_lunes = [None] * 4
agenda_martes = [None] * 3  
turnos_reservados = 0
turnos_cancelados = 0

while True: 
    print("\n--- MENÚ ---")
    print("1. Reservar turno")
    print("2. Cancelar turno (por nombre)")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        dia = input("Ingrese el día para reservar (Lunes/Martes): ").lower()
        if dia == 'lunes':
            if None in agenda_lunes:
                nombre_cliente = input("Ingrese el nombre del cliente: ")
                while not nombre_cliente.isalpha():
                    print("Error: solo se permiten letras.")
                    nombre_cliente = input("Ingrese el nombre del cliente nuevamente: ")
                for i in range(len(agenda_lunes)):
                    if agenda_lunes[i] is None:
                        agenda_lunes[i] = nombre_cliente
                        turnos_reservados += 1
                        print(f"Turno reservado para {nombre_cliente} el Lunes.")
                        break
            else:
                print("No hay turnos disponibles para el Lunes.")
        elif dia == 'martes':
            if None in agenda_martes:
                nombre_cliente = input("Ingrese el nombre del cliente: ")
                while not nombre_cliente.isalpha():
                    print("Error: solo se permiten letras.")
                    nombre_cliente = input("Ingrese el nombre del cliente nuevamente: ")
                for i in range(len(agenda_martes)):
                    if agenda_martes[i] is None:
                        agenda_martes[i] = nombre_cliente
                        turnos_reservados += 1
                        print(f"Turno reservado para {nombre_cliente} el Martes.")
                        break
            else:
                print("No hay turnos disponibles para el Martes.")
        else:
            print("Día no válido. Por favor, ingrese Lunes o Martes.")

#3. Reservar: o Elegir día (1=Lunes, 2=Martes). o Pedir nombre del paciente (solo letras). o Verificar que no esté repetido en ese día (comparando con las variables
#ya cargadas).o Guardar en el primer espacio libre (ej. lunes1, lunes2…).

    elif opcion == '2':
        dia = input("Ingrese el día para cancelar (Lunes/Martes): ").lower()
        if dia == 'lunes':
            nombre_cliente = input("Ingrese el nombre del cliente a cancelar: ")
            while not nombre_cliente.isalpha():
                print("Error: solo se permiten letras.")
                nombre_cliente = input("Ingrese el nombre del cliente a cancelar nuevamente: ")
            if nombre_cliente in agenda_lunes:
                index = agenda_lunes.index(nombre_cliente)
                agenda_lunes[index] = None
                turnos_cancelados += 1
                print(f"Turno cancelado para {nombre_cliente} el Lunes.")
            else:
                print(f"No se encontró un turno para {nombre_cliente} el Lunes.")
        elif dia == 'martes':
            nombre_cliente = input("Ingrese el nombre del cliente a cancelar: ")
            while not nombre_cliente.isalpha():
                print("Error: solo se permiten letras.")
                nombre_cliente = input("Ingrese el nombre del cliente a cancelar nuevamente: ")
            if nombre_cliente in agenda_martes:
                index = agenda_martes.index(nombre_cliente)
                agenda_martes[index] = None
                turnos_cancelados += 1
                print(f"Turno cancelado para {nombre_cliente} el Martes.")
            else:
                print(f"No se encontró un turno para {nombre_cliente} el Martes.")
        else:
            print("Día no válido. Por favor, ingrese Lunes o Martes.")

#4. Cancelar: o Elegir día. o Pedir nombre del paciente (solo letras).o Si existe, cancelar y dejar el espacio vacío ("").

    elif opcion == '3':
        dia = input("Ingrese el día para ver la agenda (Lunes/Martes): ").lower()
        if dia == 'lunes':
            print("Agenda del Lunes:")
            for i, turno in enumerate(agenda_lunes):
                print(f"Turno {i+1}: {turno if turno is not None else 'Disponible'}")
        elif dia == 'martes':
            print("Agenda del Martes:")
            for i, turno in enumerate(agenda_martes):
                print(f"Turno {i+1}: {turno if turno is not None else 'Disponible'}")
        else:
            print("Día no válido. Por favor, ingrese Lunes o Martes.")

#5. Ver agenda del día: o Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si está vacío.

    elif opcion == '4':
        print("--- RESUMEN GENERAL ---")
        print(f"Operador: {operador}")
        print(f"Turnos reservados: {turnos_reservados}")
        print(f"Turnos cancelados: {turnos_cancelados}")    

#6. Resumen general: o Turnos ocupados y disponibles por día. o Día con más turnos (o empate).

    elif opcion == '5':
        print("¡Cerrando sistema! Hasta luego.")
        break   

print("////////////////////////////////////////////////////////////////////////////////////////////////////")   

#Ejercicio 4 — “Escape Room: La Bóveda”

# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

print("=== ESCAPE ROOM: LA BÓVEDA ===")

# Validar nombre
while True:
    nombre = input("Ingresá el nombre del agente: ")
    if nombre.isalpha():
        break
    else:
        print("Error: Solo letras.")

# Bucle principal
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    
    # Regla de bloqueo por alarma
    if alarma and tiempo <= 3:
        print("\n Sistema bloqueado por alarma. PERDISTE.")
        break

    print("\n--- ESTADO ---")
    print(f"Agente: {nombre}")
    print(f"Energía: {energia} | Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {'ON' if alarma else 'OFF'}")
    print(f"Código parcial: {codigo_parcial}")

    print("\n1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")

    # Validar opción
    while True:
        opcion = input("Elegí una opción: ")
        if opcion.isdigit() and opcion in ["1", "2", "3"]:
            opcion = int(opcion)
            break
        else:
            print("Error: Opción inválida.")

    # OPCIÓN 1: Forzar cerradura
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1

        # Regla anti-spam
        if forzar_seguidas == 3:
            print(" Forzaste demasiadas veces. ¡Se trabó la cerradura!")
            alarma = True
            continue

        # Riesgo de alarma
        if energia < 40:
            print(" Riesgo de alarma. Elegí un número del 1 al 3:")
            while True:
                riesgo = input("Número: ")
                if riesgo.isdigit() and riesgo in ["1", "2", "3"]:
                    riesgo = int(riesgo)
                    break
                else:
                    print("Error: Ingresá 1, 2 o 3.")
            
            if riesgo == 3:
                print("¡Se activó la alarma!")
                alarma = True
                continue

        if not alarma:
            print("Cerradura abierta.")
            cerraduras_abiertas += 1

    # OPCIÓN 2: Hackear panel
    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        forzar_seguidas = 0

        print("Hackeando...")
        for i in range(4):
            print(f"Progreso {i+1}/4")
            codigo_parcial += "A"

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            print("Código completo. Cerradura abierta automáticamente.")
            cerraduras_abiertas += 1

    # OPCIÓN 3: Descansar
    elif opcion == 3:
        tiempo -= 1
        forzar_seguidas = 0

        if alarma:
            energia -= 10
            print("La alarma consume energía extra.")

        energia += 15
        if energia > 100:
            energia = 100

        print("Descansaste.")

# Resultado final
print("\n=== RESULTADO FINAL ===")

if cerraduras_abiertas == 3:
    print("¡VICTORIA! Abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA. Te quedaste sin recursos.")
elif alarma and tiempo <= 3:
    print("DERROTA por bloqueo del sistema.")

print("/////////////////////////////////////////////////////////////////////////////////////////////////////////")

#Ejercicio 5 — “Escape Room:"La Arena del Gladiador" 

print("--- BIENVENIDO A LA ARENA ---")

# Paso 1: Nombre del jugador
while True:
    nombre = input("Nombre del Gladiador: ")
    if nombre.isalpha():
        break
    else:
        print("Error: Solo se permiten letras.")

# Paso 2: Variables iniciales
vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
turno_jugador = True  # boolean

print("\n=== INICIO DEL COMBATE ===")

# Paso 3: Ciclo de combate
while vida_jugador > 0 and vida_enemigo > 0:

    print("\n=== NUEVO TURNO ===")
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

    # TURNO DEL JUGADOR
    if turno_jugador:
        print("\nElige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        # Validación de opción
        while True:
            opcion = input("Opción: ")
            if opcion.isdigit():
                opcion = int(opcion)
                if opcion in [1, 2, 3]:
                    break
                else:
                    print("Error: Elegí 1, 2 o 3.")
            else:
                print("Error: Ingrese un número válido.")

        # Opción 1: Ataque Pesado
        if opcion == 1:
            if vida_enemigo < 20:
                danio = danio_pesado * 1.5  # float
                print("¡Golpe Crítico!")
            else:
                danio = danio_pesado

            vida_enemigo -= danio
            print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

        # Opción 2: Ráfaga Veloz
        elif opcion == 2:
            print(">> ¡Inicias una ráfaga de golpes!")
            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        # Opción 3: Curar
        elif opcion == 3:
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("Te curaste 30 HP")
            else:
                print("¡No quedan pociones!")

        # TURNO DEL ENEMIGO (si sigue vivo)
        if vida_enemigo > 0:
            vida_jugador -= danio_enemigo
            print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")

    # (aunque no es necesario alternar turno, mantenemos boolean por requisito)
    turno_jugador = True

# Paso 4: Resultado final
print("\n=== FIN DEL COMBATE ===")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")





 


