import requests
import json


class HeadHunterAPI:
    """
    Класс для работы с API HeadHunter
    """
    url_vacancies = 'https://api.hh.ru/vacancies'
    url_employers = 'https://api.hh.ru/employers'

    def get_vacancies(self, params):
        req = requests.get(HeadHunterAPI.url_vacancies, params)  # Посылаем запрос к API
        data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
        req.close()
        data = json.loads(data)

        return data['items']

    def get_employer(self, employer_id):

        url = f"{HeadHunterAPI.url_employers}/{employer_id}"
        req = requests.get(url)  # Посылаем запрос к API

        if not req.status_code == 200:
            req.close()
            return None

        data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
        req.close()
        data = json.loads(data)

        return data

    @staticmethod
    def get_solary_representation(salary_hh):
        if salary_hh is None:
            return 0
        salary_from = salary_hh['from']
        if salary_from is not None:
            return salary_from
        else:
            return 0

