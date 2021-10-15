# api_test_errors
Попытка по созданию API

Первоначальная установка


```
cd DRF-Poll-Test
pip install -r requirements.txt
cd backend
python manage.py migrate
python manage.py createsuperuser

```


Ошибка происходит при создании POST запроса к API 

POST json

```
[
  {
    "id": 2,
    "name": "Что по чем?",
    "description": "состояние",
    "startDate": "2021-10-14",
    "finishDate": "2021-10-14"
  }
]

```


ответ 

```
AttributeError: 'list' object has no attribute 'get'
[15/Oct/2021 08:59:41] "POST /api/oprosnik/ HTTP/1.1" 500 13538
```


К сожалению опыта не хватило решить эту проблему. :weary:
