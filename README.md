# Dox Back-End

<p align='center'>
<img src="https://img.shields.io/badge/Django-239120?logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/Python-239120?logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Github-181717?logo=github&logoColor=white" />

Dox is an E-commerce project integrated with a chatbot app and Dox-Back-End is a server-side of it and is based on Django. A Dox-Back-End project that handel business and database actions on the site, which pass product data on API points to view it on the client-side project, and receive requests to create users, products ads and so on.

There are seven types of products dox project deal with it to create ads for it:
- Cars
- Apartness (housing units)
- Electronic devices (house devices)
- Furniture
- Medical devices
- Mobiles
- Accessories jewelry

and there are four types of users:
- admin user
- update vice admin user
- delete vice admin user
- normal user

### Admin user
admin user has the roles:
- create two types of vice users (update & delete) types and delete them
- update and delete normal ads 
- update and delete paid ads 
- change a site logo
- Add new and update products images
- Add new and update premium company-images

### Update vice admin user
update vice admin user has the roles:
- update and delete normal ads 
- update and delete paid ads 
- change a site logo
- update products images
- update premium company-images

### Delete vice admin user
delete vice admin user has the roles:
- delete normal ads 
- delete paid ads 
- change a site logo
- update products images
- update premium company-images

### Normal user
noraml user has the roles:
- create normal ad
- create paid ad

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
      - car/rent/
      - car/rent/email/<user_id>/
      - car/rent/<car_id>/
      - car/rent/search/
      - car/sales/
      - car/sales/email/<user_id>/
      - car/sales/<car_id>/
      - car/sales/search/
    - POST
      - car/rent/add/
      - car/sales/add/
    - PUT
      - car/rent/<car_id>/edit/
      - car/sales/<car_id>/edit/
    - DELETE
      - car/rent/<car_id>/delete/
      - car/sales/<car_id>/delete/

  ### Access model

    - GET
      - access/
      - access/email/<user_id>/
      - access/<access_id>/
      - access/search/
    - POST
      - access/add/
    - PUT
      - access/<access_id>/edit/
    - DELETE
      - access/<access_id>/delete/

  ### Electronic model

    - GET
      - electronic/
      - electronic/email/<user_id>/
      - electronic/<electronic_id>/
      - electronic/search/
    - POST
      - electronic/add/
    - PUT
      - electronic/<electronic_id>/edit/
    - DELETE
      - electronic/<electronic_id>/delete/

  ### Furniture model

    - GET
      - furniture/
      - furniture/email/<user_id>/
      - furniture/<furniture_id>/
      - furniture/search/
    - POST
      - furniture/add/
    - PUT
      - furniture/<furniture_id>/edit/
    - DELETE
      - furniture/<furniture_id>/delete/

  ### Medical model

    - GET
      - medical/
      - medical/email/<user_id>/
      - medical/<medical_id>/
      - medical/search/
    - POST
      - medical/add/
    - PUT
      - medical/<medical_id>/edit/
    - DELETE
      - medical/<medical_id>/delete/

  ### Mobile model

    - GET
      - mobile/
      - mobile/email/<user_id>/
      - mobile/<mobile_id>/
      - mobile/search/
    - POST
      - mobile/add/
    - PUT
      - mobile/<mobile_id>/edit/
    - DELETE
      - mobile/<mobile_id>/delete/

  ### Ad model

    - GET
      - ad/
      - ad/email/<user_id>/
      - ad/<ad_id>/
      - ad/search/
    - POST
      - ad/add/
    - PUT
      - ad/<ad_id>/edit/
    - DELETE
      - ad/<ad_id>/delete/

  ### Image model

    - GET
      - image/
      - image/search/
      - image/<category_name>/<active_status>/
    - POST
      - image/add/
    - PUT
      - image/<image_id>/active/
      - image/<image_id>/edit/
    - DELETE
      - image/<image_id>/delete/

  ### Properties model

    - GET
      - properties/
      - properties/email/<user_id>/
      - properties/<properties_id>/
      - properties/search/
    - POST
      - properties/add/
    - PUT
      - properties/<properties_id>/edit/
    - DELETE
      - properties/<properties_id>/delete/
  
  ### User model

    - GET
      - user/
      - user/<user_id>/
      - user/search/
      - user/logout/
    - POST
      - user/add/
      - user/login/
      - user/confirm_account/
      - user/send_code/
      - user/change_pass/
    - PUT
      - user/<user_id>/edit/
    - DELETE
      - user/<user_id>/delete/

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