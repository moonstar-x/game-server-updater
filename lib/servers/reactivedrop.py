from typing import List
from lib.config import Config
from lib.steamcmd import GameServerUpdater


class Updater(GameServerUpdater):
  APP_ID = '582400'

  def __init__(self, config: Config):
    super().__init__(config, 'Alien Swarm Reactive Drop Dedicated Server', 'reactivedrop')

  def create_args(self) -> List[str]:
    return [
      '+force_install_dir', self.destination_dir,
      '+login', 'anonymous',
      '+app_update', Updater.APP_ID,
      '+quit'
    ]
