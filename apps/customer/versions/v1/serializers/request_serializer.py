from rest_framework import serializers


class AddNewContactRequestSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=70)
    body = serializers.CharField(max_length=255)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class DeleteContactRequestSerializer(serializers.Serializer):
    contact_id = serializers.ListField(child=serializers.IntegerField(min_value=0, required=True), required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class AddCreditCardRequestSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    number_credit = serializers.CharField(max_length=20)
    expire_date = serializers.DateField()
    CVV = serializers.IntegerField()
    address = serializers.CharField(max_length=255)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class DeleteCreditCardRequestSerializer(serializers.Serializer):
    credit_card_id = serializers.ListField(child=serializers.IntegerField(min_value=0, required=True), required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class AddBlogsRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=1200)
    author = serializers.CharField(max_length=255)
    image = serializers.CharField(max_length=255)
    like = serializers.IntegerField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class UpdateBlogsRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=1200)
    author = serializers.CharField(max_length=255)
    image = serializers.CharField(max_length=255)
    like = serializers.IntegerField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class DeleteBlogsRequestSerializer(serializers.Serializer):
    blog_id = serializers.ListField(child=serializers.IntegerField(min_value=0, required=True), required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class AddSubscriberRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=70)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class DeleteSubscriberRequestSerializer(serializers.Serializer):
    subscriber_id = serializers.ListField(child=serializers.IntegerField(min_value=0, required=True), required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class AddToCartRequestSerializer(serializers.Serializer):
    item_id = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(default=1)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class DeleteItemFromCartRequestSerializer(serializers.Serializer):
    item_id_list = serializers.ListField(child=serializers.IntegerField(min_value=0, required=True), required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
