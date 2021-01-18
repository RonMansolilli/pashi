from rest_framework import serializers
from housing_app import models


class HousingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            # 'created',
            'updated',
            'projectName',
            'management',            
            'zipCode',
            # 'xCoord',        
            # 'yCoord',
            # 'neighborhood',         
            'address',
            'contactPhone',        
            'totalUnits',
            'singleRoom',          
            'studio',
            'oneBedroom',          
            'twoBedroom',
            'threeBedroom',         
            'fourBedroom',
            # 'photo',
        )
        model = models.housing_data

class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'zipCode',
            'crimeIndex',
            'crimeCount',
            'crimeRatio',
            # 'neighborhood',
            # 'quadrant'
            # 'avgRent',
            # 'rentLow',
            # 'rentHigh',
            # 'walkIndex',
            # 'violenceIndex',
            # 'crimeTime',
            # 'avgHomeValue',
        )
        model = models.neighborhood_data

