from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "body", "created_at"]

    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Заголовок должен быть не короче 3 символов.")
        return value

    def validate_body(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Текст должен быть не короче 10 символов.")
        return value
