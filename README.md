# Instructions

## Setup

1. Clone the project, run `pipenv install` inside the created directory.
2. `pipenv shell`
3. Apply the migrations.
4. Create a superuser.

## Triggering the bug

1. Access the browsable API and login with your admin user.
2. Go to `your_host:port/api/login`
3. Try a post with `{"username": "your_admin_username", "password": "your_admin_password"}`
4. Repeat it a few times, there shouldn't be any sign of throttling.

For reference, go to `your_host:port/api/throttled` and just refresh a few times to see expected throttling behaviour.

Note: For testing purposes I set the `anon` rate to `1/min`.
