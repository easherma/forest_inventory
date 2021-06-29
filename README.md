# forest_inventory

an inventory of forests

# Discussion points

## Whats here

1. A fullstack Django app. It serves the data via templates, and has basic search and filter built in (and state stored via the browser URL)
2. The backend uses Postgres as a database.
3. I used `factory_boy` to autogenerate fake data for testing. This can help detect edge cases sooner and also deal with issues of scale earlier in development. For instance, though the instructions said that at least 3 forests needed to be created, if I only made 3 I would not have had to implement pagination! ;-)
4. I set up a Django REST Framework integration. Although this isn't used given the timeframe, it makes for an easy next step to wrap my backend in a RESTful API that could then be used to build a slicker frontend interface (using React, for example)
5. The frontend leverages Django's templates, with the addition of Bootstrap 5 as a familar and quick out-of-the-box solution, which also enabled me to quickly throw together a This means I didn't have significant amount of custom css or javascript to add to the project. If I did, I have Django's excellent static file compilation available.

## Stack Choices and trade-offs

Given the limited timeframe, I chose a mature stack I was familar with (Django). This allowed me to rapidly scaffold a project with minimal suprises.

A main trade-off here is that doing a SPA-style site, or having search and filter complete or browse to a forest detail page requires a page reload. Note that using Django neither is impossible at all, but I just didn't have time to implement that in the timeframe provided.

However, the project description and mockup did suggest a fairly traditional kind of site. My instinct is always to reach for the simplest, robust tool to do the job that lets me focus my creative energy on the actual problem space.

There are also alot of beneficall functionality that came along for the ride, such as url query parameters and routing, that would all have to be duplicated client-side going with a React approach. 

P.S. Just for fun, I did take a stab at this excercise using the stack mentioned in the job description (FastAPI with React, using SQLAlechemy and Postgres for the DB). I hadn't used FastAPI before and found it really interesting!

### TODOs:

- More test coverage
  - this implementation is very basic, and so additional tests beyond what is covered by the library I am using would mostly be to validate the concept. However, as the app's functionality would be fleshed out this would rapidly no longer be the case
  - I'd add end to end testing using cypress, and unit testing for any backend or frontend code as needed
- Create RESTful endpoints
  - as mentioned above, this would help refactor the app to a cleaner architecture and also lay a good foundation for frontend work using a framework like React or Vue, if desired
- Better frontend styling, better label names and formatting
  - this was definetly a rush job. I matched the mock in main principles, but I have a laundry list of design elements I would've tightened up
- Make filter, search, and detail browsing happen without page reload
  - There are ways to do this inside the Django app, or I could have moved things closer to a React integration
- Have better representation of geographic data (aka make a map!)
  - My background is in making web-maps. I have all sorts of ideas around better representing the forests other than listing the latitude and longitude (yuck)

## Getting started

Using docker, first run:

`docker-compose build`

Afterwards you should be able to run `docker-compose up -d` to have the app running at `localhost:8000/`

Once the containers are running, you'll need to run migrations and create an inital superuser (though the latter isn't really needed for this project)

As with any shell command that we wish to run in our container, this is done using the `docker-compose -f local.yml run --rm` command: ::

    `$ docker-compose -f local.yml run --rm django python manage.py migrate`
    `$ docker-compose -f local.yml run --rm django python manage.py createsuperuser`

## Add initial data

There is little to see here without some data to start with. Luckily I wrote a utility function to populate the data at a decent level of scale. To generate this data, run this command:

`docker-compose run --rm django python3 manage.py runscript generate_fake_data`

As is, this generates 50 fake forests, with one that has a title hardcoded as 'My Forest'. You can run it additively, so for instnance if you'd like 100 forests just run it twice.

### Test coverage

To run the tests, check your test coverage, and generate an HTML
coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

I did not have time to add significant test coverage. However, one advantage of the mature stack I chose is the easy availability of libraries that already have coverage!

#### Running tests with py.test

    $ pytest
