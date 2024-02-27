from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializers, MovieSerializers, ReviewSerializers


@api_view(['GET', 'POST'])
def director_list(request):
    if request.method == 'GET':
        queryset = Director.objects.all()
        serializer = DirectorSerializers(queryset, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = DirectorSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail(request, id):
    queryset = get_object_or_404(Director, id=id)
    if request.method == 'GET':
        serializer = DirectorSerializers(queryset)
        return Response(serializer.data, status=200)
    elif request.method == 'PUT':
        serializer = DirectorSerializers(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=200)





@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        queryset = Movie.objects.all()
        serializer = MovieSerializers(queryset, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = MovieSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, id):
    queryset = get_object_or_404(Movie, id=id)
    if request.method == 'GET':
        serializer = MovieSerializers(queryset)
        return Response(serializer.data, status=200)
    elif request.method == 'PUT':
        serializer = DirectorSerializers(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=200)


@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == 'GET':
        queryset = Review.objects.all()
        serializer = ReviewSerializers(queryset, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = ReviewSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, id):
    queryset = get_object_or_404(Review, id=id)
    if request.method == 'GET':
        serializer = ReviewSerializers(queryset)
        return Response(serializer.data, status=200)
    elif request.method == 'PUT':
        serializer = DirectorSerializers(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=200)