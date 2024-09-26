# Finalty Django Project

This README provides essential information about the Finalty Django project, including details on Python version, installation, and running the project. Additionally, it outlines the project structure and lists the required dependencies.

## Project Details

### Python Version

This project is developed using Python 3.x. Ensure that you have Python 3.x installed on your system.

### How to Run

1. **Clone the Repository:**
    
    ```bash
    git clone https://github.com/finaltyfintech/Finalty.git
    cd Finalty
    ```
    
2. **Install Dependencies:**
    
    ```bash
    pip install -r requirements.txt
    ``` 
    
3. **Run Migrations:**
    
    ```bash 
    python manage.py migrate
    ``` 
    
4. **Start the Development Server:**
    
    ```bash 
    python manage.py runserver
    ``` 
    
    The development server will run on `http://127.0.0.1:8000/` by default.
    

### Project Structure

The project is organized into the following directories:

- **base:** Contains Django app related to the base functionality of the project.
    - `admin.py`: Django admin configurations.
    - `apps.py`: App configuration.
    - `models.py`: Database models.
    - `sitemaps.py`: Django sitemaps.
    - `tests.py`: App-specific tests.
    - `views.py`: Views for the app.
    - `migrations/`: Database migration files.
    - `templatetags/`: Custom template tags.
- **Finalty:** Django project settings and configurations.
    - `asgi.py`: ASGI configuration.
    - `settings.py`: Project settings.
    - `urls.py`: Project-level URLs.
    - `wsgi.py`: WSGI configuration.
- **static:** Contains static files for the project.
    - `images/`: Image assets used in the project.
- **templates:** HTML templates used in the project.
    - `backup/`: Backup templates.
    - `index.html`: Main index template.
    - `list_out.html`: List output template.
    - `underdev.html`: Under development template.

### Project Dependencies

Ensure you have the following Python packages installed:

- `djongo==1.3.6`
- `djangorestframework`
- `django==4.1.9`
- `pymongo==3.12.3`
- `django-cors-headers`
- `dnspython`
- `requests`
- `djangorestframework-jwt`
- `djangorestframework-simplejwt`
- `django-meta`
- `django-robots-txt`

## Additional Files

- `build_files.sh`: Shell script for building files.
- `note.txt`: Additional notes related to the project.
- `robots.txt`: Configuration for search engine spiders.
- `vercel.json`: Configuration for Vercel deployment.

## Views Overview

1. **Home View (`Home` function)**
    
    - Renders the `index.html` template.
    - URL: `/`
2. **List Out View (`list_out` function)**
    
    - Retrieves all contact data from the `Contact_us` model.
    - Renders the `list_out.html` template with the contact data.
    - URL: `/list_out/`
3. **Delete Contact View (`delete_contact` function)**
    
    - Handles deletion of contact records based on the provided `contact_id`.
    - Expects a GET request with the `contact_id` parameter.
    - Returns a JSON response indicating the success or failure of the deletion.
    - URL: `/delete_contact/`
4. **Under Development View (`underdev` function)**
    
    - Renders the `underdev.html` template.
    - URL: `/underdev/`
5. **Contact Form View (`contact_form` function)**
    
    - Handles form submissions for contact information.
    - Expects a POST request with form data (first name, last name, email, and message).
    - Creates a new `Contact_us` record in the database.
    - Redirects to the home page after form submission.
    - URL: `/contact_form/`
6. **Robots.txt View (`robots_txt` function)**
    
    - Generates a `robots.txt` file for search engine optimization (SEO).
    - Specifies rules for web crawlers, disallowing access to certain paths.
    - URL: `/robots.txt/`

## How to Use Views

### Home View

- Access the home page by navigating to `/`. The `index.html` template will be rendered.

### List Out View

- View the list of contacts by navigating to `/list_out/`. The `list_out.html` template will display the contact data.

### Delete Contact View

- To delete a contact, send a GET request to `/delete_contact/` with the `contact_id` parameter. The response will indicate whether the deletion was successful.

### Under Development View

- Access the under development page by navigating to `/underdev/`. The `underdev.html` template will be rendered.

### Contact Form View

- Submit contact information through the form at `/contact_form/`. The form accepts first name, last name, email, and message. After submission, you will be redirected to the home page.

### Robots.txt View

- Access the `robots.txt` file for SEO configurations by navigating to `/robots.txt/`.

## Finalty Django Project - Contact\_us Model

The `Contact_us` model defines the structure of the database table used to store contact information in the Finalty Django project. This model is responsible for representing individual contact records.

## Model Fields

1. **`name` (CharField):**
    
    - Type: CharField with a maximum length of 255 characters.
    - Purpose: Stores the full name of the contact.
