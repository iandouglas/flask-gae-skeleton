# Flask GAE Skeleton

I often find myself starting new projects all the time with Python/Flask for Google App Engine, and wanted a skeleton
project from which I could get started quickly.


## A work in progress

I'll be tweaking this over time. It's not perfect and there's still a lot I want to add, such as Javascript testing.


## virtualenv

I recommend installing an actual virtualenv for your project, but App Engine will also need your external packages
installed in the /lib/ folder here. Remember that App Engine can only support 100% Python packages. Anything that
compiles a C/C++ library cannot be used on GAE.

```
virtualenv myproject

# linux/mac:
myproject/bin/activate

# windows:
myproject\scripts\activate

# install all requirements into your virtualenv
pip install -r requirements.txt

# install all requirements into your /lib/ folder as well, but only the packages
# this is necessary because packages need to be sent to App Engine as well
pip install -r requirements.txt -t lib
```

## app.yaml

You'll need to register a project at Google App Engine and there you'll choose a unique project name which will be a
prefixed subdomain to appspot.com, something like "myproject.appspot.com". In this example, I'd use "myproject" in the
place of "your-unique-project-name-here" at the top of app.yaml


## config.py

You should change the values in config.py such as SECRET_KEY to something long and unique. I usually string several UUID
strings together. I've got code in config.py right now that should alert you via Email when an error occurs on the site
but this is untested at the moment. I recommend using SendGrid, though you'll want to use their web API instead of SMTP
access, as App Engine gives you several hundred thousand web API calls to third party services per day as part of their
quota, but their low-level socket connections may be more limited. SendGrid is a Google Cloud Platform partner, and
also my employer.

You should also change the Google Analytics ID configuration setting if you want to gather data about who visits your
site and generate reports, etc..

You could inherit the AppConfig class and override certain settings for default (development), testing, and production
modes.


## tests

Please consider developing your project using TDD principles, it will make your life so much easier.

I've already got you started with a test-driven setup under /tests/ which will test that Flask starts up
properly, and also tests static pages such as the 404 page. I've also added integration tests using Splinter.

You can easily run the tests within PyCharm (my editor of choice), or you can run them from the command line:

```python run_tests.py```

The tests require access to the Google App Engine SDK.  You can specify the location of your installed SDK with an
environment variable:

Linux / MacOS:

```export GOOGLE_APP_ENGINE_SDK=asdf```

Windows:

```set GOOGLE_APP_ENGINE_SDK=C:\Program Files\Google\App Engine```

## What are the .haml files and .scss? Do I really need them?

I use HAML as a shortcut to writing properly-formatted HTML. You're welcome to remove them, but once you understand
the simplicity of HAML, I'm guessing you'll keep HAML around. While it's not very Pythonic, to get HAML working,
you'll need Ruby installed on your system and a simple "gem install haml" (possibly with sudo) should be all you need.

Likewise with the .scss files, they allow for writing nested CSS which them compiles down into semantically-correct
CSS files. You'll need to "gem install sass" (possibly with sudo)

I use PyCharm as my preferred Python editor, and the professional edition will detect the HAML and SCSS files and
prompt you to add "watchers" which will run the HAML/SCSS compilers for you whenever your files get saved. Any manual
changes you make to the .html or .css files will be lost when the compilers run.

The .haml and .scss files are ignored via the app.yaml file so they won't end up on App Engine as part of your deploy.


## How do I deploy to App Engine?

appcfg.py update .
