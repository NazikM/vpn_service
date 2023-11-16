# VPN SITE GUIDE

This Django project provides a VPN service with user profile management. The project is structured with three main apps: `user_management`, `vpn_service`, and `statistic`.

## Installation

### Prerequisites
- Docker installed on your machine

### Steps

1. Clone the repository:

   ```bash
   https://github.com/NazikM/vpn_service.git
   ```

2. Navigate to the project directory:

   ```bash
   cd vpn_service
   ```

3. Create a `.env` file in the project root with the following content:

   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   DB_NAME=...
   DB_USER=...
   DB_PASSWORD=...
   ```

   Replace `your_secret_key` with a secure Django secret key.

4. Build and run the Docker containers using `docker-compose`:

   ```bash
   docker-compose up --build
   ```

   This command will set up the Django project and its dependencies in Docker containers.

5. Apply database migrations:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

   This will apply the initial database migrations.

6. Create a superuser for the Django admin (Optional):

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser account.

7. Access the Django admin interface at [http://localhost:8000/admin/](http://localhost:8000/admin/) and log in with the superuser credentials.

## Routes

- Admin Interface: [http://localhost:8000/admin/](http://localhost:8000/admin/)
- User Profile:
  - Register: GET|POST [http://localhost:8000/profile/register/](http://localhost:8000/profile/register/)
  - Login: GET|POST [http://localhost:8000/profile/login/](http://localhost:8000/profile/login/)
  - Logout: GET [http://localhost:8000/profile/logout/](http://localhost:8000/profile/logout/)
  - Update Profile: GET|POST [http://localhost:8000/profile/< pk >/](http://localhost:8000/profile/)
- VPN Service:
  - Site List: GET [http://localhost:8000/vpn/list/](http://localhost:8000/vpn/list/)
  - Create Site: GET|POST [http://localhost:8000/vpn/create/](http://localhost:8000/vpn/create/)
  - Delete Site: GET|POST [http://localhost:8000/vpn/delete/< pk >/](http://localhost:8000/vpn/delete/)
  - VPN Route Handler: GET|POST [http://localhost:8000/vpn/<site_name>/<site_url>/](http://localhost:8000/vpn/<site_name>/<site_url>/)


Feel free to contribute, report issues, or submit pull requests!
