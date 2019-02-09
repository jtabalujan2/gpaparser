# gpaparser

======

This application is two different applicatiosn to help me learn selenium. I worked on it offline before realizing that my github repo for it was not set up.
--
The main portion of this simply executes either the chromedriver.exe or phantomjs driver (headless browser) and uses CSUN's administrative website to parse student data. My credentials were removed and elevated priviledges are required in order to access the link in the program.
--

Application will :
1. Navigate to CSUN portal and enter credentials
2. Navigate to admin portal to look up Student records
3. Input student records 
4. Navigate through 3-4 pages to get to page that includes student's GPA
  4a. Has error catching that will notify user to manually look up certain since their GPA's are unable to be scraped via the webpage.
5. Print out in console student name and GPA


### Code can be found in Gpaparser>SeleniumTest>gpaparser.py
