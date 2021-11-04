# Device Controller Web Interface

This is an Django Application for [Device Controller Library](https://github.com/dmdhrumilmistry/DeviceController) used to control board pins using a website.

## Screenshots
- Login Page

    ![Login Page](https://github.com/dmdhrumilmistry/DeviceControllerWebInterface/blob/main/.images/LoginPage.png?raw=True)
  
- Devices Control Page

    ![Control Page](https://github.com/dmdhrumilmistry/DeviceControllerWebInterface/blob/main/.images/ControlPage.png)

- Devices Admin Page

    ![Admin Page](https://github.com/dmdhrumilmistry/DeviceControllerWebInterface/blob/main/.images/DevicesAdminPage.png)


## Installation

- Install python 3.7 or above

- Clone repository
    ```
    git clone https://github.com/dmdhrumilmistry/DeviceControllerWebInterface.git/
    ```

- Change directory
    ```
    cd DeviceControllerWebInterface
    ```

- install requirements
    ```
    pip install -r requirements.txt
    ```
    > use `pip3` and `python3` on linux distros instead of `pip` and `python`.


- Migrate DB using
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
    

- Connect Arduino Board to Host machine

- Upload sketch on the board using Arduino IDE.

    > Use Device Controller Library to program Boards. View [example](https://github.com/dmdhrumilmistry/DeviceController/blob/main/examples/ArduinoUnoController/ArduinoUnoController.ino) 

- Update COM port and other configurations in the /controller/views.py according to the uploaded sketch file

- Create admin account
    ```
    python manage.py createsuperuser
    ```
    > Enter details

- Start Application using
    ```
    python manage.py runserver 0.0.0.0:8000
    ```

- Login to admin account and Create devices based on the sketch requirements

    > Various users can be created from admin page

- Visit Running website to control devices
    ```
    http://127.0.0.1:8000/      # for localhost
    http://[local_ip]:8000/     # for local network
    ```
    > Allow incoming and outgoing connections on port 8000 of firewall settings on the host machine to access the web app.

> The host machine can be exposed to the internet using ssh/port forwarding methods to access the website over the internet.
> Before exposing the website to internet, generate a new secret key for the django app

## Generate and update new random key before exposing machine to the internet
-  Generate and copy new key
    ```
    python3 generate_new_key.py
    ```
- update secret key in ArduinoController/settings.py on line 23
  ```python
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'your_new_key'
  ```
