from playwright.sync_api import Playwright, sync_playwright

login = {"userEmail": "deep1@gmail.com", "userPassword": "Deep@1234"}
order = {"orders": [
        {"country": "India",
         "productOrderedId": "68a961459320a140fe1ca57a"}]}

class ApiUtils:


    def apiLogin(self, playwright:Playwright, credentials):
        api_request_context = playwright.request.new_context(base_url='https://rahulshettyacademy.com/')
        response = api_request_context.post(url='api/ecom/auth/login', data={"userEmail": credentials['username'],
                                                                             "userPassword": credentials['password']})

        # /check for if response valid
        assert response.ok

        response_json = response.json()
        token = response_json['token']
        print('token : ',token)
        return token

    def apiCreateOrder(self, playwright: Playwright, credentials):

        authorization = self.apiLogin(playwright, credentials)
        api_request_context = playwright.request.new_context(base_url='https://rahulshettyacademy.com/')
        response = api_request_context.post(url='api/ecom/order/create-order', data=order,
                                            headers={"Authorization" : authorization})
        response_json = response.json()
        order_id = response_json['orders'][0]
        print('OrderID :',order_id)
        return order_id





