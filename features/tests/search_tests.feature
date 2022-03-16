Feature: Test for Wiki Search
    Background:
        Given Tap on search screen

    Scenario: User searches and corrects the result
        When Enter Python into a search field
        Then Top result Python is shown

    Scenario: Found 'No results'
        When Enter awwcevrb into a search field
        Then 'No results' is shown
