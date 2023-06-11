import os
from abc import ABC, abstractmethod
from typing import List
import subprocess
from lib.config import Config


class GameServerUpdater(ABC):
  def __init__(self, config: Config, name: str, destination_dir: str):
    self.__config = config
    self.__name = name
    self.__destination_dir = destination_dir

  @property
  def name(self) -> str:
    return self.__name
  
  @property
  def username(self) -> str:
    return self.__config.steam_username
  
  @property
  def destination_dir(self) -> str:
    return os.path.abspath(os.path.join(self.__config.gameserver_root_location, self.__destination_dir))

  @abstractmethod
  def create_args(self) -> List[str]:
    pass

  def pre_run(self) -> None:
    print(f'Will update {self.name} to destination {self.destination_dir}')

  def post_run(self) -> None:
    pass

  def run(self) -> None:
    self.pre_run()

    proc = subprocess.Popen([
      self.__config.steamcmd_location,
      *self.create_args()
    ])
    proc.communicate()
    
    self.post_run()
