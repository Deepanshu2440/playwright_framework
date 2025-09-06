Feature: Order Transaction
  Tests related to order transactions

  Scenario Outline: Verify order success message shown in details page
    Given place the order with <username> and <password>
    And the user is on landing page
    When I login with <username> and <password>
    And navigate to order page
    And select orderId
    Then order message is successfully displayed
    Examples:
      | username         | password    |
      | deep1@gmail.com  | Deep@1234   |