2. **`mail_address` (EmailField):**
    
    - Type: EmailField.
    - Purpose: Stores the email address of the contact.
3. **`message` (TextField):**
    
    - Type: TextField.
    - Purpose: Stores the message or additional information provided by the contact.
4. **`updated_time` (DateTimeField):**
    
    - Type: DateTimeField with `auto_now` set to True.
    - Purpose: Automatically updates the timestamp whenever the contact record is modified.

## Methods

1. **`__str__` method:**
    - Purpose: Provides a human-readable representation of the model instance.
    - Returns: The name of the contact as the string representation.

## Database Configuration (MongoDB)

The Finalty Django project uses MongoDB as the database backend, and the configuration is specified in the `settings.py` file.

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'CLIENT': {
            'host': "mongodb+srv://finaltyfintech:nagi@cluster0.vulge49.mongodb.net/?retryWrites=true&w=majority",
            'name': 'finaltyfintech',
            'authMechanism': "SCRAM-SHA-1",
        }
    }
}
```

Explanation:

- **`ENGINE`:** Specifies the Django database engine to use Djongo, which is a connector for using Django with MongoDB.
- **`CLIENT`:** Contains MongoDB connection details.
    - **`host`:** Specifies the MongoDB server's connection URI.
    - **`name`:** Specifies the name of the MongoDB database.
    - **`authMechanism`:** Specifies the authentication mechanism to use (in this case, SCRAM-SHA-1).

## Additional Details

- **MongoDB Connection URI:**
    - The MongoDB connection URI in the `host` field includes the necessary credentials (username and password), cluster information, and other connection options.
    - Note: It's recommended to keep sensitive information like database credentials secure and not hardcode them directly in the source code.

# Deploying Finalty Django Project on Vercel

This guide provides steps to deploy the Finalty Django project on Vercel, a cloud platform for frontend and serverless functions.

## Prerequisites

- [Vercel Account](https://vercel.com/signup)
- [Vercel CLI](https://vercel.com/download)

## Deployment Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-django-project.git
   cd your-django-project
2. **Install Dependencies:**
    
    `pip install -r requirements.txt` 
    
3. **Configure Vercel:**
    
    - Install Vercel CLI: `npm install -g vercel`
    - Run `vercel login` to log in to your Vercel account.
4. **Create Vercel Configuration File:**
    
    - Create a `vercel.json` file in the project root directory.
    - Example `vercel.json`:
        
        ```json
        {
          "version": 2,
          "builds": [
            {
              "src": "Finalty/settings.py",
              "use": "@vercel/python",
              "config": {
                "maxLambdaSize": "15mb"
              }
            }
          ]
        }
        ```
        
5. **Deploy to Vercel:**
    
    - Run `vercel` in the project root directory.
    - Follow the prompts to configure your deployment.
6. **Environment Variables:**
    
    - Set the necessary environment variables in the Vercel dashboard, especially those related to your Django project settings.
7. **Finalize Deployment:**
    
    - After deployment, Vercel will provide a unique URL for your Django project.
8. **Access Your Django App:**
    
    - Visit the provided URL to access your deployed Django app.

## Additional Notes

- Make sure your Django project is configured to allow requests from the Vercel domain in the `ALLOWED_HOSTS` setting.
    
- Adjust Django settings accordingly, especially if using a different database or secret keys.
    
- For detailed Vercel deployment options, refer to the Vercel Documentation.

# Structure of the site

```bash
Finalty
│   build_files.sh
│   manage.py
│   note.txt
│   readme.md
│   requirements.txt
│   robots.txt
│   vercel.json
│
├───base
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   sitemaps.py
│   │   tests.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │   │   0001_initial.py
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           0001_initial.cpython-311.pyc
│   │           __init__.cpython-311.pyc
│   │
│   ├───templatetags
│   │   │   djtemp.py
│   │   │
│   │   └───__pycache__
│   │           djtemp.cpython-311.pyc
│   │
│   └───__pycache__
│           admin.cpython-311.pyc
│           apps.cpython-311.pyc
│           models.cpython-311.pyc
│           sitemaps.cpython-311.pyc
│           views.cpython-311.pyc
│           __init__.cpython-311.pyc
│
├───Finalty
│   │   asgi.py
│   │   settings.py
│   │   urls.py
│   │   wsgi.py
│   │   __init__.py
│   │
│   └───__pycache__
│           settings.cpython-311.pyc
│           urls.cpython-311.pyc
│           wsgi.cpython-311.pyc
│           __init__.cpython-311.pyc
│
├───static
│   └───images
│           logo.png
│           logo1.png
│
└───templates
    │   index.html
    │   list_out.html
    │   underdev.html
    │
    └───backup
            im.html
            index.html