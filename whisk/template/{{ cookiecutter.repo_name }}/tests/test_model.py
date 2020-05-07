#!/usr/bin/env python
import pytest
from {{cookiecutter.project_name}}.models.model import Model

def test_predict():
    model = Model()
    model.predict([[1,2],[3,4]])
