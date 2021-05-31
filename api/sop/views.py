from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MeterSerializer

class MeterView(APIView):
    def post(self, request, *args, **kawrgs):
        meter_serializer = MeterSerializer(data=request.data)
        if meter_serializer.is_valid():
            print(request.data)
            return Response('SUCCESS', status=status.HTTP_201_CREATED)
        else:
            return Response('FAIL', status=status.HTTP_400_BAD_REQUEST)

