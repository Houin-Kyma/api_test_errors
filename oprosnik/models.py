from django.db import models

# Create your models here.

OPTION_TYPES = ['CHOICE', 'MULTIPLE_CHOICE']


class Opros(models.Model):
    # Опрос
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    startDate = models.DateField()
    finishDate = models.DateField()

    def __str__(self):
        return self.description


class Question(models.Model):
    # Вопрос
    opros = models.ForeignKey('Opros', on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    type = models.CharField(max_length=30, default='')



    @property
    def hasOptionType(self):
        return self.type in OPTION_TYPES


class Variant(models.Model):
    # Вариант ответа
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    index = models.PositiveIntegerField()
    text = models.CharField(max_length=100)




class Finishedpoll(models.Model):
    # Заполненный опросник
    userId = models.IntegerField(db_index=True)
    opros = models.ForeignKey('Opros', on_delete=models.CASCADE)
    submitTime = models.DateTimeField(auto_now_add=True)


# При записи ответа на вопрос мы копируем тип и текст вопроса
# Копируем текст вариантов ответа для соответсвующего вопроса


class Answer(models.Model):
    # Ответ на вопрос
    finishedpoll = models.ForeignKey('Finishedpoll', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    questionType = models.CharField(max_length=30)
    questionText = models.CharField(max_length=300)
    answerText = models.CharField(max_length=300)
