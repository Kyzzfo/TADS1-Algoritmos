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

#Função que recebe dados do aluno
def data_student():
    print("|||Student registration|||")
    name = input("Name: ").strip().upper()
    reg_n = len(students)+1
    birth = verify_date("Date of birth(MM/DD/YYYY): ")
    gender = verify_gender("Gender(M or F): ")
    address = input("Address: ").strip().lower()
    phone = input("Phone number: ").strip().lower()
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
    name = input("Name: ").strip().upper()
    reg_n = len(teachers)+1
    birth = verify_date("Date of birth(MM/DD/YYYY): ")
    gender = verify_gender("Gender(M or F): ")
    address = input("Address: ").strip().lower()
    phone = input("Phone number: ").strip().lower()
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
        'Subject':None
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
        'Teacher':None
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
            print("")
        elif int(opt) == 5:
            print("")
        elif int(opt) == 6:
            print("")
        elif int(opt) == 7:
            print("")
        elif int(opt) == 8:
            print("")
        elif int(opt) == 9:
            print("")
        elif int(opt) == 10:
            print("")
        elif int(opt) == 11:
            print("")
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
print("6 - Filter teachers by subject")
print("7 - Assign teacher to subject")
print("8 - Assign subject to class")
print("9 - Consult the list of students in a class")
print("10 - Consult the list of teachers in a subject")
print("11 - Consult the list of subjects in a class")

#Loop para escolher uma das opções de função
while True:
    print("\n Select an option from the list or type 'exit' to finish the program")
    option = input()
    if options(option) is False:
        break

#Fim do programa
print("\nProgram finished")
