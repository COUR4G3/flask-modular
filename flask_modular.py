from flask import current_app

import importlib
import sys


class ModuleManager:
    def __init__(self, app=None, **options):
        self.default_app = app
        self.options = options

        if app:
            self.init_app(app, **options)

    def __getattribute__(self, name):
        if name in ('init_app', 'get_app', 'get_state', 'load_module', 'load_modules',
                'default_app', 'options'):
            return object.__getattribute__(self, name)
        else:
            return getattr(self.get_state(), name)

    def init_app(self, app, **options):
        # combine default options and new options
        new_options = self.options.copy()
        new_options.update(**options)
        app.extensions['module_manager'] = ModuleManagerState(**new_options)

    def get_app(self):
        try:
            return current_app._get_current_object()
        except RuntimeError:
            if not self.default_app:
                raise RuntimeError('flask-modular is not initialized')
            return self.default_app

    def get_state(self):
        try:
            return self.get_app().extensions['module_manager']
        except KeyError:
            raise RuntimeError('flask-modular is not initialized for this app')

    def load_module(self, name_or_module, path=None):
        app = self.get_app()
        state = self.get_state()

        if isinstance(name_or_module, str):
            name = name_or_module
            if path:
                sys.path.insert(1, path)
            try:
                module = importlib.import_module(name_or_module)
            finally:
                if path:
                    sys.path.pop(1)
        else:
            module = name_or_module
            name = module.__name__

        depends = getattr(module, '__depends__', [])
        for depend in depends:
            if depend in state.modules:
                continue
            self.load_module(depend)

        init_app = getattr(module, 'init_app', None)
        if init_app:
            init_app(app)

        state.modules[name] = module

    def load_modules(self):
        app = self.get_app()
        path = app.config.get('MODULES_PATH', None)
        for name in app.config.get('MODULES_TO_LOAD', []):
            self.load_module(name, path=path)


class ModuleManagerState:
    def __init__(self, **options):
        self.modules = {}
        self.options = options
