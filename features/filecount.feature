Feature: Count Files in the Directory that are XML
    In order to get an idea of the directory of files, it should return a count of the files

    Scenario: test data directory
    Given I have the path /Users/oconnoat/Dropbox/Source/python/xmlBrowser/testData
    When I open it and count the files
    Then I see the number 3

    Given I have the path /Users/oconnoat/Dropbox/Source/python/xmlBrowser/testData
    When I open it and count the valid xml files
    Then I see the number 2

    
    Given I have the path /Users/oconnoat/Dropbox/Source/python/xmlBrowser/testData
    When I open it and get the list of namespaces from all the trees
    Then I see the text 'test'

    Scenario: iish directory
    Given I have the path /Users/oconnoat/Dropbox/Source/python/xmlBrowser/iish
    When I open it and count the files
    Then I see the number 3696
