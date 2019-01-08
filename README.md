# SmartPark-Server

SmartPark-Server contains a website and has a REST-API.
This solution is supposed to run on a Raspberry Pi, but will work with linux, windows computers aswell.
It is possible to run the application alone as seen in the Examples, but you will have to download the client application for full functionality.
With doing so you will be able to add your own parkinglot and mark the parkingspots accordingly.


Go to [SmartPark-Client](https://github.com/magnusoy/SmartPark-Client) for more imformation setting it up.


### Prerequisites

You will need [Python 3](https://www.python.org/) for using the provided files.
Furthermore you will need to install all the dependencies listed below.

Install Python 3
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-dev libffi-dev libssl-dev -y
```

### Installing

Clone or download repository to your home directory.

```bash
cd ~
git clone https://github.com/magnusoy/SmartPark-Server.git
```

Install dependencies
```bash
cd ~/SmartPark-Server
pip3 install -r requirements.txt

or

pip3 install Flask==1.0.2
pip3 install Flask-Mail==0.9.1
pip3 install flask-marshmallow==0.9.0
pip3 install Flask-WTF==0.14.2
pip3 install Flask-SQLAlchemy==2.3.2
pip3 install marshmallow==2.16.3
pip3 install marshmallow-sqlalchemy==0.15.0
pip3 install PyJWT
```

You will have to change some settings if you want a working contact page.
```bash
cd SmartPark-Server/instance
sudo nano config.py
```
Then change MAIL_USERNAME and MAIL_PASSWORD to yours.
Press CTRL+O and then ENTER to save changes.
Press CTRL+X to exit.


### Examples

To run development server :
```bash
cd ~/SmartPark-Server
flask run
```
Press Ctrl+C in the terminal to close the server.

The development server will now run on: http://localhost:5000/

You will now also be able to use the REST-API
```bash
curl -GET http://localhost:5000/parkinglots
curl -GET http://localhost:5000/parkinglots/{id}
```

You will be able to POST, PUT and DELETE only by a valid token.
You can recieve a valid token by login
```bash
curl --user magnusoy:password http://localhost:5000/login
```

Check if your token is valid
```bash
curl -GET http://localhost:5000/protected?token={yourtoken}

{"message":"This is only available for people with valid tokens."}
```

```bash
curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"name":"Parkinglot", "location":"62.733471,7.1434657", "size":20, "empty":20}' http://localhost:5000/parkinglots?token={yourtoken}

{"empty":20,"id":39,"location":"62.733471,7.1434657","name":"Parkinglot","size":20}
```

### Usage

There is also made a SmartPark-Client application which comes with an UI.
The Client application will take care of all the API calls by updating the
status of your parkinglot.

Go to [SmartPark-Client](https://github.com/magnusoy/SmartPark-Client) for more imformation setting it up.

To run development server :
```bash
cd ~/SmartPark-Client
flask run
```
Press Ctrl+C in the terminal to close the server.

The development server will now run on: http://localhost:5000/




## Built With

* [Python](https://www.python.org/) - Python

## Contributing

If you want to contribute or find anything wrong, please create a Pull request, or issue addressing the change, or issue.


## Author

* **Magnus Øye** - [magnusoy](https://github.com/magnusoy)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/magnusoy/SmartPark-Server/blob/master/LICENSE) file for details


## Libraries

[Flask](http://flask.pocoo.org/)

[Flask-Mail](https://pythonhosted.org/Flask-Mail/)

[Flask-Marshmellow](https://flask-marshmallow.readthedocs.io/en/latest/)

[Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/)

[Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/)
