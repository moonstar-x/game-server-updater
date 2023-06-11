from lib.config import Config
from lib.servers import updater_classes


def run(config: Config) -> None:
  updaters = [Updater(config) for Updater in updater_classes]
  updaters.sort(key=lambda x: x.name)

  for updater in updaters:
    updater.run()
