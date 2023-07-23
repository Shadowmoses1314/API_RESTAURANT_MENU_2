# Menu REST API

This is an asynchronous application for managing a restaurant menu. It includes three entities: Menu, Submenu, and Dish.

Dependencies:
+ Menus have submenus.
+ Submenus have dishes.

Caching is implemented using Redis as the caching storage.

#### How to Run the Application
```
docker-compose up -d
```

The API documentation is available at ```http://127.0.0.1:8000/docs```