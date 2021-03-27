# flask-modular

A simple way to create modular and extensible apps based on the Flask framework
with full access the ecosystem of Flask extensions.

## Why not just use a blueprint?

Modules are more extensible than the existing Flask blueprints, and allow
modules to be hot-loaded, load from a configuration file and for code to be
executed on load, for instance, to initialize another Flask extension. And it's
all wrapped in a nice simple system with helpers and dependencies.

## Getting Started

It's as simple as:

```python
from flask import Flask
from flask_modular import ModuleManager

app = Flask(__name__)

manager = ModuleManager(app)
manager.load_modules()
```

Alternatively, you can initialize the manager on one or more applications 
using the `init_app` method:

```python
manager = ModuleManager()
manager.init_app(app)
```

## Entrypoint

In your `<module>/__init__.py` or `<module>.py` there should be a function
called `init_app` which takes a the `app` as it's sole parameter, that
then will do all the work of initializing your module:

```python

from flask_sqlalchemy import SQLAlchemy

from .controllers import model_controller
from .models import User

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    db.create_all([User])
    
    app.register_blueprint(model_controller)
```

This gives you all sorts of flexibility on what your module can do to your 
application once loaded without adding too many hard to remember custom
hooks, methods and classes that do the same thing.

## Dependencies

Modules can have dependencies, they will be automatically loaded before the
module is loaded (and will be loaded if not specified). Useful for having a 
generic module that initializes some extension and some that then use that
extension, or to extend an existing module:

```python
__depends__ = ['core', 'db']
```

## Configuration

Configuration is rather simple:

| Key               | Description                                           |
| ----------------- | ----------------------------------------------------- |
| `MODULES_PATH`    | The path to load custom modules from                  |
| `MODULES_TO_LOAD` | A list of modules to load when calling `load_modules` |

## License

Licensed under the [MIT License](./LICENSE.txt).