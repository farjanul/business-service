from math import radians, cos

from apps.business.models import Business


class BusinessService:

    def __init__(self, lat, lon):
        self.__lat = lat
        self.__lon = lon

    def get_business_location_within_10km(self):
        radius = 10

        # Convert the target latitude and longitude to radians
        target_lat_rad = radians(self.__lat)

        # Perform the filter operation
        businesses = Business.objects.filter(
            latitude__range=(
                self.__lat - radius / 111,
                self.__lat + radius / 111,
            ),
            longitude__range=(
                self.__lon - radius / (111 * cos(target_lat_rad)),
                self.__lon + radius / (111 * cos(target_lat_rad)),
            )
        )
        return businesses
