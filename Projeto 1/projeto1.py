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

def show_options():
    #Opções de cadastro e consulta
    print("\n1 - Register student")
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

#Função que verifica se o registro existe ou não
def verify_register(collection, key, value):
    for item in collection:
        if item[key] == int(value):
            return True  # Já existe
    print("Try again, type the number of a valid registration")
    return False
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
#Função que verifica se o input é um horario maior que zero
def verify_time(prompt):
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
#Função que verifica se o input é um horario maior que zero
def verify_number(prompt):
    while True:
        num = input(prompt).strip()
        try:
            #Tenta converter a string em um número
            num_i=int(num)
            if num_i>0:
                return num_i
            else: 
                print("Invalid answer. Please type a valid positive number.")
        except ValueError:
            print("Invalid answer. Please type a valid positive number.")
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
#Função que verifica a validade do nome de uma disciplina
def verify_subject_name(prompt):
    while True:
        name = input(prompt).strip().upper()
        # Regex para permitir letras, espaços e caracteres com acento e um número se necessário ao final
        pattern = r'^[A-Za-zÀ-ÿ]+(?: [A-Za-zÀ-ÿ]+)*(?: \d+)?$'
        if re.match(pattern, name):
            return name
        else:
            print("Invalid name. Please use only letters, accents, only one space between names and if you need, add a number just after the name")
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
    name = verify_subject_name("Subject name: ")
    reg_n = len(subjects)+1
    workload = verify_time("Workload(in hours): ")
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
    name = verify_subject_name("Class name: ")
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
    if len(students) == 0:
        print("\n||| No students registered yet to enroll |||")
    else:
        print("\n||| List of students |||")
        print("-"*40)
        for student in students:
            print(f"Name: {student['Name']}")
            print(f"Registration Number: {student['Register']}")
            print("-" * 40)
        if len(classes) == 0:
            print("\n||| No classes registered yet to enroll any student |||")
        else:
            print("\n||| List of classes |||")
            print("-" * 40)
            for classe in classes:
                print(f"Name: {classe['Name']}")
                print(f"Registration Number: {classe['Register']}")
                if classe['Subjects']:
                    print("Subjects:")
                    for subject in classe['Subjects']:
                        print(f"- {subject}")
                else:
                    print("No subjects assigned for this class yet.")
                print("-" * 40)
                
            while True:
                cl_reg = verify_number("Insert the register of the class you want to enroll a student: ")
                if verify_register(classes, 'Register', cl_reg) is True:
                    break
            while True: 
                st_reg = verify_number("Insert the register of the student you want to enroll in the class: ")
                if verify_register(students, 'Register', st_reg) is True:
                    break
            
            st_info = next(student for student in students if student['Register'] == st_reg)
            cl_info = next(classe for classe in classes if classe['Register'] == cl_reg)
            if st_info in cl_info['Students']:
                print("-" * 40)
                print(f"Student {st_info['Name']} is already enrolled in {cl_info['Name']}.")
                print("-" * 40)
            else:
                print("-" * 40)
                print(f"Student {st_info['Name']} enrolled in {cl_info['Name']}")
                print("-" * 40)
                cl_info['Students'].append(st_info)
            
#Função para atribuir um professor à uma disciplina
def assign_teacher():
    if len(teachers) == 0:
        print("\n||| No teachers registered yet to assign |||")
    else:
        print("\n||| List of teachers |||")
        print("-"*40)
        for teacher in teachers:
            print(f"Name: {teacher['Name']}")
            print(f"Registration Number: {teacher['Register']}")
            print("-" * 40)
        if len(subjects) == 0:
            print("\n||| No subjects registered yet to assign any teacher |||")
        else:
            print("\n||| List of subjects |||")
            print("-" * 40)
            for subject in subjects:
                print(f"Name: {subject['Name']}")
                print(f"Registration Number: {subject['Register']}")
                
            while True:
                su_reg = verify_number("Insert the register of the subject you want to assign a teacher: ")
                if verify_register(subjects, 'Register', su_reg) is True:
                    break
            while True: 
                te_reg = verify_number("Insert the register of the teacher you want to assign in the subject: ")
                if verify_register(teachers, 'Register', te_reg) is True:
                    break         
            te_info = next(teacher for teacher in teachers if teacher['Register'] == te_reg)
            su_info = next(subject for subject in subjects if subject['Register'] == su_reg)
            if te_info in su_info['Teachers']:
                print("-" * 40)
                print(f"Teacher {te_info['Name']} is already assigned in {su_info['Name']}.")
                print("-" * 40)
            else:
                print("-" * 40)
                print(f"Teacher {te_info['Name']} assigned in {su_info['Name']}")
                print("-" * 40)
                su_info['Teachers'].append(te_info)
