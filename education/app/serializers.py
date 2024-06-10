from rest_framework import serializers
from .models import Course,Teacher,Student

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price=serializers.IntegerField()
    lifetime=serializers.IntegerField()

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.lifetime = validated_data.get('lifetime', instance.lifetime)
        instance.save()
        return instance


class TeacherSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(max_length=255)
    status=serializers.IntegerField()
    experience=serializers.IntegerField()
    course_id=serializers.IntegerField()

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.status = validated_data.get('status', instance.status)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.course_id = validated_data.get('course_id', instance.course_id)
        instance.save()
        return instance



class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=255)
    email= serializers.CharField(max_length=255)
    parentsphone= serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    course_id=serializers.IntegerField()
    teacher_id=serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.parentsphone = validated_data.get('parentsphone', instance.parentsphone)
        instance.address = validated_data.get('address', instance.address)
        instance.course_id = validated_data.get('course_id', instance.course_id)
        instance.teacher_id = validated_data.get('teacher_id', instance.teacher_id)
        instance.save()
        return instance



