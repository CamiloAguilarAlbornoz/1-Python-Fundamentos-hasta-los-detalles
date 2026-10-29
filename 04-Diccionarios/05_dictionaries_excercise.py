students = {
    'Ana': [8, 7, 9],
    'Luis': [6, 5, 7],
    'Sofía': [10, 9, 10]
}

# Agregar un nuevo estudiante
new_student = input('\nIngrese el nombre del nuevo estudiante: ')
if new_student not in students:
    califications_new_student = input('\nIngrese las calificaciones del nuevo estudiante separadas por ,: ')
    califications_new_student = califications_new_student.split(',')
    califications_new_student = [int(x) for x in califications_new_student]
    students.update({new_student: califications_new_student})
    print(f'\nDiccionario con nuevo estudiante: {students}\n')
else: print('\nEl estudiante ya se encontraba en el diccionario\n')

# Promedio de un estudiante existente
student = input('\nIngrese el nombre de un estudiante: ')
if student in students:
    califications = students.get(student)
    if len(califications) > 0 :
        average = sum(califications) / len(califications)
        print(f'\nEl promedio de {student} es {average}\n')
    else: print('\nEl estudiante existe pero no tiene calificaciones\n')
else: print('\nEl estudiante no existe en la lista\n')

# Promedio del estudiante nuevo
califications = students.get(new_student)
if len(califications) > 0 :
    average = sum(califications) / len(califications)
    print(f'\nEl promedio de {student} es {average}\n')
else: print('\nEl estudiante existe pero no tiene calificaciones\n')