from typing import List
from lib.config import Config
from lib.steamcmd import GameServerUpdater


class Updater(GameServerUpdater):
  APP_ID = '223350'

  def __init__(self, config: Config):
    super().__init__(config, 'DayZ Dedicated Server', 'dayz')

  def create_args(self) -> List[str]:
    return [
      '+force_install_dir', self.destination_dir,
      '+login', self.username,
      '+app_update', Updater.APP_ID,
      '+quit'
    ]
