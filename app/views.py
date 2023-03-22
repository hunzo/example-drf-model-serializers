from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status


from .serializers import PayloadSerializers
from .models import Payload


@api_view(["GET"])
def GetPayloadView(request, pk=None):
    print(pk)
    if pk is None:
        payload = Payload.objects.all()
        serializers = PayloadSerializers(payload, many=True)
    else:
        try:
            payload = Payload.objects.get(pk=pk)
            serializers = PayloadSerializers(payload)
        except Payload.DoesNotExist:
            raise Http404

    return Response(serializers.data)


@api_view(["POST"])
def CreatePayload(request):
    serializes = PayloadSerializers(data=request.data)
    if serializes.is_valid():
        serializes.save()
        return Response(serializes.data, status=status.HTTP_201_CREATED)

    return Response(serializes.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def UpdatePayload(request, pk):
    payload = Payload.objects.get(id=pk)
    serializes = PayloadSerializers(payload, data=request.data)
    if serializes.is_valid():
        serializes.save()
        return Response(serializes.data, status=status.HTTP_201_CREATED)

    return Response(serializes.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def DeletePayload(request, pk):
    try:
        payload = Payload.objects.get(id=pk)
    except Payload.DoesNotExist:
        raise Http404
    payload.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
