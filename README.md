# SellerShield

SellerShield is a Django-based web application designed to help Amazon sellers manage and dispute return charges. The platform allows sellers to track returns, flag suspicious returns, and file disputes to challenge Amazon's return charges when they believe the returns to be fraudulent.

## Features

- **Order Management**: Allows sellers to create, update, and view order details.
- **Return Management**: Track returns, view the reason for return, and validate returns.
- **Dispute Management**: Allows sellers to create and manage disputes for suspicious returns.
- **User Roles**: Supports multiple roles like Sellers, Admins, and Customer Agents.
- **HTMX Integration**: Dynamic UI updates without reloading the page for a better user experience.
- **Pagination**: List views are paginated for better scalability and performance.
- **Dockerized**: The application is containerized with Docker, ensuring portability and easy setup across different environments.

## Prerequisites

- **Python 3.9+**
- **PostgreSQL** (if using Postgres for database)
- **Docker** (optional, for containerized deployment)
- **pipenv** or **virtualenv** (for dependency management)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/sellershield.git
cd sellershield

2. Create and activate a virtual environment
Using venv:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables
POSTGRES_DB=sellershield
POSTGRES_USER=sellershielduser
POSTGRES_PASSWORD=yourpassword
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

5. Run database migrations
python manage.py makemigrations
python manage.py migrate

6. Create a superuser (optional, for accessing Django Admin)
python manage.py createsuperuser

6 a: Run the Management Command
python manage.py create_users

After running the command, the following users will be created:

Seller Users: seller1, seller2 (part of the Seller group)
Customer Agent Users: agent1, agent2 (part of the Customer Agent group)
Admin Users: admin1, admin2 (part of the Admin group, with is_staff=True and is_superuser=True)
password for all user -password123
Verify the Users and Groups
Running the python manage.py shell command and inspecting the users in the database:
# Check for admin users
admin_users = User.objects.filter(groups__name='Admin')
print(admin_users)

# Check for seller users
seller_users = User.objects.filter(groups__name='Seller')
print(seller_users)

# Check for customer agent users
agent_users = User.objects.filter(groups__name='Customer Agent')
print(agent_users)


7. Run the development server
python manage.py runserver
Access the application at http://localhost:8000

Docker Setup (Optional)
1. Build and run Docker containers

2. Run database migrations inside the container
docker-compose run web python manage.py migrate


Key Technologies
Django: Backend web framework.
PostgreSQL: Database management system.
HTMX: For dynamic, single-page-like interactions without page reloads.
Bootstrap: For responsive UI components.
Docker: Containerization of the app for easy deployment.


File Structure
sellershield/
│
├── sellershield/                  # Django project directory
├── orders/                        # Orders app
├── returns/                       # Returns app
├── disputes/                      # Disputes app
├── manage.py                      # Django management script
├── Dockerfile                     # Dockerfile for building the app
├── docker-compose.yml             # Docker Compose setup
├── requirements.txt               # Python dependencies
├── .env                           # Environment variables (for local dev)
└── README.md                      # Project documentation
```
