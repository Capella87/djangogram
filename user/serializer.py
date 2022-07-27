from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.Serializer):
    # pk = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100)
    birthday = serializers.DateField()
    website = serializers.CharField(allow_null=True)
    shown_name = serializers.CharField(max_length=100, allow_null=True)
    gender = serializers.IntegerField()
    bio = serializers.CharField(allow_null=True)
    is_private = serializers.BooleanField(default=False)
    picture = serializers.ImageField(default=None, allow_null=True)

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.website = validated_data.get('website', instance.website)
        instance.shown_name = validated_data.get('shown_name', instance.shown_name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.is_private = validated_data.get('is_private', instance.is_private)
        instance.picture = validated_data.get('picture', instance.picture)

        instance.save()
        return instance

    class Meta:
        model = Profile
        fields = [
            'username',
            'birthday',
            'website',
            'shown_name',
            'gender',
            'bio',
            'is_private',
            'picture',
        ]

