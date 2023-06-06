#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Integration Tests for `hicomp` package."""

import os

import unittest
from hicomp import hicompcmd

SKIP_REASON = 'HICOMP_INTEGRATION_TEST ' \
              'environment variable not set, cannot run integration ' \
              'tests'

@unittest.skipUnless(os.getenv('HICOMP_INTEGRATION_TEST') is not None, SKIP_REASON)
class TestIntegrationHicomp(unittest.TestCase):
    """Tests for `hicomp` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_something(self):
        """Tests parse arguments"""
        self.assertEqual(1, 1)
