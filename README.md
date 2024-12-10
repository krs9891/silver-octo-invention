# silver-octo-invention
## Project Description

This is a basic Django application that implements a REST API for managing a currency exchange database. The application fetches data from an external API (Yahoo Finance) and stores it in a local database. It also allows viewing historical exchange rates in the admin interface and exporting these rates to an XLSX file.

## Specification

### Endpoints

- **GET /currency/EUR/USD/** 
    - Fetches a list of all currency pairs already present in the local application database.
    - Example result: `{"currency_pair": "EURUSD", "exchange_rate": 1.034}`

## Requirements

- Python 3.11
- Django 5.1.4
- yfinance
- openpyxl
- Other requirements are listed in the `requirements.txt` file.

## Usage Instructions

### Running on GitHub Codespaces

1. Open the project repository on GitHub.
2. Click the Code button and select Open with Codespaces.
3. If you don't have a Codespace created, click New codespace.
4. The Codespace will automatically install the required packages, run database migrations, fetch currency exchange rates from external API and create a superuser with credentials provided in the `devcontainer.json`:

    ```
    "containerEnv": {
        "DJANGO_SUPERUSER_USERNAME": "admin",
        "DJANGO_SUPERUSER_EMAIL": "admin@example.com",
        "DJANGO_SUPERUSER_PASSWORD": "admin"
    },
    ```

5. Start the development server:
    ```sh
    python manage.py runserver
    ```


### Running with Dev Container

1. Ensure you have Docker and Visual Studio Code with the Remote - Containers extension installed.
2. Open the project in Visual Studio Code.
3. Open the command palette (Ctrl+Shift+P) and select `Remote-Containers: Reopen in Container`.
4. The Dev Container will automatically install the required packages  run database migrations, fetch currency exchange rates from external API and create a superuser with credentials provided in the `devcontainer.json`:

    ```
    "containerEnv": {
        "DJANGO_SUPERUSER_USERNAME": "admin",
        "DJANGO_SUPERUSER_EMAIL": "admin@example.com",
        "DJANGO_SUPERUSER_PASSWORD": "admin"
    },
    ```


5. Start the development server:
     ```sh
     python manage.py runserver
     ```
6. The application will be available at [http://localhost:8000](http://localhost:8000).

### Running Locally

1. Clone the repository:
     ```sh
     git clone https://github.com/krs9891/silver-octo-invention.git
     cd silver-octo-invention
     ```
2. Create and activate a virtual environment:
     ```sh
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```
3. Install the required packages:
     ```sh
     pip install -r requirements.txt
     ```
4. Run database migrations:
     ```sh
     python manage.py migrate
     ```
5. Fetch currency exchange rates:
     ```sh
     python manage.py fetch_rates
     ```
6. Create a superuser:
     ```sh
     python manage.py createsuperuser
     ```
7. Start the development server:
     ```sh
     python manage.py runserver
     ```
8. The application will be available at [http://localhost:8000](http://localhost:8000).

## Tests

To run tests, use the following command:
```sh
python manage.py test
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.