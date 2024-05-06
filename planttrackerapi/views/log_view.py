"""Module for Log views"""
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from planttrackerapi.models import Log, Plant
from planttrackerapi.serializers import LogSerializer
from datetime import datetime

class LogView(ViewSet):
    """Log ViewSet"""
    def create(self, request):
        """Handle POST operations"""
        new_log = Log()
        new_log.plant = Plant.objects.get(pk=request.data["plant_id"])
        new_log.user = request.auth.user
        new_log.date = datetime.now()
        new_log.type = request.data["type"]

        try:
            new_log.save()
            serializer = LogSerializer(new_log, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single log"""
        try:
            log = Log.objects.get(pk=pk)
            serializer = LogSerializer(log, context={'request': request})
            return Response(serializer.data)
        except Log.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to log resource for current user"""
        logs = Log.objects.filter(user=request.auth.user)

        serializer = LogSerializer(
            logs, many=True, context={'request': request}
        )

        return Response(serializer.data)

    def update(self, request, pk=None):
        """Handle PUT requests for a log"""
        log = Log.objects.get(pk=pk)
        log.plant = Plant.objects.get(pk=request.data["plant_id"])
        log.user = request.auth.user
        log.date = request.data["date"]
        log.type = request.data["type"]

        log.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single log"""
        try:
            log = Log.objects.get(pk=pk)
            log.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Log.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)