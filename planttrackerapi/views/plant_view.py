"""Module for Plant views"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from planttrackerapi.models import Plant
from planttrackerapi.serializers import PlantSerializer

class PlantView(ViewSet):
    """Plant ViewSet"""
    def create(self, request):
        """Handle POST operations"""
        new_plant = Plant()
        new_plant.name = request.data["name"]
        new_plant.nickname = request.data["nickname"]
        new_plant.photo_url = request.data["photo_url"]
        new_plant.water_freq = request.data["water_freq"]
        new_plant.fert_freq = request.data["fert_freq"]
        new_plant.sunlight = request.data["sunlight"]
        new_plant.note = request.data["note"]
        new_plant.user = request.auth.user

        new_plant.save()

        serializer = PlantSerializer(new_plant, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single plant"""
        try:
            plant = Plant.objects.get(pk=pk, user=request.auth.user)
            serializer = PlantSerializer(plant, context={'request': request})
            return Response(serializer.data)
        except Plant.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to plant resource"""
        plants = Plant.objects.filter(user=request.auth.user)

        serializer = PlantSerializer(
            plants, many=True, context={'request': request}
        )

        return Response(serializer.data)

    def update(self, request, pk=None):
        """Handle PUT requests for a plant"""
        plant = Plant.objects.get(pk=pk, user=request.auth.user)
        plant.name = request.data["name"]
        plant.nickname = request.data["nickname"]
        plant.photo_url = request.data["photo_url"]
        plant.water_freq = request.data["water_freq"]
        plant.fert_freq = request.data["fert_freq"]
        plant.sunlight = request.data["sunlight"]
        plant.note = request.data["note"]
        plant.user = request.auth.user

        plant.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single plant"""
        try:
            plant = Plant.objects.get(pk=pk, user=request.auth.user)
            plant.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Plant.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
