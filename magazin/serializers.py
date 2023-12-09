from rest_framework import serializers
from .models import Product, Category, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    # category = CategorySerializer()
    # reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        # fields = '__all__'
        fields = 'id title created_at category reviews count_reviews all_reviews'.split()

    # def get_category(self, product):
    #     return CategorySerializer(product.category).data

    def get_category(self, product):
        try:
            return product.category.name
        except:
            return 'No category'

    def get_reviews(self, product):
        serializer = ReviewSerializer(Review.objects.filter(author__isnull=False, product=product),
                                      many=True)
        #serializer = ReviewSerializer(product.reviews.all(), many=True)
        return serializer.data
