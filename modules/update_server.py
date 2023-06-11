import dumb_menu
from lib.config import Config
from lib.servers import updater_classes


def run(config: Config) -> None:
  updaters = [Updater(config) for Updater in updater_classes]
  updaters.sort(key=lambda x: x.name)
  options = [f'Update {x.name}' for x in updaters]

  index_chosen = dumb_menu.get_menu_choice(options)
  updaters[index_chosen].run()
