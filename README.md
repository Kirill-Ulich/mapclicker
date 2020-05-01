## MAPCLICKER
---
Simple django-project with a geographic map

### About Mapclicker
---
There is a map on the start page, when clicked on it, the coordinates (latitude and longitude) are saved in the database. When you click on the link located under the map, you are redirected to a page with listing all the coordinates from the database.

### Installation
---
 - Clone or download the project
 - Create virtual environment at the root of the project using the command
    ```sh
    virtualenv venv
    ```
    If *virtualenv* is not installed, use the following command
    ```sh
    pip3 install virtualenv
    ```
 - Activate *venv*
    ```sh
    source venv/bin/activate
    ```
  - Install requirements
    ```sh
    pip install -r requirements.txt
    ```
 - Create a database using PostgreSQL and change DB data in *settings.py*
 - Apply migrations
    ```sh
    python manage.py migrate
    ```
It's all. Now you can start the project with the following command
```sh
python manage.py runserver
```
