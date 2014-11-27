Provisioning a new site
=======================

## Required packages:

* nginx
* python (currently 2)
* Git
* pip
* virtualenv
* postgresql
* yolk(optional for easier packages listing)

eg, on Ubuntu:
	sudo apt-get install nginx git python python-pip
	sudo pip install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with ,e.g superlists-ojan.com

## Upstart job
* see gunicorn.template.conf
* replace SITENAME with ,e.g superlists-ojan.com

## Foldet structure

/home/ojan
|__SITENAME
   |--source
   |--static
   |--virtualenv
