import random

start = input('Ви запустили гру "Камінь, ножиці, папір". Бажаєте пограти? (Вводьте + або -):')

if start == '+':
    print('Завантаження...')
    print("Завантаження завершено! Починаємо!")
    print("3...2...1...")
    print('Якщо захочете закінчити введіть "-".')
    print('Якщо захочете дізнатися рахунок вводите "р".')
    user_ball = 0
    rand_ball = 0
    while True:
        user = input("Камінь, ножиці або папір? (Вводьте до, н або п): ")
        list_play = ['к', 'н', 'п']
        if user in list_play:
            rand = random.choice(list_play)
            print(rand)

            if rand == 'к' and user == 'н':
                rand_ball += 1
            if rand == 'к' and user == 'п':
                user_ball += 1
            if rand == 'н' and user == 'к':
                user_ball += 1
            if rand == 'н' and user == 'п':
                rand_ball += 1
            if rand == 'п' and user == 'н':
                user_ball += 1
            if rand == 'п' and user == 'к':
                rand_ball += 1
        elif user == 'р':
            print('Ваши бали - ', user_ball, '. Бали вашого суперника - ', rand_ball, ".")
        elif user == '-':
            print('Ваши бали - ', user_ball, '. Бали вашого суперника - ', rand_ball, ".")
            print('Кінець гри! Заходьте ще!')
            break
        else:
            print('Введіть к, н или п')

    if start == '-':
        print('Шкода... :(')
    else:
        print('Вибачте, я вас не зрозумів, якщо хочете грати, перезапустіть програму і введіть "+". Дякую!')
