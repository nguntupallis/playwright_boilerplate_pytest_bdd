Feature: Login Feature

  Scenario: Login button is visible
    Given I access the internet web app
    Then the login button should be visible

 Scenario: NHS sign in page should be visible
    Given I access the internet web app
    When I click on the log in button
    Then your username is invalid alert should be visible

@login 
 Scenario: Sign in should <status> based on credentials provided
   Given I access the internet web app
   When I provide the <username> and <password>
   And the login button is clicked
   Then login should succeed - <status>    

Examples:
|username               | password        | status  |    
|tomsmith_valid         | pass            | pass    | 
|None                   | password        | fail    |
# |tomsmith             | password        | fail    |
# |tomsmith             | None            | fail    |
|invalid_username       | password        | fail    |  
# |tomsmith             | short           | fail    |  
|long_username          | password        | fail    |  
# |tomsmith           | long_password_that_exceeds_max_length           | fail  |  