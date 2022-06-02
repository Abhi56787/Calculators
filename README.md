# Wealth Indicator Calculators

## Installation

- Clone or download the repository

  ```bash
  git clone https://github.com/Abhi56787/Calculators.git
  ```
  
- Change to repository Calculators directory

  ```bash
  cd Calculators
  ```
  
- Install requirements

  ```bash
  python3 -m pip install -r requirements.txt
  ```

- Migrate Database

  ```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

- Collect Static Files

  ```bash
  python3 manage.py collectstatic
  ```

- Check for errors

  ```bash
  python3 manage.py check
  ```

- Start Server using manage.py

  ```bash
  python3 manage.py runserver
  ```
  
- Access `Calculators` website using <http://127.0.0.1:8000> for local machine and `http://<your_local_ip>:8000` from local device.

## Docker

- Install [Docker Desktop](https://www.docker.com/) and check version

  ```bash
  docker --version
  ```

- Clone Project

  ```bash
  git clone https://github.com/Abhi56787/Calculators.git
  ```

- Change directory

  ```bash
  cd Calculators
  ```

- build image

  ```bash
  docker build -t wi-calc .
  ```

- Start container

  ```bash
  docker run -d -p 8000:8000 wi-calc
  ```

- Access project on <http://127.0.0.1>

## Notes

- Use `python` or `py` instead of `python3` for Windows machine
