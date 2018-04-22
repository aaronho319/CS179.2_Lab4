from user.models import User
from cart.models import Cart
from product.models import Product
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status

# user
class UserList(APIView) :
	def get(self, request, format=None) :
		users = User.object.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request, format=None) :
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView) :
	def get_object(self, pk) :
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None) :
		user = self.get_object(pk)
		serializer = UserSerializer(user)
		return Response(serializer.data)

	def put(self, request, pk, format=None) :
		user = self.get_object(pk)
		serializer = UserSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None) :
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_200_NO_CONTENT)

# carts
class CartList(APIView) :
	def get(self, request, format=None) :
		carts = Cart.object.all()
		serializer = CartSerializer(carts, many=True)
		return Response(serializer.data)

	def post(self, request, format=None) :
		serializer = cartSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartDetail(APIView) :
	def get_object(self, pk) :
		try:
			return Cart.objects.get(pk=pk)
		except Cart.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None) :
		cart = self.get_object(pk)
		serializer = CartSerializer(cart)
		return Response(serializer.data)

	def put(self, request, pk, format=None) :
		cart = self.get_object(pk)
		serializer = CartSerializer(cart, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None) :
		cart = self.get_object(pk)
		cart.delete()
		return Response(status=status.HTTP_200_NO_CONTENT)

# product
class ProductList(APIView) :
	def get(self, request, format=None) :
		products = Product.object.all()
		serializer = ProductSerializer(products, many=True)
		return Response(serializer.data)

	def post(self, request, format=None) :
		serializer = ProductSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView) :
	def get_object(self, pk) :
		try:
			return Product.objects.get(pk=pk)
		except Product.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None) :
		product = self.get_object(pk)
		serializer = ProductSerializer(product)
		return Response(serializer.data)

	def put(self, request, pk, format=None) :
		product = self.get_object(pk)
		serializer = ProductSerializer(product, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None) :
		product = self.get_object(pk)
		product.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)