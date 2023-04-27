from rest_framework import serializers
from restapi.models import Course

#validators
def fee_range(value):
    if value not in range(10000,50000):
        raise serializers.ValidationError('Course fee is very high or low please check it again')

class CourseSerializer(serializers.Serializer):
    course_name = serializers.CharField(max_length=30)
    dur = serializers.IntegerField()
    fee = serializers.IntegerField(validators=[fee_range])
    trainer = serializers.CharField(max_length=40)

    def create(self,validate_data):
        return Course.objects.create(**validate_data)
    
    def update(self,instance,validated_data):
        instance.course_name = validated_data.get('course_name',instance.course_name)
        instance.dur = validated_data.get('dur',instance.dur)
        instance.fee = validated_data.get('fee',instance.fee)
        instance.trainer = validated_data.get('trainer',instance.trainer)
        instance.save()
        return instance

    #object level validation
    def validate(self,data):
        cname = data.get('course_name')
        trainer = data.get('trainer')
        if cname.lower()not in ['python','django','sql']and trainer not in ['sonu','tabu']:
            raise serializers.ValidationError('invalid course and trainer')
        return data

    #Field level validation
    def validation_dur(self,value):
        if value>100:
            raise serializers.ValidationError("Duration should be with in 100 hours")
        return value
    

    def delete(self):
        pass