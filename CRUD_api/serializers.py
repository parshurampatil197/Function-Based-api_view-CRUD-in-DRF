from rest_framework import serializers
from .models import Items


class ItemSerializer(serializers.ModelSerializer):
    category = serializers.CharField(required=True)
    subcategory = serializers.CharField(required=True)
    name = serializers.CharField()
    amount = serializers.IntegerField()

    class Meta:
        model = Items
        fields = '__all__'

    def create(self, validated_data):
        return Items.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     pass


