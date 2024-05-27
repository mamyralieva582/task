from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MySerializer

@api_view(['GET'])
def my_view(request):
    data = {'name': 'Alice', 'age': 30}
    serializer = MySerializer(data)
    return Response(serializer.data)