from django import forms

from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from dcim.models import Device
from virtualization.models import VirtualMachine

from utilities.forms import (
    BootstrapMixin,
    DatePicker,
    CommentField,
    DynamicModelMultipleChoiceField,
    SlugField,
    DynamicModelChoiceField,
)

from . import models, choices

# ThreatSource Forms


class ThreatSourceForm(NetBoxModelForm):
    class Meta:
        model = models.ThreatSource
        fields = [
            "name",
            "threat_type",
            "capability",
            "intent",
            "targeting",
            "description",
            "notes",
        ]


class ThreatSourceFilterForm(NetBoxModelFilterSetForm):
    model = models.ThreatSource

    class Meta:
        fields = ["name", "threat_type", "capability", "intent", "targeting"]


# ThreatEvent Forms


class ThreatEventForm(NetBoxModelForm):

    vulnerability = DynamicModelMultipleChoiceField(
        queryset=models.VulnerabilityAssignment.objects.all(),
        required=True,
    )

    class Meta:
        model = models.ThreatEvent
        fields = [
            "name",
            "threat_source",
            "description",
            "notes",
            "relevance",
            "likelihood",
            "impact",
            "vulnerability",
        ]


class ThreatEventFilterForm(NetBoxModelFilterSetForm):
    model = models.ThreatEvent



    class Meta:
        fields = [
            "name",
            "threat_source",
            "relevance",
            "likelihood",
            "impact",
            "vulnerability",
        ]


# Vulnerability Forms


class VulnerabilityForm(NetBoxModelForm):
    class Meta:
        model = models.Vulnerability
        fields = ["name", "cve", "description", "notes"]


class VulnerabilityFilterForm(NetBoxModelFilterSetForm):
    model = models.Vulnerability

    class Meta:
        fields = ["name", "cve"]


# VulnerabilityAssignment Forms


class VulnerabilityAssignmentForm(BootstrapMixin, forms.ModelForm):

    vulnerability = DynamicModelChoiceField(
        queryset=models.Vulnerability.objects.all(),
        required=True,
    )

    class Meta:
        model = models.VulnerabilityAssignment
        fields = ["asset_object_type", "asset_id", "vulnerability"]
        widgets = {
            'asset_object_type': forms.HiddenInput(),
            'asset_id': forms.HiddenInput(),
        }


class VulnerabilityAssignmentFilterForm(NetBoxModelFilterSetForm):
    model = models.VulnerabilityAssignment

    class Meta:
        fields = ["vulnerability"]
