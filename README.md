# Tech interview
This project is going to use no frameworks. This means server will work on top of a TCP server from socketserver built in library and there is no great framework behind these microservices.

In this repo you can find the code for the two microservices, they're in the same repo for distribution purposes but I'm treating them as separate projects, that's why they have their own compose file.

## Technologies 

### Database
Database connection will be made using MySQL official connector library.
I want to create a model object to handle queries from database, like most ORMs (e.g. Django Queryset) do.

### Server
Server will work with socketserver library and all requests will be handled using SimpleHttpRequest from http python library.

**Update 1:**
The code is OK, but I don't think is the right solution. I'll try to update the server to use wsgi, for this I really want to use something as uvicorn or gunicorn as toolkit, but I think is kind of debatible if they are frameworks or not, so I'll try a bare wsgi implementation.

The issue is that I don't have enough time to finish this, so I'll focus on the logic and fix the server later.

### Routing
I'll manage routing using a for loop on all urls.

### Testing
I'll try to use pytest to test the server endpoints.

### Dependencies
Poetry will handle dependencies.

## Framework
I'll follow a directory structure like the one Django uses. Obviously will be different and more messy, but directories and files like `models`, `views` and `urls.py` are intended to follow the Django pattern.

## Disclaimers
- I've never done a framework-less API on python and I didn't found a useful tutorial or example on the internet, so I don't expect to have a great code over here.
