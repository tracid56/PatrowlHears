# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CVE, CPE, CWE, VIA


class CVESerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CVE
        fields = [
            'cve_id', 'summary', 'assigner',
            'published', 'modified',
            'cvss', 'cvss_time', 'cvss_vector',
            'cwe', 'access', 'impact', 'vulnerable_products',
            'via_set',
            'created_at', 'updated_at'
        ]


class VIASerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VIA
        fields = [
            'cve', 'refmap', 'sources',
            'created_at', 'updated_at'
        ]


class CPESerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CPE
        fields = [
            'title', 'vector',
            'vendor', 'product', 'vulnerable_products'
        ]


class CWESerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CWE
        fields = ['cwe_id', 'name', 'description']
