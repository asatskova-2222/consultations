from datetime import datetime
from .storage import Storage
from .service import Service


def dt(s):
    return datetime.strptime(s, '%d.%m.%Y %H:%M')


def seed(service):
    service.add_interval(dt('01.10.2026 10:00'), dt('01.10.2026 10:30'))
    service.add_interval(dt('01.10.2026 11:00'), dt('01.10.2026 11:30'))
    service.add_interval(dt('02.10.2026 14:00'), dt('02.10.2026 14:30'))
    service.add_participant('Иван', 'ivan@mail.ru')
    service.add_participant('Мария', 'maria@mail.ru')


def main():
    storage = Storage()
    service = Service(storage)
    seed(service)

    while True:
        print()
        print('1. Свободные интервалы')
        print('2. Все интервалы')
        print('3. Записаться')
        print('4. Показать все записи')
        print('0. Выход')
        choice = input('> ').strip()

        if choice == '0':
            break
        elif choice == '1':
            free = service.free_intervals()
            if not free:
                print('Свободных нет.')
            for i in free:
                print(' ', i)
        elif choice == '2':
            for i in storage.intervals.values():
                mark = 'занят' if storage.is_busy(i.id) else 'свободен'
                print(f'  {i} - {mark}')
        elif choice == '3':
            try:
                iid = int(input('ID интервала: '))
                pid = int(input('ID участника: '))
                b = service.book(iid, pid)
                print(f'Запись #{b.id} создана')
            except ValueError as e:
                print(f'Ошибка: {e}')
        elif choice == '4':
            bookings = list(storage.bookings.values())
            if not bookings:
                print('Записей нет.')
            else:
                print('Записи:')
                for b in bookings:
                    interval = storage.intervals.get(b.interval_id)
                    participant = storage.participants.get(b.participant_id)
                    print(f'  Запись #{b.id}')
                    print(f'    Интервал: {interval}')
                    if participant:
                        print(f'    Участник: {participant.name} ({participant.contact})')
        else:
            print('Нет такой команды.')


if __name__ == '__main__':
    main()