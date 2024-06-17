# waystones-1.21-converter

This is a small tool to convert the `waystones.dat` from the 1.20 Minecraft Mod [Waystones](https://github.com/TwelveIterationMods/Waystones) to 1.21.
This should fix [issue 851](https://github.com/TwelveIterationMods/Waystones/issues/851)

## Usage

- Download one of the releases for your platform
- Create a backup of your `waystones.dat`!
- Run the executable
- Choose the filepath to the `waystones.dat` (`yourSavegameFolder/data/waystones.dat`)
- Wait for the process to finish
- Done

## Development

### Dependencies
- python3 with tkinter

### Setup
- Create a venv `python3 -m venv venv`
- Start venv `source venv/bin/activate`
- Install packages `pip install -r requirements.txt`
- Now you can edit the `convert-waystones-1.21.py` and test it with `python3 convert-waystones-1.21.py`

### Build
- To build the executable run `pyinstaller --onefile --windowed convert-waystones-1.21.py`
