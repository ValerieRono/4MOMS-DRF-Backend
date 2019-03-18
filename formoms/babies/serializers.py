from rest_framework import serializers
from babies.models import Babies

class BabiesSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Babies
        fields = ('id', 'name', 'birth_date', 'weight_at_birth',
                    'height_at_birth', 'parent_id')
        extra_kwargs = {
            'url': {
                'view_name': 'babies:baby-detail'
            }
        }