# Django-Wagtail

## Project Overview
This is a Django Wagtail website that allows users to manage content with a multi-language home page. The home page should contain three sections(Slider Images, Vision Section, Latest News), each of which is
implemented using Wagtail's StreamField and custom blocks. The project is designed to be easily extendable and customizable, making it suitable for various types of content management needs.

## Setup Instructions

### 1. **Clone the Repository**

   ```bash
   git clone https://github.com/YasminaMohamed99/Django-Wagtail.git
   cd Django-Wagtail
   ```
### 2. **Create a Virtual Environment**
Ensure that Python 3.9 is installed on your machine. Then, create and activate a virtual environment:

```bash
  python3 -m venv .venv
   ```
### 3. **Activate the virtual environment**
* On macOS/Linux:
    ```bash
       source .venv/bin/activate
    ```
* On Windows:
    ```bash
      .venv\Scripts\activate
    ```
### 4. **Install Project Dependencies**
With the virtual environment activated, install the required dependencies:
```bash
  pip install -r requirements.txt
```
### 5. **Apply Database Migrations**
Apply the database migrations to set up the database schema:
```bash
  python manage.py migrate
```
### 6. **Run the Development Server**
Start the Django development server:
```bash
  python manage.py runserver
```


## Adding or Switching Languages in Wagtail
1. Log in to the Wagtail admin interface.
2. Navigate to the "Settings" section.
3. Click on "Locales" to manage available languages.
4. Add a new language.
5. Navigate to the "Page" section.
6. Select home according to language.
7. Add translation and make publish.
8. Navigate to "http://127.0.0.1:8000/es/" url according added language

## Lint
To run Ruff linting, use the following command:
```bash
  ruff check .
```

## Ruff Configuration
Ruff's configuration is specified in the .ruff.toml file, located in the root directory of the project. The key settings include:

* Line Length: Set to 88 characters.
* Selected Rules: "E", "W", "F" (these include most PEP 8 guidelines).
* Ignored Rules: "E501" (ignores line length warnings).