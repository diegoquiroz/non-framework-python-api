# Tech interview
This project is going to use no frameworks. This means server will work on top of a TCP server from socketserver built in library and there is no great framework behind these microservices.

## Technologies 

### Database
Database connection will be made using MySQL official connector library.
I want to create a model object to handle queries from database, like most ORMs (like Django Queryset) do.

### Server
Server will work with socketserver library and all requests will be handled using SimpleHttpRequest from http python library.

### Routing
I'll manage routing using a for loop on all urls.

### Testing
I'll try to use pytest to test the server endpoints.

---
## Framework
I'll follow a directory structure like the one Django uses. Obviously will be different and more messy, but folders like `models`, `views` and `utils` are intended to follow Django pattern.

## Disclaimers
I've never done a framework-less API on python and I didn't found a useful tutorial or example on the internet, so I don't expect to have a great code over here.
