# STAYHAPPY by HappyMeal

## Roster and Roles:
 * Craig Chen (PM) : APIs and Flask
 * Erica Li: HTML/CSS
 * William Guo: JS data visualization
 * Nada Hameed: SQL Database 

---
## Abstract/Summary of App:
We plan to make a choropleth map of the world showcasing the exports of coffees from each country (or at least the ones on the database) throughout the different years. When users hovers the country, it will display the amount of coffee exported in that year. Clients are able to search for different countries which will redirect them another page that has a line chart with all the exports across the years as well a some fun facts. 

Time permitted, a search function to find nearby coffee shops based on location and integration of the other csv datas.

---
## API Cards:

Rest Countries API:
https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_RestCountries.md

Geoapify API:
https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_Geoapify.md 

---

## Launch codes:
1) open terminal and clone repo (with html or ssh)  
```$ git clone git@github.com:CraigChen23/HappyMeal.git```  
or  
```$ git clone https://github.com/CraigChen23/HappyMeal.git```  
2) install everything from requirements  
```$ pip install -r requirements.txt```  
3) run ```__init__.py``` by running ```python __init__.py```, open the url in the command prompt (127.0.0.1:5000) in a browser   
```$ python app/__init__.py```  
4) Have fun! 

---
## Data:

Description: CSV containing information on of coffee exports from the year 1990 - 2018. The information includes country name, each individual year and the amount of coffee exported in thousands of 60kg bags. There are also other csv files with data on coffee consumption, coffee imports, prices, inventories etc. 

Source: https://www.kaggle.com/datasets/yamaerenay/ico-coffee-dataset-worldwide
