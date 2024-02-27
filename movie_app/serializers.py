from rest_framework import serializers

from movie_app.models import Director, Movie, Review



class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class DirectorSerializers(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = '__all__'

    def get_movies_count(self, obj):
        return obj.movies.count()

class MovieSerializers(serializers.ModelSerializer):
    reviews = ReviewSerializers(many=True)
    reting = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_reting(self, obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()

        if total_stars > 0:
            total_stars / num_reviews
        return 0.0
