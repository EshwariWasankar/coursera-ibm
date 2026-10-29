import unittest

from app import app


class ServiceTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_root_reports_service_and_port(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {
            "message": "SERVICERUNNING",
            "port": 8000,
        })

    def test_health_endpoint(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})


if __name__ == "__main__":
    unittest.main()
