# Menu REST API ![pre-commit workflow](https://github.com/Shadowmoses1314/API_RESTAURANT_MENU_2/actions/workflows/pre-commit.yml/badge.svg)

This is an asynchronous application for managing a restaurant menu. It includes three entities: Menu, Submenu, and Dish.

Dependencies:
+ Menus have submenus.
+ Submenus have dishes.

Caching is implemented using Redis as the caching storage.

#### How to Run the Application
```
docker compose -f "docker-compose.yml" up -d --build
```
#### How to Run the Tests
```
docker compose -f "docker-compose.tests.yml" up -d --build
```

#### Output test results to the console
```
docker logs test_app
```


The API documentation is available at ```http://127.0.0.1:8000/docs```

![Image alt](https://github.com/Shadowmoses1314/API_RESTAURANT_MENU_2/raw/main/image_from_readme/api.JPG)
