Feature: Blog Article
    A blog where you can publish your articles.

    Scenario: Publishing an article with a title and a text
        Given I'm a connected user
        And I check the index page

        When I enter a title for my article
        And I enter a text for my article
        And I press the share button

        Then I should not see the error message
        And the article should be published

    Scenario: Publishing an article with no title and no text
        Given I'm a connected user
        And I check the index page

        When I press the share button

        Then I should see an error message