from importlib.resources import read_binary
import json
from xml.etree.ElementPath import ops

# en obj_file = open() abrimos el archivo.json y luego en str_contents = read() leemos el archivo, 
# el loads() devolverá un objeto de tipo diccionario sobre el que se puede iterar.

# funcion para leer el json
def read_file(name_file):
    obj_file = open(name_file, 'rt', encoding='utf-8')
    
    str_contents = obj_file.read()
    res = json.loads(str_contents)
    
    obj_file.close()
    
    return res

# esta funcion es para guardar el archivo

def save_file(name_file, list):
    obj_file = open(name_file, 'wt', encoding='utf-8')
    
    content_to_save = json.dumps(list, indent=4)
    obj_file.write(content_to_save)
    
    obj_file.close()

def register_patients():
    patientName = input('Introduzca el nombre: ')
    patientLastname = input('Introduzca el apellido: ')
    dni = input('Intrdoduzca el DNI sin puntos: ')
    dateOfBirth = input('Fecha de nacimiento: ')
    patientNationality = input('Nacionalidad: ')

    openArchivo = read_file('dataPacientes.json')
    openArchivo[0]["pacientes"].append({
        "nombre": patientName,
        "Apellido": patientLastname,
        "DNI": dni,
        "F.nacimiento": dateOfBirth,
        "Nacionalidad": patientNationality,
    })
    save_file('dataPacientes.json', openArchivo)
    


# funcion para eliminar un pacientes
def delete_patient(object, namePatient):
    for element in object:
        if(element[0]["pacientes"] == namePatient):
            object.remove(element)


# Funcion para editar un paciente
def edit_patient(object, namePatient):
    
    
        

# INTERFAZ

def to_register():
    print('Bienvenido a Instituto Médico Las Luciérnagas :)')
    num = input('A continuacion elija una opcion:\n1 - Registrar un paciente.\n2 - Registrar un profesional.\n3 - Editar datos de un paciente.\n4 - Eliminar un paciente.\n5 - Agregar una historia clinica a un paciente.\n0 - Salir.\nRespuesta: ')
            
    match num:
        case "1":
           register_patients()
           to_register()
        case "2":
            professionalName = input('Ingrese su nombre: ')
            professionalLastname = input('Ingrese su apellido: ')
            specialty = input('Ingrese su especialidad: ')

            listProfessional = read_file('dataProfesionales.json')
            listProfessional["professionals"].append({"Nombre": professionalName, "Apellido": professionalLastname, "Especialidad": specialty})
            save_file('dataProfesionales.json', listProfessional)
        case "3":
            date = read_file('dataPacientes.json')
            n = input('Introduzca el nombre del usuario que desea eliminar: ')
            delete_patient(date, n)

            save_file('dataPacientes.json', date)
           
        case "0":
            print('Hasta pronto :)')
        
                
to_register()