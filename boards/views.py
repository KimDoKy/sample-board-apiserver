from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Board
from .serializers import BoardSerializer

@csrf_exempt
def board_list(request):
    if request.method == 'GET':
        objs = Board.objects.all()
        serializer = BoardSerializer(objs, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def board_detail(request, pk):
    try:
        obj = Board.objects.get(pk=pk)
    except Board.DoesNotExists:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = BoardSerializer(obj)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BoardSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj.delete()
        return JsonResponse({'result': 'success'}, status=200)
