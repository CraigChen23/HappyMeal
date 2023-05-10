# STAYHAPPY by HappyMeal

## Roster and Roles:
 * Craig Chen (PM) : APIs and Flask
 * Erica Li: HTML/CSS
 * William Guo: JS data visualization
 * Nada Hameed: SQL Database 

---
## Description of website:
We plan to make a choropleth map of the world showcasing the exports of coffees from each country (or at least the ones on the database) throughout the different years. When users click onto the country, it will redirect them to another page that has a bar graph and pie chart of their coffee export throughout the years. 

Clients are able to filter results based on country and year. 
Time permitted, a search function to find nearby coffee shops based on location 

---
## API Cards:

https://restcountries.com/v3.1/all (open api)

- https://restcountries.com/v3.1/name/{name}


https://www.geoapify.com/static-maps-api (key accessed)
- ```
var requestOptions = {
  method: 'GET',
};

fetch("https://api.geoapify.com/v2/places?categories=commercial.supermarket&filter=rect%3A10.716463143326969%2C48.755151258420966%2C10.835314015356737%2C48.680903341613316&limit=20&apiKey=c1260a076fc84b9391b4ee3b50fa4ce9", requestOptions)
  .then(response => response.json())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

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

Description here 

Source: https://www.kaggle.com/datasets/yamaerenay/ico-coffee-dataset-worldwide
