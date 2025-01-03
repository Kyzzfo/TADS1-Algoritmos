'''
- Crie um sistema escolar que permita cadastrar alunos, professores, diciplinas e turmas
    - Alunos: nome, matrícula, data de nascimento, sexo, endereço, telefone, e-mail
    - Professores: nome, matrícula, data de nascimento, sexo, endereço, telefone, e-mail, disciplina
    - Disciplinas: nome, código, carga horária, professor
    - Turmas: nome, código, disciplinas, professores, alunos

- O sistema deve permitir a matrícula de alunos em turmas    
- O sistema deve permitir a filtragem de professores por diciplina    

- O sistema deve permitir a alocação de professores em diciplinas
- O sistema deve permitir a alocação de diciplinas em turmas

- O sistema deve permitir a consulta de alunos matriculados em turmas
- O sistema deve permitir a consulta de professores alocados em diciplinas
- O sistema deve permitir a consulta de disciplinas alocadas em turmas
'''
#Importa o módulo datetime para verificação de data
from datetime import *
#Importa o módulo para verificação de formatação dos textos
import re

#Matrizes de informações
students = []
teachers = []
subjects = []
classes = []

#Função que verifica se a data de nascimento é válida
def verify_date(prompt):
    while True:
        date_str = input(prompt).strip()
        try:
            #Tenta converter a string em uma data
            date = datetime.strptime(date_str, "%m/%d/%Y")
            return date
        except ValueError:
            print("Invalid date format. Please use MM/DD/YYYY.")
#Função que verifica se o input é um número maior que zero
def verify_number(prompt):
    while True:
        num = input(prompt).strip()
        try:
            #Tenta converter a string em um número
            num_i=int(num)
            if num_i>0:
                return num_i
            else: 
                print("Invalid answer. Please type a valid time in hours.")
        except ValueError:
            print("Invalid answer. Please type a valid time in hours.")
#Função que verifica se o gênero é válido
def verify_gender(prompt):
    while True:
        gen = input(prompt).strip().upper()
        if gen == "M":
            return "Male"
        elif gen == "F":
            return "Female"
        else:
            print("Invalid gender. Answer with M for Male or F for Female.")
#Função que verifica a validade do nome
def verify_name(prompt):
    while True:
        name = input(prompt).strip().upper()
        # Regex para permitir letras, espaços e caracteres com acento
        pattern = r'^[A-Za-zÀ-ÿ]+(?: [A-Za-zÀ-ÿ]+)*$'
        if re.match(pattern, name):
            return name
        else:
            print("Invalid name. Please use only letters, accents, and only one space between names.")
#Função que verifica a validade do email
def verify_email(prompt):
    while True:
        email = input(prompt).strip()
        # Regex para validar o e-mail
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return email
        else:
            print("Invalid email. Please enter a valid email.")
#Função que verifica a validade de um número de telefone
def verify_phone(prompt):
    while True:
        phone = input(prompt).strip()
        # Regex para validar o telefone
        pattern = r'^\d{10,15}$'
        if re.match(pattern, phone):
            return phone
        else:
            print("Invalid phone. Please enter a number with 10 to 15 digits.")

#Função que recebe dados do aluno
def data_student():
    print("|||Student registration|||")
    name = verify_name("Name: ")
    reg_n = len(students)+1
    birth = verify_date("Date of birth(MM/DD/YYYY): ")
    gender = verify_gender("Gender(M or F): ")
    address = input("Address: ").strip().upper()
    phone = verify_phone("Phone number(only digits): ")
    email = verify_email("Email address: ")
    print(f"Registration number: {len(students)+1}")
    return {
        'Name': name,
        'Register': reg_n,
        'Birth Date': birth.strftime('%m/%d/%Y'),
        'Gender': gender,
        'Address': address,
        'Phone': phone,
        'Email': email
    }
#Função que recebe dados do professor
def data_teacher():
    print("|||Teacher registration|||")
    name = verify_name("Name: ")
    reg_n = len(teachers)+1
    birth = verify_date("Date of birth(MM/DD/YYYY): ")
    gender = verify_gender("Gender(M or F): ")
    address = input("Address: ").strip().upper()
    phone = verify_phone("Phone number(only digits): ")
    email = verify_email("Email address: ")
    print(f"Registration number: {len(teachers)+1}")
    return {
        'Name': name,
        'Register': reg_n,
        'Birth Date': birth.strftime('%m/%d/%Y'),
        'Gender': gender,
        'Address': address,
        'Phone': phone,
        'Email': email,
        'Subjects':[]
    }
#Função que recebe dados de uma disciplina
def data_subject():
    print("|||Subject registration|||")
    name = input("Subject name: ").strip().upper()
    reg_n = len(subjects)+1
    workload = verify_number("Workload(in hours): ")
    print(f"Registration number: {len(subjects)+1}")
    return {
        'Name': name,
        'Register': reg_n,
        'Workload': workload,
        'Teachers':[]
    }
#Função que recebe dados de uma turma
def data_class():
    print("|||Class registration|||")
    name = input("Class name: ").strip().upper()
    reg_n = len(classes)+1
    print(f"Registration number: {len(classes)+1}")
    return {
        'Name': name,
        'Register': reg_n,
        'Subjects': [],
        'Teachers':[],
        'Students': []
    }

#Função que registra alunos
def reg_student():
    student=data_student()
    students.append(student)
    print(f"Student {student['Name']} registered successfully!")
#Função que registra professores
def reg_teacher():
    teacher=data_teacher()
    teachers.append(teacher)
    print(f"Teacher {teacher['Name']} registered successfully!")
