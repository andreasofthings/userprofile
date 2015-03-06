from django.test import TestCase


class ViewsTest(TestCase):
    """
    TestCase to test all exposed views for anonymous users.
    """

    def setUp(self):
        pass

    def testHome(self):
        response = self.client.get('/user/')
        self.assertEquals(response.status_code, 200)

    def testLogin(self):
        response = self.client.get('/user/login/')
        self.assertEquals(response.status_code, 200)

    def testLogout(self):
        response = self.client.get('/user/logout/')
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/user/')
