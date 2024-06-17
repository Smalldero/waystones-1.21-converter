import nbtlib, tkinter, os, ctypes
from nbtlib import IntArray
from tkinter import filedialog, messagebox

# update BlockPos
def update_blockpos_tags(nbt_data):
    if isinstance(nbt_data, dict):
        for key, value in nbt_data.items():
            if key == 'BlockPos' and isinstance(value, dict):
                x = value.get('X')
                y = value.get('Y')
                z = value.get('Z')
                if x is not None and y is not None and z is not None:
                    nbt_data['BlockPos'] = IntArray([x, y, z])
            elif isinstance(value, dict) or isinstance(value, list):
                update_blockpos_tags(value)
    elif isinstance(nbt_data, list):
        for item in nbt_data:
            update_blockpos_tags(item)

# get file path and start update
def main():
    dialog = tkinter.Tk()
    dialog.withdraw()

    # activate high dpi
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass

    messagebox.showinfo("Info", "Make sure to create a backup of your waystones.dat before using this tool!")

    file_path = filedialog.askopenfilename(title="Select waystones.dat file", filetypes=[("DAT files", "*.dat")])

    if file_path:
        nbt_file = nbtlib.load(file_path)
        waystones_data = nbt_file['data']['Waystones']

        update_blockpos_tags(waystones_data)

        nbt_file.save()

        messagebox.showinfo("Success", "waystones.dat conversion to 1.21 done!")
    else:
        messagebox.showinfo("Info", "No file choosen - exiting")

# start the program
if __name__ == "__main__":
    main()
