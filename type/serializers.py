# movie_api/movies/serializers.py

from rest_framework import serializers
from .models import Type

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type # 모델 설정
        fields = ('item','price','color','size','sajin') # 필드 설정