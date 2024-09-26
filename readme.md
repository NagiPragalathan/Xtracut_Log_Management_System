# Xtracut Log Management System

## Overview

The **Xtracut Log Management System** is a comprehensive dashboard built using the Django framework to monitor various plugins utilized by users. It provides real-time insights into plugin usage, allowing users to filter data by time periods such as 1 day, 1 week, 1 month, or custom date ranges. This system is designed to help administrators easily track the status of plugins, view detailed logs, and assess the performance or errors occurring across different users.

## Features

- **Plugin Monitoring**: Track and monitor the usage of plugins by different users.
- **Filters**: Filter data by specific time frames (1 day, 1 week, 1 month) or define a custom date range.
- **User-specific Insights**: View plugin usage details and errors specific to individual users.
- **Dashboard Overview**: Visual representation of plugin activity, including success and failure rates.
- **Status Indicators**: Displays the current status of each plugin (active/inactive/errors).
- **Real-Time Updates**: Automatically updates the status of plugins in real-time.
- **Django-based Backend**: Built using the Django web framework with MongoDB for data storage.

## Installation

Follow the steps below to set up the **Xtracut Log Management System** locally:

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- MongoDB
- pip (Python package manager)

### Steps

1. **Clone the repository**:
    
    ```bash
   git clone https://github.com/NagiPragalathan/Xtracut_Log_Management_System.git cd Xtracut_Log_Management_System
    ```
    
3. **Create a virtual environment** (recommended):
    
    ```bash
     python -m venv venv source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
    
4. **Install required dependencies**:
    
    ```bash
     pip install -r requirements.txt
    ```
    
5. **Configure MongoDB**:
    
    - Ensure MongoDB is running locally or configure the connection in `settings.py`:
        
      ```python
      DATABASES = {
          'default': {
          'ENGINE': 'djongo',
          'NAME': 'your_database_name',
          'HOST': 'localhost',
          'PORT': 27017,
      } }
      ```  
6. **Run migrations**:
    
    ```bash
    python manage.py migrate
    ```
    
7. **Create a superuser** (for accessing the Django admin panel):
    
    ```bash
    python manage.py createsuperuser
    ```
    
8. **Start the development server**:
    
    ```bash
    python manage.py runserver
    ```
    
9. **Access the system**: Open your web browser and navigate to:
    

    ```bash
    http://localhost:8000
    ```
    
## Technologies Used

- **Backend**: Django (Python Framework)
- **Database**: MongoDB
- **Frontend**: HTML, CSS, JavaScript
- **Version Control**: Git
  
## Usage

1. Log in to the dashboard using your admin credentials.
2. Navigate to the plugin monitoring section to view plugin usage data.
3. Apply filters (1 day, 1 week, 1 month, or custom date range) to analyze plugin activities over specific time periods.
4. Drill down into user-specific data to investigate plugin performance or errors.
5. Monitor the status of each plugin in real-time and address any issues as they arise.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software as per the terms outlined in the license file.

## Contributors

We would like to thank the following contributors for their hard work:

- [NagiPragalathan](https://github.com/NagiPragalathan)
- [Tarunika](https://github.com/Tarunika-R)
- [Praveena](https://github.com/Praveena-Krishnan)

## Contribution

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.
