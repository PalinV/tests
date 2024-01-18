from main import sorted_course, post_yd, popular_name, unique_names
import pytest
from unittest import TestCase

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
              ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
              ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
              ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
              ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
          ]
durations = [14, 20, 12, 20]


class TestYandex(TestCase):
    def test_successful_put(self):
        result = post_yd()
        key = result.json()['name']
        expected ='my_file'
        self.assertEquals(key, expected)

    def test_dict_value(self):
        res = sorted_course(courses, mentors, durations)
        self.assertIn ('Java-разработчик с нуля', res)

    def test_count_value(self):
        res = sorted_course(courses, mentors, durations)
        self.assertEqual(len(res), 4)


@pytest.mark.parametrize(
    'expected',[
        200, 201, 400, 404
    ]
)
def test_successful_answer(expected):
    result = post_yd(my_file='my_file')
    answer = result.status_code
    assert expected <= answer


@pytest.mark.parametrize(
    'expected',[
        'Александр', 'Денис', 'Максим', 'Евгений'
    ]
)
def test_name_in_dict(expected):
    result_dict = popular_name(mentors)
    result = result_dict[expected]
    assert result > 2


@pytest.mark.parametrize(
    'expected', [
        'Александр', 'Денис', 'Максим', 'Евгений'
    ]
)
def test_unique_names(expected):
    result = unique_names(mentors)
    counter = 0
    for name in result:
        if name == expected:
            counter += 1
    assert counter == 1




















