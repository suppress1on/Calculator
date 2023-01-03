#функция, возвращающая результат операций
def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    elif operation == 'mod':
        return a % b
    else:
        error = 'Wrong operation!' #обработка ошибки: неверная операция
        return error

#список с результатами функции выше
history = list()
cycle_work = True
while cycle_work: #пока переменная cycle_work = true, цикл будет работать
    #ниже представлено меню
    print('-------------------------')
    print('|Choice 1: Calculator    |')
    print('|Choice 2: History       |')
    print('|Choice 3: Sort history  |')
    print('|Choice 4: Clear history |')
    print('|Choice 5: Exit          |')
    print('-------------------------')
    choice = int(input('Enter choice: '))
    if choice == 1: 
        #условие 1: пользователь вводит числа и операцию
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        operation = input('Enter operation: ')

        res = calculator(a, b, operation) #вызов функции
        print('Result: ', res) #вывод результата на экран
        history.append(res) #добавление результата в историю

    elif choice == 2:
        #условие 2: вывод списка результатов на экран
        if not history: #обработка ошибки: "если список пуст"
            print('You have no history!')
        else:
            print(history)

    elif choice == 3:
        #условие 3: сортировка истории по возрастанию
        history.sort(); 
        print('Sort history: ', history)
    
    elif choice == 4:
        #условие 4: очистка истории
        history.clear();
        print('Cleared!')
    
    elif choice == 5:
        #условие 5: выход из программы
        cycle_work = False #присвоение переменной cycle_work значения false
        #цикл завершается, а вместе с ним - вся программа
    else:
        #обработка случая, когда пользователь ввел неверную цифру
        print('Wrong choice!')
