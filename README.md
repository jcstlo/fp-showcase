# Docker Commands

* Start container: `docker-compose up -d`
  * To force building a new image, add the `--build` flag (e.g. if you change `requirements.txt`)
* Stop container: `docker-compose down`
* To run commands within the Docker container: `docker-compose exec [service_name] [command]`
  * e.g. `docker-compose exec web python manage.py test`

# First start up

* `docker-compose up -d --build`
* `docker-compose exec web python manage.py migrate`