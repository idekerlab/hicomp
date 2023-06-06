#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `hicomp` package."""
import os
import tempfile
import shutil

import unittest
from hicomp.runner import HicompRunner


class TestHicomprunner(unittest.TestCase):
    """Tests for `hicomp` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_constructor(self):
        """Tests constructor"""
        myobj = HicompRunner(outdir='foo', exitcode=0)

        self.assertIsNotNone(myobj)

    def test_run(self):
        """ Tests run()"""
        temp_dir = tempfile.mkdtemp()
        try:
            myobj = HicompRunner(outdir=os.path.join(temp_dir, 'foo'),
                                                         exitcode=4)
            self.assertEqual(4, myobj.run())
        finally:
            shutil.rmtree(temp_dir)
