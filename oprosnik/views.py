from datetime import date

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Opros, Question, Variant, Finishedpoll, Answer
from .serializers import *


# Create your views here.


class OprosView(APIView):
    def get(self,request):
        today = date.today()
        oprosSet = Opros.objects.all()
        # параметр many сообщает сериализатору, что он будет сериализовать более одного опроса.
        return Response(OprosSerializer(oprosSet,many=True).data)

    def post(self,request):
        opros = request.data.get('opros')

        # Создайте опрос из приведенных выше данных
        serializer = OprosSerializer(data = opros)
        if serializer.is_valid(raise_exception=True):
            opros_saved = serializer.save()
        return Response({"success": "Opros '{}' created successfully".format(opros_saved.title)})



    

