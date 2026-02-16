from rest_framework import serializers
from django.db.models import Avg
from .models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(source='products.count', read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']

    
    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Category name too short")
        return value

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

   
    def validate_title(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Title too short")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0")
        return value


class ProductReviewSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'reviews', 'rating']

    def get_reviews(self, obj):
        from .models import Review
        reviews = Review.objects.filter(product=obj)
        return [
            {
                "id": r.id,
                "text": r.text,
                "stars": r.stars,
                "created_at": r.created_at
            } for r in reviews
        ]

    def get_rating(self, obj):
        avg = obj.reviews.aggregate(avg=Avg('stars'))['avg']
        return round(avg, 2) if avg else None


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'stars', 'product']

    
    def validate_text(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Review text is too short")
        return value

    def validate_stars(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Stars must be between 1 and 5")
        return value

    def validate_product(self, value):
        if not value:
            raise serializers.ValidationError("Product must be specified")
        return value

