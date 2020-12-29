#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Решить индивидуальное задание лабораторной работы 6, оформив каждую команду в виде
#отдельной функции

#  Использовать словарь, содержащий следующие ключи: название пункта назначения; номер
# рейса; время посадки. Написать программу, выполняющую следующие действия: ввод
# с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
# быть упорядочены по времени посадки; вывод на экран информации о рейсах,
# направляющихся в пункт, название которого введено с клавиатуры; если таких рейсов нет,
# выдать на дисплей соответствующее сообщение.

import sys
import json


def add(aircraft, name, number, time):
    plane = {
        'name': name,
        'number': number,
        'time': time,
    }

    aircraft.append(plane)
    if len(aircraft) > 1:
        aircraft.sort(key=lambda item: item.get('time', ''))


def list(aircraft):
    table = []
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 17
    )
    table.append(line)
    table.append(
        '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
            "№",
            "Пункт назначения",
            "Номер рейса",
            "Время посадки"
        )
    )
    table.append(line)

    for idx, plane in enumerate(aircraft, 1):
        table.append(
            '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                idx,
                plane.get('name', ''),
                plane.get('number', ''),
                plane.get('time', 0)
            )
        )

    table.append(line)

    return '\n'.join(table)


def select(aircraft, period):

    result = []
    for plane in aircraft:
        if period == plane.get('name'):
            result.append(plane)

    return result


def load(filename):
    with open(filename, 'r') as fin:
        return json.load(fin)


def save(trains, filename):
    with open(filename, 'w') as fout:
        json.dump(trains, fout)


if __name__ == '__main__':
    aircraft = []

    while True:
        command = input(">>> ")

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Пункт назначения ")
            number = input("Номер рейса ")
            time = input("Время посадки ")

            add(aircraft, name, number, time)

        elif command == 'list':
            print(list(aircraft))

        elif command.startswith('select '):
            parts = command.split(maxsplit=1)
            selected = select(aircraft, parts[1])
            count = 0
            if selected:
                for idx, plane in enumerate(selected, 1):
                    print(
                        '{:>4}: {}, номер рейса - {}, время посадки - {}'.format(count, plane.get('name', ''),
                                                                                      plane.get('number', ''),
                                                                                      plane.get('time', ''))
                    )
            else:
                print("Таких пунктов назначения не найдено.")


        elif command.startswith('load '):
            parts = command.split(maxsplit=1)
            aircraft = load(parts[1])

        elif command.startswith('save '):
            parts = command.split(maxsplit=1)
            save(aircraft, parts[1])

        elif command == 'help':
            print("Список команд:\n")
            print("add - Добавить данные;")
            print("list - Вывести данные;")
            print("select <Город> - Вывести всю информацию  по городу;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
