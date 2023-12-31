from unittest import mock

import django
from django.apps import apps
from django.conf import settings
from django.test import TestCase, override_settings

from aws_xray_sdk import global_sdk_config
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core.sampling.sampler import LocalSampler


class XRayConfigurationTestCase(TestCase):
    def test_sampler_can_be_configured(self):
        assert isinstance(settings.XRAY_RECORDER['SAMPLER'], LocalSampler)
        assert isinstance(xray_recorder.sampler, LocalSampler)
