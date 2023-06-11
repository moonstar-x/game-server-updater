import os
from dataclasses import dataclass
import yaml


@dataclass
class Config:
  steamcmd_location: str
  gameserver_root_location: str
  steam_username: str


def load_config(config_file: str) -> Config:
  if not os.path.exists(config_file):
    raise Exception(f'Config file {config_file} does not exist.')

  with open(config_file, 'r') as file:
    yml = yaml.safe_load(file)
    return Config(**yml)