#Função para atribuir uma disciplina a uma turma
def assign_subject():        
    if len(classes) == 0:
        print("\n||| No classes registered yet to assign any subject|||")
    else:
        print("\n||| List of classes |||")
        print("-"*40)
        for classe in classes:
            print(f"Name: {classe['Name']}")
            print(f"Registration Number: {classe['Register']}")
            print("-" * 40)
        if len(subjects) == 0:
            print("\n||| No subjects registered yet to assign to any class |||")
        else:
            print("\n||| List of subjects |||")
            print("-" * 40)
            for subject in subjects:
                print(f"Name: {subject['Name']}")
                print(f"Registration Number: {subject['Register']}")
                
            while True:
                su_reg = verify_number("Insert the register of the subject you want to assign a class: ")
                if verify_register(subjects, 'Register', su_reg) is True:
                    break
            while True: 
                cl_reg = verify_number("Insert the register of the class you want to assign in the subject: ")
                if verify_register(classes, 'Register', cl_reg) is True:
                    break
            cl_info = next(classe for classe in classes if classe['Register'] == cl_reg)
            su_info = next(subject for subject in subjects if subject['Register'] == su_reg)
            if su_info in cl_info['Subjects']:
                print("-" * 40)
                print(f"{su_info['Name']} is already assigned to {cl_info['Name']}.")
                print("-" * 40)
            else:
                print("-" * 40)
                print(f"{su_info['Name']} assigned in {cl_info['Name']}")
                print("-" * 40)
                cl_info['Subjects'].append(su_info)

#Função que mostra os alunos em uma turma
def students_class():
    if len(classes) == 0:
        print("\n||| No classes registered to check |||")
    else:
        print("\n||| List of classes |||")
        print("-"*40)
        for classe in classes:
            print(f"Name: {classe['Name']}")
            print(f"Registration Number: {classe['Register']}")
            print("-" * 40)
        while True: 
                cl_reg = verify_number("Insert the register of the class you want to check the students: ")
                if verify_register(classes, 'Register', cl_reg) is True:
                    break
        cl_info = next(classe for classe in classes if classe['Register'] == cl_reg)

        if cl_info['Students']:
                print(f"Students in {cl_info['Name']}:")
                for student in cl_info['Students']:
                    print(f"{student['Register']} - {student['Name']}")
        else:
            print("No students enrolled in this class.")
#Função que mostra os professores em uma disciplina
def teachers_subject():
    if len(subjects) == 0:
        print("\n||| No subjects registered to check |||")
    else:
        print("\n||| List of subjects |||")
        print("-"*40)
        for subject in subjects:
            print(f"Name: {subject['Name']}")
            print(f"Registration Number: {subject['Register']}")
            print("-" * 40)
        while True: 
                su_reg = verify_number("Insert the register of the subject you want to check the teachers: ")
                if verify_register(subjects, 'Register', su_reg) is True:
                    break
        su_info = next(subject for subject in subjects if subject['Register'] == su_reg)

        if su_info['Teachers']:
                print(f"Teachers in {su_info['Name']}:")
                for teacher in su_info['Teachers']:
                    print(f"{teacher['Register']} - {teacher['Name']}")
        else:
            print("No teachers assigned to this subject.")
#Função que mostra as disciplinas em uma turma
def subjects_class():
    if len(classes) == 0:
        print("\n||| No classes registered to check |||")
    else:
        print("\n||| List of classes |||")
        print("-"*40)
        for classe in classes:
            print(f"Name: {classe['Name']}")
            print(f"Registration Number: {classe['Register']}")
            print("-" * 40)
        while True: 
                cl_reg = verify_number("Insert the register of the class you want to check the subjects: ")
                if verify_register(classes, 'Register', cl_reg) is True:
                    break
        cl_info = next(classe for classe in classes if classe['Register'] == cl_reg)

        if cl_info['Subjects']:
                print(f"Subjects in {cl_info['Name']}:")
                for subject in cl_info['Subjects']:
                    print(f"{subject['Register']} - {subject['Name']}")
        else:
            print("No subjects assigned to this class.")

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
        print("-" * 40)
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
        print("-" * 40)
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
        print("-" * 40)
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

            if classe['Students']:
                print("Students:")
                for student in classe['Students']:
                    print(f"{student['Register']} - {student['Name']}")
            else:
                print("No students assigned for this class yet.")
            print("-" * 40)

#Início da execução do programa
print("| Welcome user |\n")

show_options()

#Loop para escolher uma das opções de função
while True:
    print("\n Select an option from the list or type 'exit' to finish the program\n(Type 0 to show the options again)")
    option = input().strip()
    try:
        if int(option) == 0:
            show_options()
        elif option == "exit":
            break
        elif int(option) == 1:
            reg_student()
        elif int(option) == 2:
            reg_teacher()
        elif int(option) == 3:
            reg_subject()
        elif int(option) == 4:
            reg_class()
        elif int(option) == 5:
            enroll_student()
        elif int(option) == 6:
            assign_teacher()
        elif int(option) == 7:
            assign_subject()
        elif int(option) == 8:
            students_class()
        elif int(option) == 9:
            teachers_subject()
        elif int(option) == 10:
            subjects_class()
        elif int(option) == 11:
            all_students()
        elif int(option) == 12:
            all_teachers()
        elif int(option) == 13:
            all_subjects()
        elif int(option) == 14:
            all_classes()
        else:
            print("Invalid option")    
    except ValueError:
            print("Invalid option")

#Fim do programa
print("\nProgram finished")
