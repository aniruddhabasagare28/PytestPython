Feature: Open Transaction
  Tests related to Order Transactions

  Scenario Outline: Verify order success message shown in details page

    Given Place the item order with <username> and <password>
    And User is on landing page

    When I login to portal with <username> and <password>
    And Navigate to order page
    And Select the order

    Then Verify order message is successfully displayed
    Examples:
      | username                    | password    |
      |aniruddhabasagare28@gmail.com| Admin123!@# |
      |ani2805@gmail.com            | Admin123!@# |
