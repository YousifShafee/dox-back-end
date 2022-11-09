# Dox Back-End

<p align='center'>
<img src="https://img.shields.io/badge/Django-239120?logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/Python-239120?logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Github-181717?logo=github&logoColor=white" />

<hr class="dotted">
It is an back-end side of Dox E-commerce system by Django. 

## API Reference

### Error Handling

  Application returns following errors:

  - 200 - Success
  
  - 201 - Created

  - 400 - Bad Request

  - 404 - Page Not Found

  - 405 - Method not allowed

  - 422 - Not processable

### End Points

Application has the following models.

  ### Cars model

    - GET
      - main/car/rent/
      - main/car/rent/email/<user_id>/
      - main/car/rent/<car_id>/
      - main/car/rent/search/
      - main/car/sales/
      - main/car/sales/email/<user_id>/
      - main/car/sales/<car_id>/
      - main/car/sales/search/
    - POST
      - main/car/rent/add/
      - main/car/sales/add/
    - PUT
      - main/car/rent/<car_id>/edit/
      - main/car/sales/<car_id>/edit/
    - DELETE
      - main/car/rent/<car_id>/delete/
      - main/car/sales/<car_id>/delete/

  ### Access model

    - GET
      - main/access/
      - main/access/email/<user_id>/
      - main/access/<access_id>/
      - main/access/search/
    - POST
      - main/access/add/
    - PUT
      - main/access/<access_id>/edit/
    - DELETE
      - main/access/<access_id>/delete/

  ### Electronic model

    - GET
      - main/electronic/
      - main/electronic/email/<user_id>/
      - main/electronic/<electronic_id>/
      - main/electronic/search/
    - POST
      - main/electronic/add/
    - PUT
      - main/electronic/<electronic_id>/edit/
    - DELETE
      - main/electronic/<electronic_id>/delete/

  ### Furniture model

    - GET
      - main/furniture/
      - main/furniture/email/<user_id>/
      - main/furniture/<furniture_id>/
      - main/furniture/search/
    - POST
      - main/furniture/add/
    - PUT
      - main/furniture/<furniture_id>/edit/
    - DELETE
      - main/furniture/<furniture_id>/delete/

  ### Medical model

    - GET
      - main/medical/
      - main/medical/email/<user_id>/
      - main/medical/<medical_id>/
      - main/medical/search/
    - POST
      - main/medical/add/
    - PUT
      - main/medical/<medical_id>/edit/
    - DELETE
      - main/medical/<medical_id>/delete/

  ### Mobile model

    - GET
      - main/mobile/
      - main/mobile/email/<user_id>/
      - main/mobile/<mobile_id>/
      - main/mobile/search/
    - POST
      - main/mobile/add/
    - PUT
      - main/mobile/<mobile_id>/edit/
    - DELETE
      - main/mobile/<mobile_id>/delete/

  ### Ad model

    - GET
      - main/ad/
      - main/ad/email/<user_id>/
      - main/ad/<ad_id>/
      - main/ad/search/
    - POST
      - main/ad/add/
    - PUT
      - main/ad/<ad_id>/edit/
    - DELETE
      - main/ad/<ad_id>/delete/

  ### Image model

    - GET
      - main/image/
      - main/image/search/
      - main/image/<category_name>/<active_status>/
    - POST
      - main/image/add/
    - PUT
      - main/image/<image_id>/active/
      - main/image/<image_id>/edit/
    - DELETE
      - main/image/<image_id>/delete/

  ### Properties model

    - GET
      - main/properties/
      - main/properties/email/<user_id>/
      - main/properties/<properties_id>/
      - main/properties/search/
    - POST
      - main/properties/add/
    - PUT
      - main/properties/<properties_id>/edit/
    - DELETE
      - main/properties/<properties_id>/delete/
  
  ### User model

    - GET
      - main/user/
      - main/user/<user_id>/
      - main/user/search/
      - main/user/logout/
    - POST
      - main/user/add/
      - main/user/login/
      - main/user/confirm_account/
      - main/user/send_code/
      - main/user/change_pass/
    - PUT
      - main/user/<user_id>/edit/
    - DELETE
      - main/user/<user_id>/delete/

## Some technical information:

- Django 3.0 
- Django REST Framework 3.13.1
- Django REST Framework jwt 1.11.0
- Django Import Export 2.8.0


## To Install:

Cloning the Repository:

```
$ git clone https://github.com/YousifShafee/dox-back-end

$ cd dox-back-end 

```

Installing dependencies:

```
$ pip install -r requirements.txt

```

Last commands to start:

```
$ python manage.py runserver

```

Build a new changes in database:

```
$ python manage.py makemigrations

$ python manage.py migrate

```
Create a super user:

```
$ python manage.py createsuperuser <admin_name>

```