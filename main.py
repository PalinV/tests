import requests
from pprint import pprint

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]


def sorted_course(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title":course, "mentors":mentor, "duration":duration}
        courses_list.append(course_dict)
    durations_dict = {}
    pair = {}
    for id, course in enumerate(courses_list):
        key = course["duration"]
        if key not in durations_dict:
            pair[key] = [id]
            durations_dict = pair
        else:
            durations_dict[key].append(id)
    durations_dict = sorted(durations_dict.items())
    dict_course_duraction = {}
    for duration, id in durations_dict:
        for x in range(len(id)):
            dict_course_duraction[courses[id[x]]] = duration
    return dict_course_duraction


def popular_name(mentors):
    all_list = []
    for m in mentors:
        all_list += (m)
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)
    unique_names = list(set(all_names_list))
    all_names_sorted = sorted(unique_names)
    popular = []
    for name in all_names_sorted:
        popular.append([name, all_names_list.count(name)])
    popular.sort(key=lambda x:x[1], reverse=True)
    counter = 0
    name_count = {}
    for name, count in popular:
        if counter <= 3:
            name_count[name] = count
            counter += 1
        else:
            print(name_count)
            break
    return name_count


def unique_names(mentors):
    all_list = []
    for m in mentors:
        all_list += (m)
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)
    unique_names = list(set(all_names_list))
    all_names_sorted = sorted(unique_names)
    return all_names_sorted

def post_yd(my_file='my_file'):
    url_yd = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    yd_token = 'y0_AgAAAAAyU__bAADLWwAAAADjoZergguARrbYRqGO84emW9w-UcRdiJ4'
    params = {
        'path': my_file,
        'overwrite': 'true'
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(yd_token)
    }
    response = requests.get(url=url_yd, headers=headers, params=params)
    link = response.json()['href']
    requests.put(url=link, data='my_file')
    url_yd_upload = 'https://cloud-api.yandex.net/v1/disk/resources'
    resp = requests.get(url=url_yd_upload, headers=headers, params=params)
    return resp

