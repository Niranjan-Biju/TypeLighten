from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def passage(request):
    display_passage = {'person': 'Niranjan', 'age':20}
    return Response(display_passage)