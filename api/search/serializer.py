from .models import *
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['full_name', 'sex', 'age']

# class AssociatedPersonSerializer(serializers.ModelSerializer):
#     """Used as a nested serializer by MemberSerializer"""
#     person = PersonSerializer(many=True,read_only=True)
#     class Meta:
#         model = AssociatedPerson
#         fields = ['person']

class AssociateSerializer(serializers.ModelSerializer):
    # p = PersonSerializer(read_only=True)

    class Meta:
        model = AssociatedPerson
        fields = ['relation']

class BookSerializer(serializers.ModelSerializer):
    associates = PersonSerializer(many=True,read_only=True)
    genre = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")

    class Meta:
        model = Book
        fields = ["name",
                "description",
                "language",
                "release",
                "created_at",
                "subscriber",
                "url",
                "associates",
                "genre",
                "rating"]
        depth = 2
