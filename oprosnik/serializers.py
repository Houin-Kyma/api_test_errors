from rest_framework import serializers

from .models import Opros


class OprosSerializer(serializers.Serializer):
    # Опрос
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=300)
    startDate = serializers.DateField()
    finishDate = serializers.DateField()

    def create(self, validated_data):
        return Opros.objects.create(**validated_data)


class QuestionSerializer(serializers.Serializer):
    # Вопрос
    id = serializers.IntegerField(required=False)
    type = serializers.CharField(max_length=30)
    text = serializers.CharField(max_length=300)


class VariantSerializer(serializers.Serializer):
    # Вариант ответа
    id = serializers.IntegerField(required=False)
    index = serializers.IntegerField(required=False)
    text = serializers.CharField(max_length=100)


class UserAnswerSerializer(serializers.Serializer):
    # Вариант ответа пользователя
    index = serializers.IntegerField()
    text = serializers.CharField(max_length=100)


class FinishedpollSerializer(serializers.Serializer):
    # Заполненный опрос
    id = serializers.IntegerField()
    submitTime = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S')
