from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Inventory.models import ItemType
from Inventory.serializers import ItemTypeSerializer

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def ItemType_list(request):
    if request.method == 'GET':
        snippets = ItemType.objects.all()
        serializer = ItemTypeSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def ItemType_detail(request, pk):
    try:
        itemType = ItemType.objects.get(pk=pk)
    except ItemType.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ItemTypeSerializer(itemType)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemTypeSerializer(itemType, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        itemType.delete()
        return HttpResponse(status=204)
