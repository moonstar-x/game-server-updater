import os
import shutil
from typing import List
from pathlib import Path
from lib.config import Config
from lib.steamcmd import GameServerUpdater


class Updater(GameServerUpdater):
  APP_ID = '233780'
  GAME_APP_ID = '107410'

  MODS_APP_IDS = {
    '@ACE': '463939057',
    '@CBA_A3': '450814997',
    '@CUP_ACE_compat_vehicles': '621650475',
    '@CUP_ACE_compat_weapons': '549676314',
    '@CUP_Core': '583496184',
    '@CUP_CWA': '853743366',
    '@CUP_Maps': '583544987',
    '@CUP_Units': '497661914',
    '@CUP_Vehicles': '541888371',
    '@CUP_Weapons': '497660133',
    '@Enhanced_Movement': '333310405',
    '@RHSAFRF': '843425103',
    '@RHSGREF': '843593391',
    '@RHSSAF': '843632231',
    '@RHSUSAF': '843577117',
    '@ShackTac_UI': '498740884',
    '@task_force_radio': '620019431',
    '@Zombies_and_Demons': '501966277',
    '@Ravage': '1376636636',
    '@3CB_Factions': '1673456286',
    '@CUP_Maps2': '1981964169'
  }

  def __init__(self, config: Config):
    super().__init__(config, 'Arma 3 Dedicated Server', 'arma3')

  def pre_run(self) -> None:
    super().pre_run()

    mod_names = '  '.join(Updater.MODS_APP_IDS.keys())
    print('Will update the following mods:')
    print(mod_names)

  def create_args(self) -> List[str]:
    args = [
      '+@ShutdownOnFailedCommand', '0',
      '+force_install_dir', self.destination_dir,
      '+login', self.username,
      '+app_update', Updater.APP_ID
    ]

    for mod_app_id in Updater.MODS_APP_IDS.values():
      mod_args = ['+workshop_download_item', Updater.GAME_APP_ID, mod_app_id, 'validate']
      args = [*args, *mod_args, *mod_args]  # Adding it twice in case it fails at first.

    args.append('+quit')

    return args

  def post_run(self) -> None:
    for mod_name, mod_id in Updater.MODS_APP_IDS.items():
      mod_symlink_target = os.path.join(self.destination_dir, mod_name)
      mod_symlink_source = self.get_mod_dir(mod_id)

      if not Updater.symlink_exists(mod_symlink_target):
        Updater.create_symlink(mod_symlink_source, mod_symlink_target)
        print(f'Created symlink for {mod_name}: {mod_symlink_source} -> {mod_symlink_target}')

    print('Clearing old keys...')
    keys_dir = self.get_keys_dir()
    current_keys = [f for f in os.listdir(keys_dir) if f != 'a3.bikey']
    
    for key in current_keys:
      key_path = os.path.join(keys_dir, key)
      os.remove(key_path)

    print('Copying new keys...')
    new_keys = [f for f in Path(self.get_workshop_dir()).rglob('*.bikey')]
    
    for key in new_keys:
      key_destination = os.path.join(keys_dir, key.name)
      shutil.copy(key.absolute(), key_destination)


  def get_workshop_dir(self) -> str:
    return os.path.join(self.destination_dir, 'steamapps', 'workshop', 'content', Updater.GAME_APP_ID)

  def get_mod_dir(self, mod_id: str) -> str:
    return os.path.join(self.get_workshop_dir(), mod_id)
  
  def get_keys_dir(self) -> str:
    return os.path.join(self.destination_dir, 'keys')

  @staticmethod
  def symlink_exists(symlink: str) -> bool:
    path = Path(symlink)
    return path.exists() or path.is_symlink()

  @staticmethod
  def create_symlink(source: str, target: str) -> None:
    if os.name == 'nt':
      import _winapi
      _winapi.CreateJunction(source, target)
    else:
      os.symlink(source, target, target_is_directory=True)

