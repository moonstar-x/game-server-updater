import time
import dumb_menu
from datetime import timedelta
from lib.config import load_config
from modules import update_server, update_all_servers


CONFIG_FILE = 'config.yml'
OPTIONS = {
  'Update All Game Servers': update_all_servers.run,
  'Update Single Game Server': update_server.run
}


def main():
  config = load_config(CONFIG_FILE)
  
  index_chosen = dumb_menu.get_menu_choice(OPTIONS.keys())
  chosen_fn = list(OPTIONS.values())[index_chosen]

  start_time = time.monotonic()
  chosen_fn(config)
  end_time = time.monotonic()

  delta = timedelta(seconds=end_time - start_time)
  print(f'Done! Execution took: {delta}')


if __name__ == '__main__':
  main()
