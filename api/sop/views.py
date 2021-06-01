from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Meter
from .serializers import MeterSerializer

class MeterView(APIView):
    def post(self, request, *args, **kawrgs):
        meter_serializer = MeterSerializer(data=request.data)
        if meter_serializer.is_valid():
            meter_serializer.save()
            return Response('SUCCESS', status=status.HTTP_201_CREATED)
        else:
            return Response('FAIL', status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        queryset = Meter.objects.all()
        serializer = MeterSerializer(queryset, many=True)
        return Response(serializer.data[-1])