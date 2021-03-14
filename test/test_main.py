#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

@pytest.mark.parametrize(
    'name',
    [
        ('ada'),
        ('blues')
    ]
)
def test_main(
    name
):
    assert True
