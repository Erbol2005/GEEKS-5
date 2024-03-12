from rest_framework import serializers

from movie_app.models import Director, Movie, Review



def validate_name_min_length(value, min_length):
    if len(value) < min_length:
        raise serializers.ValidationError(f'Минимальная длина для заполнения равна {min_length}')
    return value


class DirectorSerializers(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = '__all__'

    def get_movies_count(self, obj):
        return obj.movies.count()

    def validate_name(self, value):
        validate_name_min_length(value, min_length=5)

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_text(self, value):
        validate_name_min_length(value, min_length=5)

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

    def validate_title(self, value):
        validate_name_min_length(value, min_length=1)