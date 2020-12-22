from rest_framework import serializers


class AddNewContactRequestSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=70)
    body = serializers.CharField(max_length=255)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass







