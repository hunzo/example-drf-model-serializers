from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from .serializers import PayloadSerializers
from .models import Payload


class Home(APIView):

    def get_object(self, pk=None):
        try:
            return Payload.objects.get(pk=pk)
        except Payload.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):

        if pk is None:
            payload = Payload.objects.all()
            serializer = PayloadSerializers(payload, many=True)
            return Response(serializer.data)

        payload = self.get_object(pk=pk)
        serializer = PayloadSerializers(payload)

        return Response(serializer.data)

    def post(self, request, pk=None):
        if pk is None:
            serializer = PayloadSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
