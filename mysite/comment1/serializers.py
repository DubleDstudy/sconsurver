from rest_framework import serializers
from comment1.models import Comment1


class Comment1Serializer(serializers.ModelSerializer):

    class Meta:
        model = Comment1
        fields = ('uid',
                  'userid',
                  'comment',
                  'timestamp',
                  )

