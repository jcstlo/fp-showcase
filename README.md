# Docker Commands

* Start container: `docker-compose up -d`
  * To force building a new image, add the `--build` flag (e.g. if you change `requirements.txt`)
* Stop container: `docker-compose down`
* To run commands within the Docker container: `docker-compose exec [service_name] [command]`
  * e.g. `docker-compose exec web python manage.py test`

# First start up

* `docker-compose up -d --build`
* `docker-compose exec web python manage.py migrate`
* `docker-compose exec web python manage.py createsuperuser`

# Production deployment steps (with HTTPS)

## Prerequisites:

* You own a domain name
* A running Linux VPS with Docker and Docker Compose (e.g. DigitalOcean droplet)

## Steps

* Copy the sample docker-compose file with `cp docker-compose-prod-sample.yml docker-compose-prod.yml`
  * In `docker-compose-prod.yml`, replace environment variables that have `__REPLACE_ME__`
* Start the containers
  * Run `docker compose -f docker-compose-prod.yml up -d --build` to start the containers
  * Run `docker compose exec web python manage.py migrate` to run database migrations
  * Run `docker compose exec web python manage.py collectstatic` to collect all static assets for nginx to server
* Check if the website is available at `https://<domain_name_here>`
  * Note that `ACME_CA_URI` environment variable is using Let's Encrypt's staging environment, so an error ("Your connection is not private") is expected
    * Click on "Advanced" and then on "Proceed"
  * Try creating a new user, uploading a picture, and checking if static assets load properly
* Once the step above is confirmed, you can now switch to Let's Encrypt's production environment
  * Run `docker compose -f docker-compose-prod.yml down`
  * Run `docker volume prune -a`
  * Comment out the line with `ACME_CA_URI` in `docker-compose-prod.yml`
  * Run `docker compose -f docker-compose-prod.yml up -d --build` to start the containers
* Re-run the `migrate` and `collectstatic` commands from earlier, since all the volumes were pruned
* The website should now be available at `https://<domain_name_here>`!