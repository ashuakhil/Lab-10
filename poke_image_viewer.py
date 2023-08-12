"""
Description:
  Graphical user interface that displays the official artwork for a
  user-specified Pokemon, which can be set as the desktop background image.

Usage:
  python poke_image_viewer.py
"""
from tkinter import *
from tkinter import ttk
from poke_api import get_pokemon_names, get_pokemon_artwork
from image_lib import download_image, save_image_file, set_desktop_background_image

# Create the main window
root = Tk()
root.title("Pokemon Viewer")

# Set the icon (replace 'icon.ico' with your actual icon file)
icon_path = 'icon.ico'
root.iconbitmap(icon_path)

# Create frames
frame1 = ttk.Frame(root)
frame2 = ttk.Frame(root)
frame3 = ttk.Frame(root)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)

# Create a Combobox with a list of Pokemon names
pokemon_names = get_pokemon_names()
selected_pokemon = StringVar()
pokemon_combobox = ttk.Combobox(frame1, textvariable=selected_pokemon, values=pokemon_names)
pokemon_combobox.set("Select a Pokemon")
pokemon_combobox.pack(side='left', padx=10, pady=10)

# Create a Label to display the Pokemon artwork
pokemon_artwork = PhotoImage()  # Placeholder for the image
artwork_label = ttk.Label(frame1, image=pokemon_artwork)
artwork_label.pack(side='left', padx=10, pady=10)

# Create a Button to set the desktop background image
def set_desktop_image():
    selected_name = selected_pokemon.get()
    if selected_name:
        image_data = get_pokemon_artwork(selected_name)
        if image_data:
            image_path = f'images/{selected_name}.png'
            save_image_file(image_data, image_path)
            set_desktop_background_image(image_path)

set_button = ttk.Button(frame2, text="Set as Desktop Image", command=set_desktop_image)
set_button.pack(side='bottom', padx=10, pady=10)

# Event handler for Combobox selection
def on_combobox_select(event):
    selected_name = selected_pokemon.get()
    if selected_name:
        image_data = get_pokemon_artwork(selected_name)
        if image_data:
            image_path = f'images/{selected_name}.png'
            save_image_file(image_data, image_path)
            artwork = PhotoImage(file=image_path)
            artwork_label.config(image=artwork)
            artwork_label.image = artwork  # Keep a reference to prevent garbage collection
            set_button.config(state='normal')
        else:
            set_button.config(state='disabled')
    else:
        set_button.config(state='disabled')

pokemon_combobox.bind("<<ComboboxSelected>>", on_combobox_select)

root.mainloop() 