# slafs-lp-blog
My blog with paid content


You can view it here:
https://radiant-meadow-8675.herokuapp.com

# stack

the site was build with:

- python
- django
- django-cms
- django-laterpay (for the paid content - COMING SOON!)

The site is deployed on Heroku.

# how to install this

- Clone the repo and go into it's root directory.
- Create python virutalenv `virtualenv my/env` and activate it.
- Install dependencies by `pip install -r requirements.txt`.
- Configure the project by env variables (`DATABASE_URL`, `DJANGO_DEBUG`, `DJANGO_SECRET_KEY`).
- Create database and a superuser `python ./manage.py syncdb`.
- Optionally, gather statifiles by doing `python ./manage.py collectstatic`.
- Run a development server `python ./manage.py runserver` and visit http://127.0.0.1:8000 to see the site.
- Deploy to heroku (learn more on: https://devcenter.heroku.com/articles/getting-started-with-django)

# idea

The idea is to have django-cms `placeholder` (`lp_placeholder`) tag that recognizes whether the user has
access to the content or not (which I didn't manage to do).

You can see my efforts in `paid_content/templatetags/paid_content_tags.py` and
`slafs_blog/templates/base.html`.

