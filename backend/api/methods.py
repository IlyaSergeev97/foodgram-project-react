import api.serializers
from api.models import Recipe
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response


def post_delete_favorite_shopping_cart(request, model, id):
    user = request.user
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        model.objects.create(user=user, recipe=recipe)
        serializer = api.serializers.RecipeToRepresentationSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    obj = get_object_or_404(model, user=user, recipe=recipe)
    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def favorited_and_shoping_cart(self, models, obj):
    request = self.context.get('request')
    if not request or request.user.is_anonymous:
        return False
    return models.objects.filter(user=request.user, recipe=obj).exists()
