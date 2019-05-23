# Week1

Description of task: Data Scraping 

1. Get all releases of economic data from the FRED API

https://research.stlouisfed.org/docs/api/fred/

https://research.stlouisfed.org/docs/api/fred/releases.html

2. Use the API key provided below, 

27cbff1814752ba2aa046855f6d4a162

3. Save the JSON response in local server 

4. Parse it into a relational datatable 

5. Write the response into a MySQL database 

   https://www.mysql.com/products/workbench/

    MySQL workbench is free 


Instruction on how to run the code:

- Code for all tasks are included within the week1 finder

- dataScraping.py contains the code for retrieving data from the FRED API and parse data to a relational datatable
	packages: requests, json
	run: python3 dataScraping.py

- release_data.json contains the origin data retrieved from the API in json format

- released_data.csv contains the data(table) to be loaded to the mysql database

- relationaldb.xml contains the xml file for MySQL database.
