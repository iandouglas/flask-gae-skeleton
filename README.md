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
pip install -r requirements.txt -t lib
```

## app.yaml

You'll need to register a project at Google App Engine and there you'll choose a unique project name which will be a 
prefixed subdomain to appspot.com, something like "myproject.appspot.com". In this example, 
I'd use "myproject" in the place of "some-unique-name" at the top of app.yaml


## tests

Please consider developing your project using TDD principles, it will make your life so much easier.

I've already got you started with a test_flask.py script under /tests/unit/ which will test that Flask starts up 
properly, and also tests the 404 page. At some point, I'll add some basic feature/integration tests as well using
the splinter package.


## What's with all of the .keep files

These are simple placeholder files so folders will be added to git in the easiest manner. Once you have files in the 
folders, the .keep files are safe to delete.


## What are the .haml files and .scss? Do I really need them?

I use HAML as a shortcut to writing proper HTML. You're welcome to remove them, but once you understand the simplicity
of HAML, I'm guessing you'll keep HAML around. While it's not very Pythonic, to get HAML working, you'll need Ruby 
installed on your system and a simple "gem install haml" (possibly with sudo) should be all you need.

Likewise with the .scss files, they allow for writing nested CSS which them compiles down into semantically-correct 
CSS files. You'll need to "gem install sass" (possibly with sudo)

I use PyCharm as my preferred Python editor, and the professional edition will detect the HAML and SCSS files and 
prompt you to add "watchers" which will run the HAML/SCSS compilers for you whenever your files get saved. Any manual
changes you make to the .html or .css files will be lost when the compilers run.
