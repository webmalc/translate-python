#!/usr/bin/env python
# encoding: utf-8

from .deepl import DeeplProvider  # noqa
from .dummy import DummyProvider  # noqa
from .microsoft import MicrosoftProvider  # noqa
from .mymemory_translated import MyMemoryProvider  # noqa

__all__ = [
    "MyMemoryProvider",
    "MicrosoftProvider",
    "DeeplProvider",
    "DummyProvider",
]
