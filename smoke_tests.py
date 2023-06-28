import unittest
import requests
import time

class SmokeTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://localhost:8000'

        for i in range(0, 100):
            try:
                res = requests.get(self.url + '/.well-known/ready')
                if res.status_code == 204:
                    return
                else:
                    raise Exception(
                            "status code is {}".format(res.status_code))
            except Exception as e:
                print("Attempt {}: {}".format(i, e))
                time.sleep(1)

        raise Exception("did not start up")

    def testWellKnownReady(self):
        res = requests.get(self.url + '/.well-known/ready')

        self.assertEqual(res.status_code, 204)

    def testWellKnownLive(self):
        res = requests.get(self.url + '/.well-known/live')

        self.assertEqual(res.status_code, 204)

    def testMeta(self):
        res = requests.get(self.url + '/meta')

        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.json(), dict)

    def testRerank(self):
        url = 'http://localhost:8000/rerank'
        propertyText = """
        The ref2Vec-centroid module is used to calculate object vectors based on the centroid of referenced vectors.
        The idea is that this centroid vector would be calculated from the vectors of an object's references, enabling
        associations between clusters of objects. This is useful in applications such as making suggestions
        based on the aggregation of a user's actions or preferences.
        """

        req_body = {'query': 'What is ref2vec?', 'property': propertyText}
        res = requests.post(url, json=req_body)
        resBody = res.json()

        self.assertEqual(200, res.status_code)
        self.assertEqual(resBody['query'], req_body['query'])
        self.assertEqual(resBody['property'], req_body['property'])
        self.assertTrue(resBody['score'] != 0)
        print(f"score: {resBody['score']}")


if __name__ == "__main__":
    unittest.main()
