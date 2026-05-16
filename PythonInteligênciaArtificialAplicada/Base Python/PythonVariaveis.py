#Tipos de Dados

#tipo String
name = input("Digite seu nome: ")
print(type(name))

#Tipo inteiro
age = int(input("Digite sua idade: "))
print(type(age))

#Tipo boolean
employee_status = bool(input("Está trabalhando ? "))
print(type(employee_status))

#Tipo float
salary = float(input("Digite seu salario: "))
print(type(salary))


print(
    f"Olá, {name}!\n\n"
    f"Verificamos que você possui {age} anos "
    f"e sua situação profissional atual é: {employee_status}.\n"
    f"Com base nisso, gostaríamos de oferecer um aumento "
    f"em seu salário atual de {salary}."
)


