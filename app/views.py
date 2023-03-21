from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PayloadSerializers
from .models import Payload


class Home(APIView):

    def get(self, request, pk=None):
        if pk:
            all_payload = Payload.objects.filter(pk=pk)
        else:
            all_payload = Payload.objects.all()
        serializer = PayloadSerializers(all_payload, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    def post(self, request, pk=None):
        if pk == None:
            return Response({"test": "test"})
        
        serializer = PayloadSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = PayloadSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
