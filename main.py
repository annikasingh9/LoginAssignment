from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
Builder.load_file("LoginAssignment.kv")

users = {"Banana": "Bananas7!"}
class LoginAssignmentApp(App):
    def build(self):

        return LoginManager()



class LoginManager(ScreenManager):
    pass

class LoginPage(Screen):
    def check_credentials(self,username,password):
        if username.text in users and users[username.text] == password.text:
            self.manager.current = 'correct_screen'
        else:
            self.ids.test.text = "Invalid Credentials"
            self.ids.test.color = "red"
    def register(self):
        self.manager.current = "register_screen"


class CorrectLogin(Screen):
    def advance(self):
        self.manager.current = "login_page"

class RegisterScreen(Screen):
    def register(self, newusername, newpassword, re_newpassword):
        special = "~!@#$%^&*()_+-=."
        has_special = False
        numbers = "1234567890"
        has_lowercase = False
        has_capital = False
        has_numbers = False
        for i in newpassword.text:
            if i in special:
                has_special = True
            if i in numbers:
                has_numbers = True
            if i.capitalize() == i:
                has_capital = True
            if i.lower() == i:
                has_lowercase = True

        if (newusername.text not in users) and (
                newpassword.text == re_newpassword.text) and has_special and has_numbers and has_capital and has_lowercase and (
                len(newpassword.text) > 7):
            users[newusername.text] = newpassword.text
            self.manager.current = "login_page"
        else:
            self.ids.validity.color = (1, 0, 0, 1)

    def log(self):
        self.manager.current = "login_page"


users = {"Banana": "Ban"}

LoginAssignmentApp().run()

