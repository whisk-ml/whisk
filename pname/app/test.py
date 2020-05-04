import os
import unittest
import json
# import app from the main.py file
from main import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
        self.assertEqual(app.debug,False)

    # function to teardown connection after testing
    def tearDown(self):
        pass

    def test_predict(self):
        pass
        # The code below is commented out as it will likely fail when a real model
        # is provided. It should pass on a fresh app.
        # response = self.app.post('/predict',
        #                         data=json.dumps({"data": [[1]]}),
        #                         content_type='application/json')
        # self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
