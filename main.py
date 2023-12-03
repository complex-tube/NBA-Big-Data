import threading

from frameworks.ui import UI


def download_games():
    global ui
    ui.download_games_option_chosen()


def download_stats():
    global ui
    ui.download_stats_option_chosen()


ui = UI()
ui.launch_elk_clicked()
ui.connect_to_elastic()

print("Теперь можно зайти по адресу localhost:5601 и работать в Kibana")
print("Если нужно дополнительное взаимодействие, есть несколько опций")
print("Выберите один из вариантов.")
print("1. Скачивание статистики данных за все время по игрокам и играм с ресурса.")
print("2. Загрузка скачанных данных на локальный сервер ELK.")
print("3. Выход.")

choice = input("Ваш выбор: ")
while not choice.isdecimal():
    choice = input("Ваш выбор: ")

continue_program = 1

while int(continue_program) != 0:
    while not choice.isdecimal() or (int(choice) != 1 and int(choice) != 2 and int(choice) != 3):
        print("Пожалуйста, выберите из доступных ранее вариантов")
        choice = input()
    if int(choice) == 1:
        print("Вы выбрали вариант 1")
        games_thread = threading.Thread(target=download_games)
        stats_thread = threading.Thread(target=download_stats)
        games_thread.start()
        stats_thread.start()
        games_thread.join()
        stats_thread.join()
    elif int(choice) == 2:
        print("Вы выбрали вариант 2")
        ui.launch_logstash_clicked()
    elif int(choice) == 3:
        print("Вы выбрали вариант 3")
        ui.exit()
        input("Для выключение нажмите клавишу enter")
        exit(0)
    print("Желаете продолжить работу?")
    print("Да - 1")
    print("Нет - 0")

    continue_program = input("Ваш выбор: ")
    choice = str(0)
    while not continue_program.isdecimal() or (int(continue_program) != 1 and int(continue_program) != 0):
        continue_program = input("Ваш выбор: ")
print("Конец работы")
