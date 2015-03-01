from django.test import TestCase


class ViewsTest(TestCase):
    """
    TestCase to test all exposed views for user.
    """

    def setUp(self):
        pass

    def testHome(self):
        response = self.client.get('/user/')
        self.assertEquals(response.status_code, 200)
