# Flask Python Tutorial

Today we'll make a Flask-driven website that gives users a tutorial on basic Python concepts. We'll be doing this to practice concepts we've learned in class, such as 

* Rendering templates, redirecting, and other routing
* Passing variables to templates
* Making `GET` and `POST` routes
* Parsing form data

## Deliverables

For this assignment you will be creating ONE Flask app. Each problem listed below will direct you to create a route or feature within that app.

*Reminder: On your laptop, you can run your server from your command line with the following command:*

```
flask run
```

## Requirements:

### Routes

By the end of this, you should have ONE Flask app that implements the following routes:

| METHOD | PATH | FUNCTIONALITY |
| ------ | ------------- | ---------------------------------------------------------- |
| GET | `/` | Render a home page that includes the Python logo somewhere on the page |
| GET | `/loops` | Make a page describing for loops, while loops, and ranges in Python |
| GET | `/operators` | Make a page detailing at least 3 different operators |
| POST | `/operators` | Enable user to enter new operators |


### Database

Your `operators` documents in Mongo should look something like this: 

```json
{
  "name": "Floor Division",
  "description": "Division that rounds down to the nearest integer. Also known as integer division.",
  "symbol": "//",
  "example": "3 // 2 == 1",
  "uses": "A common situation we might see this operator is when we need to calcuate a 
  list index, which will need to be a whole number. For example, perhaps we are trying to 
  find the middle index of a list, but there are an even number of elements. In this case, 
  we could use floor division to select the leftmost element in the list by default."
}
```

### Additional Requirements

* Your site should have a `static` folder that includes a style.css with styling for your site. 
* Your site should have a nav bar/header and footer that is present on every page.
  * Navbar should include links to "Home", "Operators", and "Loops" pages


------------

## Getting Started

### Home Page

This page 

