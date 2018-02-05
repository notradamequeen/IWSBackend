from rest_framework import serializers
from iws.models import Field, RiskType, Form


class FieldSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    field_name = serializers.CharField(required=True, max_length=100)
    data_type = serializers.CharField(required=True, max_length=100)

    class Meta:
        model = Field
        fields = '__all__'
        depth = 2

    def create(self, validated_data):
        return Field.objects.create(**validated_data)


class RiskTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    fields = FieldSerializer(many=True, read_only=True)

    class Meta:
        model = RiskType
        fields = '__all__'

    def create(self, validated_data):
        return RiskType.objects.create(**validated_data)


class FormSerializer(serializers.Serializer):
    field = FieldSerializer()
    risk_type = RiskTypeSerializer()

    class Meta:
        model = Form
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        return Form.objects.create(**validated_data)
