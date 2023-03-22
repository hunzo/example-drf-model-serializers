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



# class Home(APIView):
#     """
#     View to list all users in the system.
#     # test
#     ## test

#     * Requires token authentication.
#     * Only admin users are able to access this view.
#     """

#     def get_object(self, pk=None):
#         try:
#             return Payload.objects.get(pk=pk)
#         except Payload.DoesNotExist:
#             raise Http404

#     def get(self, request, pk=None, format=None):
#         """
#         Return a list of all users.
#         """
#         if pk is None:
#             payload = Payload.objects.all()
#             serializer = PayloadSerializers(payload, many=True)
#             return Response(serializer.data)

#         payload = self.get_object(pk=pk)
#         serializer = PayloadSerializers(payload)

#         return Response(serializer.data)

#     def post(self, request, pk=None):
#         if pk is None:
#             serializer = PayloadSerializers(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         serializer = PayloadSerializers(data=request.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk=None):
#         if pk is None:
#             serializer = PayloadSerializers(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
