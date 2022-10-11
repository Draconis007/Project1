import os
from tkinter import *
from PIL import ImageTk, Image
from random import *

root = Tk()
root.title('Energizer Randomizer')
root.geometry("900x700")


# Creating the Brand functions
def brand():
    # Hides previous frames
    hide_all_frames()
    brand_frame.pack(fill="both",expand=1)
    #my_label = Label(brand_frame, text="Brands").pack()
    #Creating a List of Brand Names
    our_brands = ['bang', 'reign', 'bawls', 'monster', 'gfuel', 'redbull', 'coffee']
    
#Generating a rando number
    rando = randint(0, len(our_brands)-1)
    brandimg = "pictures/" + our_brands[rando] + ".png"
#Creating Brand Images
    global brand_image
    brand_image = ImageTk.PhotoImage(Image.open(brandimg))
    show_brand = Label(brand_frame, image=brand_image)
    show_brand.pack(pady=15)
    
#Creating ze button fer da randomizer of brand
    rando_button = Button(brand_frame, text="Randomize!", command=brand)
    rando_button.pack(pady=10)
    
# Create Nutritional Facts functions (This is to show there is another window for future editing/maintenance)
def NFacts():
    # Hides previous frames
    hide_all_frames()
    NFacts_frame.pack(fill="both", expand=1)
    my_label = Label(NFacts_frame, text="Nutritional Facts").pack()
 
        
# Hiding the previous frames
def hide_all_frames():
    #Loop thru all children and destroys them in prior frames
    for widget in brand_frame.winfo_children():
        widget.destroy()
        
    for widget in NFacts_frame.winfo_children():
        widget.destroy()
        
    brand_frame.pack_forget()
    NFacts_frame.pack_forget()


# Create our menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create main menu items
drinks_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=drinks_menu)
drinks_menu.add_command(label="Brand Names", command=brand)
#drinks_menu.add_command(label="Nutritional Facts", command=NFacts)
#drinks_menu.add_separator()
drinks_menu.add_command(label="Exit", command=root.quit)



#Creating the frames
brand_frame = Frame(root, width=500, height=500)
NFacts_frame = Frame(root, width=500, height=500)



root.mainloop()

