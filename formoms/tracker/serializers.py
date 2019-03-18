from rest_framework import serializers
from tracker.models import Tracker

class TrackerSerializer(serializers.HyperlinkedModelSerializer):
    # baby_id = serializers.ReadOnlyField(source='babies.baby_id')

    class Meta:
        model = Tracker
        fields = ('id', 'date', 'height', 'weight', 'baby_id')
        extra_kwargs = {
            'url': {
                'view_name': 'tracker:tracker-detail'
            }
        }