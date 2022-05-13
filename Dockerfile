# DESCRIPTION:	  Deploys Wealth Indicator Calculators in Container
# COMMENTS:
#	This file describes how to deploy Wealth Indicator Calculators
#	in a container with all dependencies installed.
# USAGE:
#	# Download WIC Dockerfile
#	wget [link]
#
#	# Build image
#	docker build -t wi-calc .
#
#   # run docker container
#	docker run -d -p 80:8000 wi-calc
#

# choose baseimage
FROM python

# set initial Working Directory
WORKDIR /

# create project directory and set as workding directory
ENV GP_DIR="/wi-calc"
RUN [ -d ${GP_DIR} ] || mkdir -p ${GP_DIR}
WORKDIR ${GP_DIR}

# copy project files
COPY . .

# install requirements
RUN python -m pip install -r requirements.txt

# check for errors in application
RUN python manage.py check

# migrate database
RUN python manage.py makemigrations
RUN python manage.py migrate

# collect static images
RUN python manage.py collectstatic

# expose ports
EXPOSE 8000

# start application
CMD [ "gunicorn", "Calculators.wsgi", "-b", "0.0.0.0:8000" ]