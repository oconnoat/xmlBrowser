Feature: run xpath on a particular file
    Scenario: run the xpath query
    Given I have the path '/Users/oconnoat/Dropbox/Source/python/xmlBrowser/testData' and the url '/Users/oconnoat/Dropbox/Source/python/xmlBrowser/testData/test1.xml'
    When I run the xpath query '/node[@value="1"]'
    Then I see the text <node value="1" id="1">One</node> 