#Função que registra disciplinas
def reg_subject():
    subject=data_subject()
    subjects.append(subject)
    print(f"Subject {subject['Name']} registered successfully!")
#Função que registra turmas
def reg_class():
    classe=data_class()
    classes.append(classe)
    print(f"Class {classe['Name']} registered successfully!")

#Função para matricular estudantes em turmas
def enroll_student():
    print(f"Student enrolled in class")
#Função para atribuir um professor à uma disciplina
def assign_teacher():
    print(f"Teacher assigned to subject")
#Função para atribuir uma disciplina a uma turma
def assign_subject():
    print(f"Subject assigned to class")

#Função que mostra os alunos em uma turma
def students_class():
    print("Alunos por turma")
#Função que mostra os professores em uma disciplina
def teachers_subject():
    print("Professores por disciplina")
#Função que mostra as disciplinas em uma turma
def subjects_class():
    print("Disciplinas por turma")

#Função que mostra todos os alunos
def all_students():
    if len(students) == 0:
        print("\n||| No students registered yet |||")
    else:
        print("\n||| List of students |||")
        print("-"*40)
        for student in students:
            print(f"Name: {student['Name']}")
            print(f"Registration Number: {student['Register']}")
            print(f"Date of Birth: {student['Birth Date']}")
            print(f"Gender: {student['Gender']}")
            print(f"Address: {student['Address']}")
            print(f"Phone: {student['Phone']}")
            print(f"Email: {student['Email']}")
            print("-" * 40)
#Função que mostra todos os professores
def all_teachers():
    if len(teachers) == 0:
        print("\n||| No teachers registered yet |||")
    else:
        print("\n||| List of teachers |||")
        for teacher in teachers:
            print(f"Name: {teacher['Name']}")
            print(f"Registration Number: {teacher['Register']}")
            print(f"Date of Birth: {teacher['Birth Date']}")
            print(f"Gender: {teacher['Gender']}")
            print(f"Address: {teacher['Address']}")
            print(f"Phone: {teacher['Phone']}")
            print(f"Email: {teacher['Email']}")
            if teacher['Subjects']:
                print("Subjects:")
                for subject in teacher['Subjects']:
                    print(f"- {subject}")
            else:
                print("No subjects assigned for this teacher yet.")
            print("-" * 40)
#Função que mostra todas as disciplinas
def all_subjects():
    if len(subjects) == 0:
        print("\n||| No subjects registered yet |||")
    else:
        print("\n||| List of subjects |||")
        for subject in subjects:
            print(f"Name: {subject['Name']}")
            print(f"Registration Number: {subject['Register']}")
            print(f"Workload: {subject['Workload']} hours")
            if subject['Teachers']:
                print("Teachers:")
                for teacher in subject['Teachers']:
                    print(f"- {teacher}")
            else:
                print("No teachers assigned for this subject yet.")
            print("-" * 40)
#Função que mostra todas as turmas
def all_classes():
    if len(classes) == 0:
        print("\n||| No classes registered yet |||")
    else:
        print("\n||| List of classes |||")
        for classe in classes:
            print(f"Name: {classe['Name']}")
            print(f"Registration Number: {classe['Register']}")
            if classe['Subjects']:
                print("Subjects:")
                for subject in classe['Subjects']:
                    print(f"- {subject}")
            else:
                print("No subjects assigned for this class yet.")
                            
            if classe['Teachers']:
                print("Teachers:")
                for teacher in classe['Teachers']:
                    print(f"- {teacher}")
            else:
                print("No teachers assigned for this class yet.")

            if classe['Teachers']:
                print("Teachers:")
                for teacher in classe['Teachers']:
                    print(f"- {teacher}")
            else:
                print("No teachers assigned for this class yet.")
            print("-" * 40)
            
#        'Name': name,
 #       'Register': reg_n,
  #      'Subjects': [],
   #     'Teachers':[],
    #    'Students': []

#Função que chama as funções das opções
def options(opt):
    try:
        if opt == "exit":
            return False
        elif int(opt) == 1:
            reg_student()
        elif int(opt) == 2:
            reg_teacher()
        elif int(opt) == 3:
            reg_subject()
        elif int(opt) == 4:
            reg_class()
        elif int(opt) == 5:
            enroll_student()
        elif int(opt) == 6:
            assign_teacher()
        elif int(opt) == 7:
            assign_subject()
        elif int(opt) == 8:
            students_class()
        elif int(opt) == 9:
            teachers_subject()
        elif int(opt) == 10:
            subjects_class()
        elif int(opt) == 11:
            all_students()
        elif int(opt) == 12:
            all_teachers()
        elif int(opt) == 13:
            all_subjects()
        elif int(opt) == 14:
            all_classes()
        else:
            print("Invalid option")    
    except ValueError:
            print("Invalid option")

#Início da execução do programa
print("| Welcome user |\n")

#Opções de cadastro e consulta
print("1 - Register student")
print("2 - Register teacher")
print("3 - Register subject")
print("4 - Register class")
print("5 - Enroll student in class")
print("6 - Assign teacher to subject")
print("7 - Assign subject to class")
print("8 - Consult the list of students in a class")
print("9 - Consult the list of teachers in a subject")
print("10 - Consult the list of subjects in a class")
print("11 - Consult the list of students in general")
print("12 - Consult the list of teachers in general")
print("13 - Consult the list of subjects in general")
print("14 - Consult the list of classes in general")

#Loop para escolher uma das opções de função
while True:
    print("\n Select an option from the list or type 'exit' to finish the program")
    option = input()
    if options(option) is False:
        break

#Fim do programa
print("\nProgram finished")
