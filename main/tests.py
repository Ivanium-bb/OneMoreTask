from django.db.models import Prefetch
from django.test import TestCase, Client

from main.models import FoodCategory, Food
from main.views import FoodView
from main.serializers import FoodSerializer, FoodListSerializer

from django.urls import reverse
from rest_framework import status
from collections import OrderedDict


# client = Client()

class FoodTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.drinks = FoodCategory.objects.create(name_ru="Напитки", order_id=10)

        self.drink1 = Food.objects.create(
            category=self.drinks,
            internal_code=100,
            code=1,
            name_ru="Чай",
            description_ru="Чай 100 гр",
            cost=123.00
        )

        self.drink2 = Food.objects.create(
            category=self.drinks,
            internal_code=200,
            code=2,
            name_ru="Кола",
            description_ru="Кола",
            cost=123.00
        )
        self.drink3 = Food.objects.create(
            category=self.drinks,
            internal_code=300,
            code=3,
            name_ru="Спрайт",
            description_ru="Спрайт",
            cost=123.00
        )
        self.drink4 = Food.objects.create(
            category=self.drinks,
            internal_code=400,
            code=4,
            name_ru="Байкал",
            description_ru="Байкал",
            cost=123.00
        )
        self.drink5 = Food.objects.create(
            category=self.drinks,
            internal_code=500,
            code=5,
            name_ru="Фанта",
            description_ru="Фанта",
            cost=123.00,
            is_publish=False
        )

        self.bakery = FoodCategory.objects.create(name_ru="Выпечка", order_id=20)
        self.bakery1 = Food.objects.create(
            category=self.bakery,
            internal_code=222,
            code=22,
            name_ru="Печенье",
            description_ru="Печенье 100 гр",
            cost=123.00
        )
        self.bakery2 = Food.objects.create(
            category=self.bakery,
            internal_code=333,
            code=33,
            name_ru="Хлеб",
            description_ru="Хлеб",
            cost=123.00
        )
        self.bakery3 = Food.objects.create(
            category=self.bakery,
            internal_code=444,
            code=44,
            name_ru="Пирог",
            description_ru="Пирог",
            cost=123.00
        )
        self.bakery4 = Food.objects.create(
            category=self.bakery,
            internal_code=555,
            code=55,
            name_ru="Беляш",
            description_ru="Беляш",
            cost=321.00,
            is_publish=False
        )

        self.side_dish = FoodCategory.objects.create(name_ru="Гарниры", order_id=30)
        self.side_dish1 = Food.objects.create(
            category=self.side_dish,
            internal_code=112,
            code=1,
            name_ru="Пюре",
            description_ru="Пюре",
            cost=123.00,
            is_publish=False
        )
        self.first_dish = FoodCategory.objects.create(name_ru="Первые блюда", order_id=30)

    def test_FoodView(self):
        result = [

            {
                "id": 2,
                "name_ru": "Выпечка",
                "name_en": 'null',
                "name_ch": 'null',
                "order_id": 20,
                "foods": [
                    {
                        "internal_code": 222,
                        "code": 22,
                        "name_ru": "Печенье",
                        "description_ru": "Печенье 100 гр",
                        "description_en": 'null',
                        "description_ch": 'null',
                        "is_vegan": 'false',
                        "is_special": 'false',
                        "cost": "123.00",
                        "additional": [

                        ]
                    },
                    {
                        "internal_code": 333,
                        "code": 33,
                        "name_ru": "Хлеб",
                        "description_ru": "Хлеб",
                        "description_en": 'null',
                        "description_ch": 'null',
                        "is_vegan": 'false',
                        "is_special": 'false',
                        "cost": "123.00",
                        "additional": [

                        ]
                    },
                    {
                        "internal_code": 444,
                        "code": 44,
                        "name_ru": "Пирог",
                        "description_ru": "Пирог",
                        "description_en": 'null',
                        "description_ch": 'null',
                        "is_vegan": 'false',
                        "is_special": 'false',
                        "cost": "123.00",
                        "additional": [

                        ]
                    },
                ]
            },
            {
                "id": 1,
                "name_ru": "Напитки",
                "name_en": 'null',
                "name_ch": 'null',
                "order_id": 10,
                "foods": [
                    {
                        "internal_code": 100,
                        "code": 1,
                        "name_ru": "Чай",
                        "description_ru": "Чай 100 гр",
                        "description_en": 'null',
                        "description_ch": 'null',
                        "is_vegan": 'false',
                        "is_special": 'false',
                        "cost": "123.00",
                        "additional": [

                        ]
                    },
                    {
                        "internal_code": 200,
                        "code": 2,
                        "name_ru": "Кола",
                        "description_ru": "Кола",
                        "description_en": 'null',
                        "description_ch": 'null',
                        "is_vegan": 'false',
                        "is_special": 'false',
                        "cost": "123.00",
                        "additional": [

                        ]
                    },
                    {
                        "internal_code": 300,
                        "code": 3,
                        "name_ru": "Спрайт",
                        "description_ru": "Спрайт",
                        "description_en": 'null',
                        "description_ch": 'null',
                        "is_vegan": 'false',
                        "is_special": 'false',
                        "cost": "123.00",
                        "additional": [

                        ]
                    },
                    {
                        "internal_code": 400,
                        "code": 4,
                        "name_ru": "Байкал",
                        "description_ru": "Байкал",
                        "description_en": 'null',
                        "description_ch": 'null',
                        "is_vegan": 'false',
                        "is_special": 'false',
                        "cost": "123.00",
                        "additional": [

                        ]
                    }
                ]
            }
        ]

        response = self.client.get('/api/v1/foods/')
        result = list(map(OrderedDict, result))
        self.assertEqual(response.data, result)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
