from rest_framework import serializers


class BeerSerializer(serializers.Serializer):
    BeerName = serializers.CharField(max_length=40)
    Description = serializers.CharField(max_length=40)
    Alcohol = serializers.FloatField()
    price = serializers.FloatField()


class FooterSerializer(serializers.Serializer):
    Name = serializers.CharField(max_length=40)
    Title = serializers.CharField(max_length=40, allow_blank=True)
    Text1 = serializers.CharField(max_length=40, allow_blank=True)
    Text2 = serializers.CharField(max_length=40, allow_blank=True)


class FinalDataSerializer(serializers.Serializer):
    BeerMain = BeerSerializer(many=True)
    BeerDown = BeerSerializer()
    Footer = FooterSerializer()
