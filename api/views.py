from rest_framework import status
from rest_framework.views import APIView
from .models import StudentModel
from .serializers import StudentSerializers
# Create your views here.
from rest_framework.response import Response

class StudentView(APIView):
    # for all
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu = StudentModel.objects.get(id=id)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)    
        all = StudentModel.objects.all()    
        serializer = StudentSerializers(all,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
