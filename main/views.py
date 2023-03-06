from django.db.models import Prefetch
from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from main.models import FoodCategory, Food
from main.serializers import FoodListSerializer


class FoodView(mixins.ListModelMixin, GenericAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        queryset = FoodCategory.objects.filter(food__is_publish=True).prefetch_related(
            Prefetch("food", queryset=Food.objects.filter(is_publish=True))).distinct()
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
