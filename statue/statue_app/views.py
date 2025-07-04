from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Statue
from .serializers import StatueSerializer





@api_view(['GET', 'POST'])
def statue_list(request):
    if request.method == 'GET':
        statues = Statue.objects.all().order_by('-id')  # Show latest first
        serializer = StatueSerializer(statues, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StatueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def statue_detail(request, pk):
    """
    Retrieve a single statue by ID.
    """
    statue = get_object_or_404(Statue, pk=pk)
    serializer = StatueSerializer(statue)
    return Response(serializer.data)

