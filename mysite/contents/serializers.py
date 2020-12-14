from rest_framework import serializers 
from contents.models import Contents
 
 
class ContentsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Contents
        fields = ('imageurl',
                  'uid',
                  'userid',
                  'timestamp',
                  'favoriteCount',
                  'usertype',
                  'explain'
                  )
