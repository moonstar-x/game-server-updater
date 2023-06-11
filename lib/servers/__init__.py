import os
import importlib


updater_classes = [importlib.import_module(f'.{file.replace(".py", "")}', package=__name__).Updater for file in os.listdir(os.path.dirname(__file__)) if not file.startswith('__') and file.endswith('.py')]
