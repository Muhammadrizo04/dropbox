[comment]: <> (<p align="center">)

[comment]: <> (  <img src="https://i.imgur.com/uoyXjst.png"/>)

[comment]: <> (</p>)

# PROJECT : DROPBOX

![python](https://img.shields.io/badge/-python-grey?style=for-the-badge&logo=python&logoColor=white&labelColor=306998)
![django](https://img.shields.io/badge/-django-grey?style=for-the-badge&logo=django&logoColor=white&labelColor=092e20)
![linux](https://img.shields.io/badge/linux-grey?style=for-the-badge&logo=linux&logoColor=white&labelColor=072c61)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)


### Outline
- #### Prerequisites
- #### Setup
    - #### Development
    - #### Staging
    - #### Production

### Prerequisites
- #### Language: python 3.12.3
- #### Frameworks : Django 5.0.4
- #### Deployment: gunicorn, gitlab ci/cd , system daemons
- #### Database : sqlite3 (soon postgresql 15)
- #### Redis (soon)
# Architecture
```
dropbox/
├── config/
│   ├── settings.py
│   ├── __init__.py
│   ├── asgi.py
│   ├── urls.py
│   └── wsgi.py
├── file_manager/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
├── common/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
├── media/
├── requirements.txt
├── static/
│   └── logo.png
├── .dockerignore
├── .env
├── .gitignore
├── .pre-commit-config.yaml
├── docker-compose.yml
├── entrypoint.sh
├── manage.py
├── pyproject.toml
├── README.md
└── start.sh
```


## Usage

1. Clone this repository to your local machine:

```bash
$ git clone https://github.com/Muhammadrizo04/dropbox.git
$ cd dropbox
```

2. Set up the project's virtual environment (recommended):

```bash
$ python -m venv venv
$ source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the project dependencies:

```bash
$ pip install -r requirements.txt
```

4. Set up the database (if applicable):

```bash
$ python manage.py migrate
```

5. Run the development server:

```bash
$ python manage.py runserver
```

Now your sample Django backend is up and running! You can access it at `http://localhost:8000/`.

## Contributing

If you'd like to contribute to this project or report any issues, please follow the guidelines outlined in the CONTRIBUTING.md file (if provided).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to reach out to the project maintainer:

- Name: Abdulla Abdukulov
- Email: abduqulovabdulla3108@gmail.com
- GitHub: [Abdulla Dev](https://github.com/abdullaabdukulov)

- Name: Muhammadrizo Muxtorov
- Email: muxtorovrizo@icloud.com
- GitHub: [Muhammadrizo Dev](https://github.com/Muhammadrizo04)
