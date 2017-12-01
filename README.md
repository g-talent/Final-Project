# Final-Project

A repository for the Fall 2017 IS452 final project.

Recently, I have been thinking about the database my work uses.  In the CAD department, to keep track of all the customer sites, 
we create ID's for each customer.  We use an abbreviation of the company/customer name, the dealer and the date the drawing was 
submitted to create the ID.  For a company, we take the first two letters of each word then space then show the abbreviation for 
the dealer then month and year.  An example would be Harvest Land Coop, KSi dealer, Nov. 2017, the ID would be halaco k1117.  
For a customer name, we use the first three letters of the last name followed by the firs three letters of the first name, then space, 
then dealer, then month and year.  An example of a customer name ID would be, Grace Talent, KSi dealer, Nov. 2017: talgra k1117.

While I can't use the names we have on file with my company, I thought maybe I could use the data from the Chicago Data Portal.  
They have a list of the current business licenses registered with the city.  I am thinking of using my company's way of creating ID's 
to create ID's for the businesses in Chicago.  Here is a link to the dataset 
https://data.cityofchicago.org/Community-Economic-Development/Business-Licenses-Current-Active/uupf-x98q.  
There are some 60,000 businesses registered with the city.  It is an active spreadsheet.  

Steps:
  - Read in csv file
  - Clean up the legal names of the business so that I can create the ID's
    - Make all lowercase and take out all the punctuation
    - Take out LLC, INC, LTD, AND, THE etc.
    - If there is only one word for the company/customer name then use the full name for ID
  - Detect any duplicate names
    - Use the street address or some other means if street address does not work to differentiate the duplicate names
  - Create ID
    - Company - use first two letters of each word in name then space then month/year when license was issued
    - Customer name - use first three letters of last name followed by first three letters of first name then space then 
    month/year when license was issued
  - Create a dictionary where the ID's are the keys and all other information stored as values of the key
  - Create for each renewal and list the businesses up for renewal

Goal:
  - Create ID's using the legal names of the business
    - If there are duplicate names, then use the street address to differentiate
    - If there are two licenses registered to the same company/customer with same street address, then find some other way to 
    differentiate the two.
  - Create a dictionary of the businesses using the ID's as the key
  - Create files for each renewal year and list the businesses that are up for renewal

Potential problems:
  - How to detect names?
  - Seems like those who use their name as their legal business name on paper and what their business is known by customers will 
  usually have their address redacted for privacy
  - How to extract street address without the numbers attached?
  - Should I web scrape or just read in the csv file?  Not sure how to go about web scraping an active spreadsheet.  
  I looked at the source page and couldn't really make to much sense of it when it got to the spreadsheet part.
