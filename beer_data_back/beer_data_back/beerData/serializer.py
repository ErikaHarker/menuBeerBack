from rest_framework import serializers


class BeerSerializer(serializers.Serializer):
    BeerName = serializers.CharField(max_length=40)
    Descripcion = serializers.CharField(max_length=40)
    Alcohol = serializers.FloatField()
    price = serializers.FloatField()


class BannerSerializer(serializers.Serializer):
    Name = serializers.CharField(max_length=40)
    Title = serializers.CharField(max_length=40)
    Text1 = serializers.CharField(max_length=40)
    Text2 = serializers.CharField(max_length=40)


class FinalDataSerializer(serializers.Serializer):
    BeerMain = BeerSerializer(many=True)
    BeerDown = BeerSerializer()
    Banner = BannerSerializer()



