Feature: Iterate the collection and compile tag stats
    In order to understand the structure of the files, compile a list of tags

    Scenario: tags in test data directory
    Given I have the path /Users/oconnoat/Dropbox/Source/python/xmlBrowser/testData
    When I open it and count the tags in the files
    Then I see the number 4




