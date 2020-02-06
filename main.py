import mysql.connector

bd = mysql.connector.connect(user='michel',
                           password='12345678',
                           database='escuela')

cursor = bd.cursor()

while True:
    print('1) Agregar alumno')
    print('2) Mostrar alumnos')
    print('0) Salir')
    op = input('> ')
    if op == '1':
        id = input('id: ')
        nombre = input('nombre: ')
        apellido1 = input('apellido1: ')
        apellido2 = input('apellido2: ')
        codigo = input('codigo: ')
        carrera = input('carrera: ')

        consulta = "INSERT INTO alumno " \
                   "(id, nombre, apellido1, " \
                   "apellidos2, codigo, carrera) " \
                   "VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(consulta,
                       (id, nombre, apellido1,
                        apellido2, codigo, carrera))
        bd.commit()

    elif op == '2':
        consulta = "SELECT * FROM alumno"
        cursor.execute(consulta)

        for fila in cursor.fetchall():
            print('id: ', fila[0])
            print('nombre: ', fila[1])
            print('apellido1: ', fila[2])
            print('apellidos2: ', fila[3])
            print('codigo: ', fila[4])
            print('carrera: ', fila[5])

    elif op == '0':
        break