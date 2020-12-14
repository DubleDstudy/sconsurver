from rest_framework import serializers
from ripple.models import Ripple


class RippleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ripple
        fields = ('uid',
                  'userid',
                  'comment',
                  'timestamp',
                  )

~

