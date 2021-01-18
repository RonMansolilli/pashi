from rest_framework import serializers
from housing_app import models


class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            # 'id',
            'zipCode',
            'crimeIndex',
            'crimeCount',
            'crimeRatio',
            'safetyRank'
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

class HousingSerializer(serializers.ModelSerializer):
    # info = NeighborhoodSerializer(many=True, read_only=True)
    # crimeIndex1 = serializers.RelatedField(source='crimeIndex', read_only=True)

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