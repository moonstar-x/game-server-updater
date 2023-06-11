# Game Server Updater

This small script can be used to install game servers from [SteamCMD](https://developer.valvesoftware.com/wiki/SteamCMD).

## Installation

Clone this repository:

```text
git clone https://github.com/moonstar-x/game-server-updater
```

And create a virtual environment:

```text
python -m venv ./venv
```

Then, activate it with:

```text
source ./venv/bin/activate
```

Or, on Windows:

```text
./venv/Scripts/activate.bat
```

Finally, install the dependencies:

```text
pip install -r requirements.txt
```

## Usage

First, rename the `config.sample.yml` file to `config.yml` and edit it accordingly.

You can run the script by running:

```text
python main.py
```

Or, if you're on Windows, you can use the `run.bat` script to run this with the appropriate environment.

## Adding New Configurations

To add a new configuration for a specific server, you should create a python file inside the `lib/servers` folder and export a class named `Updater` that inherits from `lib.steamcmd.GameServerUpdater`.

This created class should receive a `config: lib.config.Config` parameter and should call the parent class constructor with this config object, a pretty name that describes the name of the game server and the folder name where the game server data will be installed. Then, your class should implement the abstract `create_args() -> List[str]` method and return a list of the arguments passed to SteamCMD.

You can check the current implementations to guide yourself in the creation of this updater class.

That's it. The presence of the file in this folder will be enough for the script to recognize it as an option when running it.

## Author

This script was made by [moonstar-x](https://github.com/moonstar-x). 
