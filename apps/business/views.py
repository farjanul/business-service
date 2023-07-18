from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from apps.business.models import Business
from apps.business.serializers import BusinessSerializer
from apps.business.service import BusinessService


class BusinessViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    lookup_field = "uuid"

    @action(
        detail=False,
        methods=['get'],
        url_name='business-within-10km',
        url_path='within-10km',
    )
    def within_10km(self, request, *args, **kwargs):
        # Retrieve business data within 10km
        try:
            lat = float(request.GET.get('lat'))
            lon = float(request.GET.get('lon'))
        except Exception as _:
            raise ValidationError({'message': 'valid lat and lon must be required'})

        businesses = BusinessService(lat, lon).get_business_location_within_10km()
        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data)

