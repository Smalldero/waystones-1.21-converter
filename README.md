# waystones-1.21-converter

This is a small tool to convert the `waystones.dat` from the 1.20.1 (and maybe some other versions) Minecraft Mod [Waystones](https://github.com/TwelveIterationMods/Waystones) to 1.21.
This should fix [issue 851](https://github.com/TwelveIterationMods/Waystones/issues/851)

## Usage

**IMPORTANT**
The converter only works on the waystone file before the savegame was used in the newer version! In the new version the important data gets overwritten so the converter wont work anymore. So make sure to use a savefile where everything was still working.

- Download one of the releases for your platform
- Create a backup of your `waystones.dat`! (`yourSavegameFolder/data/waystones.dat`)
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
- To build the executable run `pyinstaller --onefile --windowed convert-waystones-1.21.py` on each platform
- On mac you can also build the linux version with `pyinstaller --onefile --distpath dist/linux --workpath build/linux --specpath spec/linux convert-waystones-1.21.py`

