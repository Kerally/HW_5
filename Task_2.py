import requests


# створіть функцію для перевірки, що за замовчуванням число не менше 0 та не 
# більше 100 (потрібно, щоб верхня та нижня межа могли налаштовуватися)

def test_number():
    min_limit = int(input("Enter the min: "))
    max_limit = int(input("Enter the max: "))
    number = int(input("Enter the number for test: "))
    if min_limit < number < max_limit:
        return True
    return False

test_number()


# створіть функцію для перевірки, що отриманий аргумент є числом (інт)

def is_int(arg):
   if arg.isdigit() == True:
      return True
   return False

arg = input("Enter the argument: ")
print(is_int(arg))


# створіть функцію, що отримує урл та віддає json, отриманий через цей урл
# (валідувати не потрібно, ми поки що працюємо з даними, вважаючи, 
# що вони валідні)

def URL_json(URL):
    r = requests.get(URL)
    return r.json

URL = input("Enter the URL: ")
print(URL_json(URL))


# створити функцію, яка приймає стрічку, і має її повернути, враховуючи , що ця
# стрічка має бути довжиною не більше 150 символів (може регулюватися через 
# передачу аргумента функції), а якщо отримана стрічка буде довшою за 150 
# символів, то стрічка має бути обрізана до 150 символів, причому останні
# три символи мають бути ... (трьома крапками)

def len_string(input_string):
    if len(input_string) > 150:
        input_string = input_string[:150]
        dots = "..."
        input_string = input_string + dots
        return input_string
    else:
        return input_string

input_string = input("Enter the text: ")
print(len_string(input_string))


# написати функцію, котра дозаписує (режим "а") в файл певні текстові дані
# покрити все тестами (окрім запису в файл, це буде занадто)

def mode_a():
   try:
      f = open("test.txt", encoding = 'utf-8')
      with open("test.txt",'w',encoding = 'utf-8') as f:
         f.write("Mode 'A'\n")
   finally:
      f.close()

mode_a()

