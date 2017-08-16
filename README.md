## Web Based DateTime Calculator

This is the DateTime Calculator using the web interface.

The following technologies are used in development:
* Python 2.7
* Flask micro web framework, version 0.12.2
* Jinja2 template engine
* WTForms 3.0dev
* pytz Python module
* Vim 7.4.8056
* Safari 10.1.2
* macOS Sierra, 10.12.6

## Steps for running the project in CentOS:
1. Install pip if it is not already installed
```sh
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python get-pip.py
```
2. Install Python virtual environment, this is to minimize clashes with other installed python modules and isolate project environment
```sh
$ sudo yum install python-virtualenv.noarch
```
3. Change directory to datesapp
```sh
$ cd <path>/<to>/datesapp
```
4. Create the virtual environment, named venv
```sh
$ virtualenv venv
```
5. Activate the newly created virtual environment
```sh
$ . venv/bin/activate
```
6. Install the Flask micro web framework using pip
```sh
$ pip install Flask
```
7. Install WTForms to manage web forms
```sh
$ pip install wtforms
```
8. Install pytz module to handle timezones
```sh
$ pip install pytz
```
9. Run the project
```sh
$ python dates.py
```
10. Finally open 127.0.0.1:5000 in browser

### More help in installation
Please follow [this link](http://flask.pocoo.org/docs/0.12/installation).
