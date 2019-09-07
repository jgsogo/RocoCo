
Backend
=======


Make it work
------------

**Requirements:** Python 3.x installed and working. Run ``python --version``

You can clone repo and install this project in any directory, we will
refer to it with ``<folder>`` in the following commands.

First thing we have to do is to configure the Python environment:

 * Clone the repo and move into it:
   ```bash
   cd <folder>
   git clone https://github.com/jgsogo/RocoCo.git
   cd RocoCo
   ```
 * We are going to use a python virtualenvironment to run the project. We will create
   the virtualenv inside the repo (just for convenience):
   ```bash
   python -m venv _venv/rococo
   source <folder>/_venv/rococo/bin/activate
   ```
   To exit the virtualenv, just type ``deactivate``.
 * Now let's install the requirements:
   ```bash
   pip install -r backend/requirements.txt
   ```

Next step is to create and configure the Django project:
 * Create the database:
   ```bash
   cd <folder>/RocoCo/backend/rococo
   python manage.py migrate
   ```
 + We need a user to access the admin interface (use any name and
   password when prompted):
   ```bash
   python manage.py createsuperuser
   ```

Everything is ready, let's run it:

```bash
cd <folder>/RocoCo/backend/rococo
python manage.py runserver
```

Open ``http://127.0.0.1:8000/admin/`` to access the admin interface, there you
will need to create some objects to populate the database.

The Rest API should have started at ``http://127.0.0.1:8000/walls/``, there are
an HTML and a JSON views.

Enjoy!
