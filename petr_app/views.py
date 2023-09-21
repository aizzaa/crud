from rest_framework.decorators import api_view
from .models import Category, Post, Tag
from .serializers import CategorySerializer
from rest_framework.response import Response


@api_view(['GET'])
def category_list(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def category_create(request):
    serializer = CategorySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    print('==========>', serializer.data)
    return Response(serializer.data, status=201)


@api_view(['GET'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=200)
    except Category.DoesNotExist:
        return Response(f'This category has no pk: {pk}', status=404)


@api_view(['PUT'])
def update(request, pk):
    try:
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    except Category.DoesNotExist:
        return Response(f'This category has no pk: {pk}', status=404)


@api_view(['DELETE'])
def delete(request, pk):
    # try:
    category = Category.objects.get(id=pk)
    print('DELETEEED')
    # except Category.DoesNotExist:
    #     return Response(f'This category has no pk: {pk}', status=404)
    category.delete()
    return Response(f'Your category was deleted', status=204)






