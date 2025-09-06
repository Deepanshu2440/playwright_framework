class LoginPage:

    def __init__(self, page):
        self.page = page

    def login(self,credentials):
        self.page.goto('https://rahulshettyacademy.com/client/')
        self.page.get_by_placeholder('email@example.com').fill(credentials['username'])
        self.page.get_by_placeholder('enter your passsword').fill(credentials['password'])
        self.page.get_by_role('button').click()

        return self.page
