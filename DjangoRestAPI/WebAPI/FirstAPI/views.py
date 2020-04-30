from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializer import PersonSerializers
from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class PersonView(generics.ListAPIView):

    queryset = Person.objects.all()
    serializer_class = PersonSerializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ("id","Name")
    search_fields = ('id','Name')









'''class PersonView(APIView):

    def get(self,request,format=None):
        data = Person.objects.all()
        serializer = PersonSerializers(data,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        try:
            serializer = PersonSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)'''

'''global data
data = ["Harsh"]

class Youtube(APIView):

    #def __init__(self):
        self.data = ["Harsh"]

    def get(self,requests,format=None):
        #return Response({"Message":self.data})
        return Response({"Message":data})

    def post(self,requests,format=None):

        MyData = requests.data

        Name = MyData.get("Name",None)

        data.append(Name)

        #self.data.append(Name)
        #print("Data Received : {}".format(data))
        return Response({
            'Response': 200,
            "Data":Name,
            "Message": "Item was added to Database"
                        })

    def put(self,requests,format=None):
        MyData = requests.data
        return Response(
            {"Response":"PUT Works"}
        )'''


