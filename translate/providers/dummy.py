#!/usr/bin/env python
# encoding: utf-8
from .base import BaseProvider


class DummyProvider(BaseProvider):
    """
    @DummyProvider: This is a dummy provider
    """

    name = "Dummy"

    def get_translation(self, text):
        return ""
