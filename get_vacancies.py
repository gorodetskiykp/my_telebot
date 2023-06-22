import requests

def get_vacancies():
    url = 'https://api.hh.ru/vacancies'
    resp = requests.get(url=url)

    response = []
    if resp.status_code == 200:
        json_data = resp.json()
        vacancies = json_data.get('items')

        if vacancies:
            response.append(f"Найденные вакансии: {len(vacancies)}\n")

            for vac in vacancies:
                title = vac.get('name')
                employer = vac.get('employer').get('name')
                response.append(f"Специализация: {title}")
                response.append(f"Работадатель: {employer}")
                response.append("-" * 80)
        else:
            response.append("Вакансии не найдены")
    else:
        response.append("Нет данных")

    return '\n'.join(response)
