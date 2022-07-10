from django.test import TestCase
from django.urls import reverse


class LoginBaseTest(TestCase):

    def setUp(self):   #set up is where we do our initializations for the test. Set up is called once before each test is run
        self.register_url=reverse('home')
        self.user = {
            'username' : 'username',
            'pass1' : 'password',
            #'password2': 'password2'
        }

        return super().setUp()

class RegisterBaseTest(TestCase):
    def setUp(self):
        self.register_url=reverse('signup')
        self.user = {
            'username' : 'LBJ1234',
            'pass1' : 'password',
            'pass2': 'password',
        }
        self.user_password_mismatch={
            'username' : 'LBJ1234',
            'pass1' : 'tes',
            'pass2' : 'tester'

        }
        self.user_username_too_long={
            'username' : 'ABCDEFGHIJKLMNOPQRSTUVWXYZLBJ1234',
            'pass1' : 'tester',
            'pass2' : 'tester'
        }

        self.user_not_alpha_numeric={
            'username' : '@$%#^%$&%ABCDEFGHIJKLMNOPQRSTUVWXYZLBJ1234',
            'pass1' : 'tester',
            'pass2' : 'tester'
        }
        self.user_fine={
            'username' : 'brucewayne',
            'pass1' : '12',
            'pass2' : '12'
        }
        self.user_password_too_short={
            'username' : 'brucewayne',
            'pass1' : '1',
            'pass2' : '1'
        }

        return super().setUp()

class LoginCreatedBaseTest(TestCase):

    def setUp(self):   #set up is where we do our initializations for the test. Set up is called once before each test is run
        self.register_url=reverse('accountcreated')
        self.user = {
            'username' : 'username',
            'pass1' : 'password',
            #'password2': 'password2'
        }
        return super().setUp()
    


#viewing html page will return page 200
#redirect page will return code 302
#password does not match



class LoginTest(LoginBaseTest):
    def test_can_view_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'authentication/login.html')
    
    def test_can_login_user(self):
        response=self.client.post(self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)


class RegisterTest(RegisterBaseTest):
        def test_can_view_page_correctly(self):
            response = self.client.get(self.register_url)
            self.assertEqual(response.status_code,200)
            self.assertTemplateUsed(response, 'authentication/registration.html')
        
        def test_register_passwords_do_not_match(self):
            response=self.client.post(self.register_url,self.user_password_mismatch, format='text/html')
            self.assertEqual(response.status_code, 200)
        
        def test_username_too_long(self):
            response=self.client.post(self.register_url,self.user_username_too_long, format='text/html')
            self.assertEqual(response.status_code, 200)
        
        def test_not_alpha_numeric(self):
            response=self.client.post(self.register_url,self.user_not_alpha_numeric, format='text/html')
            self.assertEqual(response.status_code, 200)
        
        def test_user_fine(self):
            response=self.client.post(self.register_url,self.user_fine, format='text/html')
            self.assertEqual(response.status_code, 302)
        
        def test_password_too_short(self):
            response=self.client.post(self.register_url,self.user_password_too_short, format='text/html')
            self.assertEqual(response.status_code, 200)



class LoginCreatedTest(LoginCreatedBaseTest):
    def test_can_view_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'authentication/successfullogin.html')




        

