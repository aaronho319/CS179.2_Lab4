from rest_framework import serializers
from .models import User, Cart, Product

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

	class UserSerializer(serializers.Serializer):
		id = serializers.IntegerField(read_only=True)
		email = serializers.EmailField()
		firstName = serializers.CharField(max_length=30)
		lastName = serializers.CharField(max_length=30)
		shippingAddress = serializers.CharField(max_length=300)

		def create(self, validated_data):
		    return User.objects.create(**validated_data)

		def update(self, instance, validated_data):
		    instance.email = validated_data.get('email', instance.email)
		    instance.firstName = validated_data.get('firstName', instance.firstName)
		    instance.lastName = validated_data.get('lastName', instance.lastName)
		    instance.shippingAddress = validated_data.get('shippingAddress', instance.shippingAddress)
		    instance.save()
		    return instance


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'

	class ProductSerializer(serializers.Serializer):
		id = serializers.IntegerField(read_only=True)
		price = serializers.FloatField()
		name = serializers.CharField(max_length=50)
		description = serializers.CharField(max_length=300)

		def create(self, validated_data):
			return Product.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.price = validated_data.get('price', instance.price)
			instance.name = validated_data.get('name', instance.name)
		    instance.description = validated_data.get('description', instance.description)
		    instance.save()
		    return instance


class CartSerializer(serializers.ModelSerializer):
	products = ProductSerializer(many=True)

	class Meta:
		model = Cart
		fields = '__all__'

	class CartSerializer(serializers.Serializer):
		id = serializers.IntegerField(read_only=True)
		cart_code = serializers.CharField(max_length=10)
		totalPrice = serializers.FloatField()
		hashasPaid = serializers.BooleanField()
		product = serializers.ManyToManyField(Product)

		def create(self, validated_data):
			products_data = validated_data.pop('products')
			cart = Cart.objects.create(**validated_data)
			for product_data in products_data:
				Product.object.create(cart=cart, **product_data)

			return cart

		def update(self, instance, validated_data):
		    instance.cart_code = validated_data.get('cart_code', instance.cart_code)
		    instance.totalPrice = validated_data.get('totalPrice', instance.totalPrice)
		    instance.hasPaid = validated_data.get('hasPaid', instance.hasPaid)
		    products_data = validated_data.pop('products')
		    instance.products_data = products_data.id
		    return instance