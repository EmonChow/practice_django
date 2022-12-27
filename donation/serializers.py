from django.conf import settings
from authentication.serializers import AdminUserMinimalListSerializer

from rest_framework import serializers

from django_currentuser.middleware import get_current_authenticated_user

from rest_framework_recursive.fields import RecursiveField

from donation.models import *


class CauseListSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField(read_only=True)
    updated_by = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cause
        fields = '__all__'
        extra_kwargs = {
            'created_at': {
                'read_only': True,
            },
            'updated_at': {
                'read_only': True,
            },
            'created_by': {
                'read_only': True,
            },
            'updated_by': {
                'read_only': True,
            },
        }

    def get_created_by(self, obj):
        return obj.created_by.email if obj.created_by else obj.created_by

    def get_updated_by(self, obj):
        return obj.updated_by.email if obj.updated_by else obj.updated_by


class CauseMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cause
        fields = ['id', 'name']


class CauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cause
        fields = '__all__'

    def create(self, validated_data):
        modelObject = super().create(validated_data=validated_data)
        user = get_current_authenticated_user()
        if user is not None:
            modelObject.created_by = user
        modelObject.save()
        return modelObject

    def update(self, instance, validated_data):
        modelObject = super().update(instance=instance, validated_data=validated_data)
        user = get_current_authenticated_user()
        if user is not None:
            modelObject.updated_by = user
        modelObject.save()
        return modelObject


class CauseContentListSerializer(serializers.ModelSerializer):
    cause = CauseMinimalSerializer()
    created_by = serializers.SerializerMethodField(read_only=True)
    updated_by = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CauseContent
        fields = '__all__'
        extra_kwargs = {
            'created_at': {
                'read_only': True,
            },
            'updated_at': {
                'read_only': True,
            },
            'created_by': {
                'read_only': True,
            },
            'updated_by': {
                'read_only': True,
            },
        }

    def get_created_by(self, obj):
        return obj.created_by.email if obj.created_by else obj.created_by

    def get_updated_by(self, obj):
        return obj.updated_by.email if obj.updated_by else obj.updated_by


class CauseContentMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CauseContent
        fields = ('id', 'cause', 'name', 'value')


class CauseContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CauseContent
        fields = '__all__'

    def create(self, validated_data):
        modelObject = super().create(validated_data=validated_data)
        user = get_current_authenticated_user()
        if user is not None:
            modelObject.created_by = user
        modelObject.save()
        return modelObject

    def update(self, instance, validated_data):
        modelObject = super().update(instance=instance, validated_data=validated_data)
        user = get_current_authenticated_user()
        if user is not None:
            modelObject.updated_by = user
        modelObject.save()
        return modelObject


class CauseContentImageListSerializer(serializers.ModelSerializer):
    cause = CauseMinimalSerializer()
    created_by = serializers.SerializerMethodField(read_only=True)
    updated_by = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CauseContentImage
        fields = '__all__'
        extra_kwargs = {
            'created_at': {
                'read_only': True,
            },
            'updated_at': {
                'read_only': True,
            },
            'created_by': {
                'read_only': True,
            },
            'updated_by': {
                'read_only': True,
            },
        }

    def get_created_by(self, obj):
        return obj.created_by.email if obj.created_by else obj.created_by

    def get_updated_by(self, obj):
        return obj.updated_by.email if obj.updated_by else obj.updated_by


class CauseContentImageMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CauseContent
        fields = ('id', 'cause', 'head', 'image')


class CauseContentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CauseContentImage
        fields = '__all__'

    def create(self, validated_data):
        modelObject = super().create(validated_data=validated_data)
        user = get_current_authenticated_user()
        if user is not None:
            modelObject.created_by = user
        modelObject.save()
        return modelObject

    def update(self, instance, validated_data):
        modelObject = super().update(instance=instance, validated_data=validated_data)
        user = get_current_authenticated_user()
        if user is not None:
            modelObject.updated_by = user
        modelObject.save()
        return modelObject


class PaymentMethodListSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField(read_only=True)
    updated_by = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PaymentMethod
        fields = '__all__'
        extra_kwargs = {
            'created_at': {
                'read_only': True,
            },
            'updated_at': {
                'read_only': True,
            },
            'created_by': {
                'read_only': True,
            },
            'updated_by': {
                'read_only': True,
            },
        }

    def get_created_by(self, obj):
        return obj.created_by.email if obj.created_by else obj.created_by

    def get_updated_by(self, obj):
        return obj.updated_by.email if obj.updated_by else obj.updated_by


class PaymentMethodMinimalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['id', 'name']
        extra_kwargs = {
            'created_at': {
                'read_only': True,
            },
            'updated_at': {
                'read_only': True,
            },
            'created_by': {
                'read_only': True,
            },
            'updated_by': {
                'read_only': True,
            },
        }


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'
        extra_kwargs = {
            'created_at': {
                'read_only': True,
            },
            'updated_at': {
                'read_only': True,
            },
            'created_by': {
                'read_only': True,
            },
            'updated_by': {
                'read_only': True,
            },
        }

    def create(self, validated_data):
        modelObject = super().create(validated_data=validated_data)
        user = get_current_authenticated_user()
        if user is not None:
            modelObject.created_by = user
        modelObject.save()
        return modelObject

    def update(self, instance, validated_data):
        modelObject = super().update(instance=instance, validated_data=validated_data)
        user = get_current_authenticated_user()
        if user is not None:
            modelObject.updated_by = user
        modelObject.save()
        return modelObject


class PaymentMethodDetailListSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField(read_only=True)
    updated_by = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PaymentMethodDetail
        fields = '__all__'
        extra_kwargs = {
            'created_at': {
                'read_only': True,
            },
            'updated_at': {
                'read_only': True,
            },
            'created_by': {
                'read_only': True,
            },
            'updated_by': {
                'read_only': True,
            },
        }

    def get_created_by(self, obj):
        return obj.created_by.email if obj.created_by else obj.created_by

    def get_updated_by(self, obj):
        return obj.updated_by.email if obj.updated_by else obj.updated_by


class PaymentMethodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethodDetail
        fields = '__all__'
        extra_kwargs = {
            'created_at': {
                'read_only': True,
            },
            'updated_at': {
                'read_only': True,
            },
            'created_by': {
                'read_only': True,
            },
            'updated_by': {
                'read_only': True,
            },
        }

    def create(self, validated_data):
        modelObject = super().create(validated_data=validated_data)
        user = get_current_authenticated_user()
        if user is not None:
            modelObject.created_by = user
        modelObject.save()
        return modelObject

    def update(self, instance, validated_data):
        modelObject = super().update(instance=instance, validated_data=validated_data)
        user = get_current_authenticated_user()
        if user is not None:
            modelObject.updated_by = user
        modelObject.save()
        return modelObject


class DonationListSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField(read_only=True)
    updated_by = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Donation
        fields = '__all__'
        extra_kwargs = {
            'created_at': {
                'read_only': True,
            },
            'updated_at': {
                'read_only': True,
            },
            'created_by': {
                'read_only': True,
            },
            'updated_by': {
                'read_only': True,
            },
        }

    def get_created_by(self, obj):
        return obj.created_by.email if obj.created_by else obj.created_by

    def get_updated_by(self, obj):
        return obj.updated_by.email if obj.updated_by else obj.updated_by


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'
        extra_kwargs = {
            'created_at': {
                'read_only': True,
            },
            'updated_at': {
                'read_only': True,
            },
            'created_by': {
                'read_only': True,
            },
            'updated_by': {
                'read_only': True,
            },
        }

    def create(self, validated_data):
        modelObject = super().create(validated_data=validated_data)
        user = get_current_authenticated_user()
        if user is not None:
            modelObject.created_by = user
        modelObject.save()
        return modelObject

    def update(self, instance, validated_data):
        modelObject = super().update(instance=instance, validated_data=validated_data)
        user = get_current_authenticated_user()
        if user is not None:
            modelObject.updated_by = user
        modelObject.save()
        return modelObject


class MonthlySubscriptionListSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField(read_only=True)
    updated_by = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MonthlySubscription
        fields = '__all__'
        extra_kwargs = {
            'created_at': {
                'read_only': True,
            },
            'updated_at': {
                'read_only': True,
            },
            'created_by': {
                'read_only': True,
            },
            'updated_by': {
                'read_only': True,
            },
        }

    def get_created_by(self, obj):
        return obj.created_by.email if obj.created_by else obj.created_by

    def get_updated_by(self, obj):
        return obj.updated_by.email if obj.updated_by else obj.updated_by


class MonthlySubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlySubscription
        fields = '__all__'
        extra_kwargs = {
            'created_at': {
                'read_only': True,
            },
            'updated_at': {
                'read_only': True,
            },
            'created_by': {
                'read_only': True,
            },
            'updated_by': {
                'read_only': True,
            },
        }

    def create(self, validated_data):
        modelObject = super().create(validated_data=validated_data)
        user = get_current_authenticated_user()
        if user is not None:
            modelObject.created_by = user
        modelObject.save()
        return modelObject

    def update(self, instance, validated_data):
        modelObject = super().update(instance=instance, validated_data=validated_data)
        user = get_current_authenticated_user()
        if user is not None:
            modelObject.updated_by = user
        modelObject.save()
        return modelObject
