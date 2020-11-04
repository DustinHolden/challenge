# Challenge
This is the response to the coding challenge received from Genesis Research.

## Project Structure
You will find that the settings have been broken into four files. `common.py`,`local.py`,`test.py`,`production.py`.

`common.py` gives us a base file that is inherited in the other three files. The settings in these files are overridden 
in each file if needed.

`local.py` is a configuration for local development, these settings should not ever be used in a production environment.
 They will and can expose sensitive information.

`test.py` is a configuration for test environments. Much like `local.py` these files should not be used in production. 
This file should be referenced when running automated tests.

`production.py` is the configuration that should be used when deploying to a production environment. This file is 
configured to run a Django server behind a load balancer that terminates SSL. These are sane configurations, but should 
be reviewed before placing in to a production environment.

## Environment Installation
This project was built using Python 3.8, but should work on any version that is 3.6+. To run this environment you can 
follow the below steps.

1. Clone from the repository `clone https://github.com/DustinHolden/challenge.git`
2. cd into the root directory
3. Create a virtualenv (e.g. `python3 -m venv ./venv`) using your preferred method
4. Activate your environment, `source ./venv/bin/activate`
5. Install the requirements. `pip install -r requirements.txt`
6. Run database migrations `./manage.py migrate`
7. Run development server `./manage.py runserver`

### Caveats
This project was set up to use the Argon2 password hasher. If you encounter any issues installing requirements, you can 
comment out `'django.contrib.auth.hashers.Argon2PasswordHasher'` and remove `argon2-cffi==20.1.0` from the 
requirements.txt file. Argon2 is the recommended password hasher for Django, but is not included by default.

Django-Environ was used to build most of the settings files. This library is very helpful in setting sane defaults for 
each configuration. Though, you will note that there are not many defaults set in the `production.py` because we want 
to reference these settings from the servers environment. If we do not want to reference them from the servers 
environment, we can distribute a `.env` file with these variables set. In most cases we want to keep the `.env` file 
outside of version control.

## Production Recommendations
A few items that were left out of the production set up were error logging, performance monitoring, and cloud storage. 
I recommend using [Sentry](https://sentry.io/) for error logging, [New Relic](https://newrelic.com/) for performance 
monitoring, and [django-storages](https://django-storages.readthedocs.io/en/latest/) for interacting with different 
cloud providers.

## Interacting with the API
For your convenience, a registration process was included. You can access it 
[here](http://127.0.0.1:8000/rest-auth/registration/). Once you `POST` your response, you will receive a token. This 
token must be used in the REST API calls. Include this token in the `Authorization` header with a value in this format 
`Token YOUR_TOKEN_HERE`.

You can also browse the API via the Django Rest Framework browsable API by going [here](http://127.0.0.1:8000/api/). 
You will still need to be logged in to access any information.

The Django admin has also been made available to create, update, or delete any information. You will need to create a 
user with the appropriate authorization to access the admin. `./manage.py createsuperuser` is the quickest way to add a 
superuser. Then you can log into the admin [here](http:/127.0.0.1:8000/admin/).