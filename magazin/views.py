from rest_framework.decorators import api_view
from rest_framework.response import Response
from magazin.serializers import ProductSerializer
from .models import Product
from rest_framework import status

@api_view(['GET'])
def product_list_view(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data
    return Response(data)


@api_view(['GET'])
def product_detail_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': "Продукт не найден"})
    data = ProductSerializer(product).data
    return Response(data=data)


@api_view(['GET'])
def test(request):
    context = {
        'name': "John",
        'age': 12,
        'hobby': 'swimming',
        'boolean': True,
        'list': [
            '1', '2', '3'
        ]
    }

    return Response(data=context)
