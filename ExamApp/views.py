from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ExamApp.models import QuestionDb  
from ExamApp.serializers import QuestionSerializer #we use Exam App because serializer is in that folder

# Create your views here.
class QuestionListCreateView(APIView):
    def get(self,request):
        qs=QuestionDb.objects.all()
        serializer_instance=QuestionSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            QuestionDb.objects.create(**actual_data)
            return Response(data={
                "Message":"Question Created Successfully"
            })
        else:
            return Response(data={"Error":serializer_instance.errors})

class QuestionRetreiveView(APIView):
    def get(self,request,pk):
        qs=QuestionDb.objects.get(id=pk)
        serializer_instance=QuestionSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk):
        form_data=request.data
        serializer_instance=QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            QuestionDb.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        qs=QuestionDb.objects.filter(id=pk).delete()
        serializer_instance=QuestionSerializer(qs)
        return Response(
            {
                "Message":"Deleted Succsesfully"
            }
        )

    

    
