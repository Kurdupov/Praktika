from tkinter import *


# функція для обрахунку
def result():
    ships = {
        'Авіаносець': 100,
        'Лінкор': 150,
        'Крейсер': 175,
        'Eсмінець': 190,
        'Cубмарина': 300
    }

    ranks = {
        1: 1000,
        2: 1500,
        3: 2000,
        4: 5000,
        5: 10000,
    }

    rank_names = {
        1: 'Матрос',
        2: 'Старшина',
        3: 'Мічман',
        4: 'Капітан',
        5: 'Адмірал',
    }

    # перевіряємо чи вибрано тип корабля
    if not ship_type.get(ANCHOR):
        status.set('Виберіть тип корабля')

    # перевіряємо чи вибраний ранг
    elif not rank.get():
        status.set('Виберіть звання')

    # перевіряємо чи обраховуємо для декількох людей, та чи коректна кількість людей
    elif not count_p.get().isdigit() and confirm_value.get():
        status.set('Не правильно введено кількість моряків \n введіть ціле число')

    else:
        # якщо всі данні підходять
        res = (ships[ship_type.get(ANCHOR)] + ranks[rank.get()]) * count_months.get()

        if confirm_value.get():
            res *= int(count_p.get())

        status_text = f'Розрахований розмір заробітної плати.\n Звання - {rank_names[rank.get()]}\n' \
                      f'Тип корабля - {ship_type.get(ANCHOR)}\n Кількість місяців - {count_months.get()}\n'

        if confirm_value.get():
            status_text += f'Кількість людей - {count_p.get()}\nЗаробітня плата - {res}'
        else:
            status_text += f'Заробітня плата - {res}'

        status.set(status_text)


def changeText(text):
    status.set(text)


root = Tk()

root['bg'] = '#87CEFA'
root.title('Моряк - Розрахунок заробітньої плати')
root.geometry("500x700")
root.minsize(300, 700)

# розмістимо лейбли-контейнери
# label для кнопок вибору звання
rank_container = Label(root, bd=0, pady=5, justify=CENTER, )
rank_container.pack(side=TOP, expand=True, fill=BOTH)

ship_type_container = Label(root, bg='blue', bd=0, height=5)
ship_type_container.pack(side=TOP, expand=True, fill=BOTH)

months_container = Label(root, bd=0, height=0)
months_container.pack(side=TOP, expand=True, fill=BOTH)

infotable_container = Label(root, bg='#87CEFA', bd=0, justify=CENTER, height=20)
infotable_container.pack(side=TOP, expand=True, fill=BOTH)

sev_people = Label(root, bg='#87CEFA', bd=0, justify=CENTER)
sev_people.pack(side=TOP, expand=True, fill=BOTH)

# головний екран
status = StringVar()
status.set('')

infotable = Label(infotable_container, bd=0, textvariable=status, font='Arial', bg='#87CEFA', height=19, justify=CENTER)
infotable.pack(side=TOP, fill=BOTH, expand=True)

# радіо звання
rank = IntVar()
rank.set(0)

# заголовок блоку
choicerank = Label(rank_container, text='Оберіть звання: ', font='Arial 12', bd=0, bg='#66FFFF')
choicerank.pack(side=TOP, expand=True, fill=BOTH)

# перемикачі
rank1 = Radiobutton(rank_container, text="Матрос", value=1, font='Arial 12', variable=rank, bg='#87CEFA', bd=0,
                    height=2,
                    activebackground='#00CCCC')
rank1.pack(side=LEFT, fill=BOTH, expand=True)

rank2 = Radiobutton(rank_container, text="Старшина", font='Arial 12', value=2, variable=rank, bg='#87CEFA', bd=0,
                    height=2,
                    activebackground='#00CCCC')
rank2.pack(side=LEFT, fill=BOTH, expand=True)

rank3 = Radiobutton(rank_container, text="Мічман", font='Arial 12', value=3, variable=rank, bg='#87CEFA', bd=0,
                    height=2,
                    activebackground='#00CCCC')
rank3.pack(side=LEFT, fill=BOTH, expand=True)

rank4 = Radiobutton(rank_container, text="Капітан", font='Arial 12', value=4, variable=rank, bg='#87CEFA', bd=0,
                    height=2,
                    activebackground='#00CCCC')
rank4.pack(side=LEFT, fill=BOTH, expand=True)

rank5 = Radiobutton(rank_container, text="Адмірал", font='Arial 12', value=5, variable=rank, bg='#87CEFA', bd=0,
                    height=2,
                    activebackground='#00CCCC')
rank5.pack(side=LEFT, fill=BOTH, expand=True)

# тип корабля
ship_types = ['Авіаносець', 'Лінкор', 'Крейсер', 'Eсмінець', 'Cубмарина']

# заголовок
choicetype = Label(ship_type_container, text='Оберіть тип корабля: ', bd=0, bg='#66FFFF', font='Arial 12')
choicetype.pack(side=TOP, expand=True, fill=BOTH)

# список
ship_type = Listbox(ship_type_container, bd=0, bg='#88CEFA', font='Arial 12 ', height=5, selectbackground='#00CCCC')

for st in ship_types:
    ship_type.insert(END, st)

ship_type.pack(side=TOP, expand=True, fill=BOTH)

# кількість місяців
countmonths_label = Label(months_container, font='Arial 12', text='Кількість місяців: ', bd=0, bg='#66FFFF')
countmonths_label.pack(side=TOP, expand=True, fill=BOTH)

# змінна для збергіання кількісті місяців
count_months = IntVar()

months = Scale(months_container, from_=3, to=36, bg='#87CEFA', font='Arial 12', orient='horizontal',
               troughcolor='#00CCCC',
               activebackground="#04819E", variable=count_months)
months.pack(side=TOP, expand=True, fill=BOTH)

# обрахунок для декількох людей
confirm_value = IntVar()
confirm_value.set(0)

count_p = StringVar()
count_people = Entry(sev_people, bg='#00CCCC', font='Arial 12', width=400, state=DISABLED, disabledbackground='#87CEFA',
                     textvariable=count_p)


# функція для розблокування поля вводу
def checkbox():
    if confirm_value.get():
        count_people['state'] = NORMAL
    else:
        count_people['state'] = DISABLED


confirm = Checkbutton(sev_people, bg='#00CCCC', text='Декілька людей ?', font='Arial 12', activebackground='#87CEFA',
                      offvalue=0,
                      onvalue=1, variable=confirm_value, command=checkbox)
confirm.pack(side=LEFT, expand=True, fill=BOTH)

count_people.pack(side=LEFT, expand=True, fill=BOTH)

# кнопка обрахунку результату
result = Button(root, text='Розрахувати заробітну плату', justify=CENTER, bd=0, font='Arial 12 bold', bg='#00CCCC',
                activebackground='#04859D', command=result)
result.pack(side=TOP, expand=True, fill=BOTH)

# про програму, використовуєм ламбда функцію для того щоб передати параметр у change text
about = Button(root, height=2, text='Про програму', justify=CENTER, bd=0, font='Arial 12 bold', bg='#00CCCC',
               activebackground='#04859D', command=lambda: changeText('Робота з навчальної практики\n '
                                                                      'Виконав:\nстудент гр.  КН-Б19_д/122_Ф\n '
                                                                      'Курдупов О.В.'))
about.pack(side=TOP, expand=True, fill=BOTH)

if __name__ == "__main__":
    root.mainloop()
