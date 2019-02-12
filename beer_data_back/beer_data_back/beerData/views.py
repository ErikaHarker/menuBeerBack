from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
import json


@api_view(['POST'])
def BeerView(request):
    if request.method == "POST":
        serializer = FinalDataSerializer(data=request.data)
        if serializer.is_valid():
            fileName = 'dataBeer.json'

            with open(fileName, 'w') as file:
                json.dump(serializer.data, file, indent=4)

            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        else:

            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
