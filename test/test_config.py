import os
import unittest

from flask import current_app
from flask_testing import TestCase
from main.config import basedir
from manage import app

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('main.config.DevelopmentConfig')
        return app 

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'Azu')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)


if __name__ == '__main__':
    unittest.main()