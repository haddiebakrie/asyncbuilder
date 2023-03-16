import pytest


def test_flower():
    from kivy_garden.asyncbuilder import FlowerLabel
    label = FlowerLabel()
    assert label.text == 'Demo flower'
