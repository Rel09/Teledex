import tkinter as tk
from PIL import Image, ImageTk

teletubbies = [
    {
        "name": "Tinky Winky",
        "image_path": "tinky_winky.png",
        "description": "Tinky Winky is the first Teletubby. He is the tallest and often described as the leader of the group. He is purple and has a triangular antenna on his head."
    },
    {
        "name": "Dipsy",
        "image_path": "dipsy.png",
        "description": "Dipsy is the second Teletubby. He is green and wears a distinctive cowhide-patterned hat. He is laid-back, cool, and enjoys dancing."
    },
    {
        "name": "Laa-Laa",
        "image_path": "laa_laa.png",
        "description": "Laa-Laa is the third Teletubby. She is yellow and has a curly antenna. She loves to sing and dance, often carrying her orange ball with her."
    },
    {
        "name": "Po",
        "image_path": "po.png",
        "description": "Po is the fourth and smallest Teletubby. She is red and has a circular antenna on her head. She is energetic and enjoys riding her scooter."
    }
]

def display_teletubby(index):
    name_label.config(text=teletubbies[index]["name"])
    description_label.config(text=teletubbies[index]["description"])
    image = Image.open(f"img/{teletubbies[index]['image_path']}")
    image = image.resize((450, 500))
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.photo = photo

def on_next_button_click():
    global current_index
    current_index = (current_index + 1) % len(teletubbies)
    display_teletubby(current_index)

def on_prev_button_click():
    global current_index
    current_index = (current_index - 1) % len(teletubbies)
    display_teletubby(current_index)


if __name__ == "__main__":
    current_index = 0
    root = tk.Tk()
    root.title("Teledex")


    window_width = 1000
    window_height = 670
    root.geometry(f"{window_width}x{window_height}")
    root.resizable(width=False, height=False)

    left_frame = tk.Frame(root)
    left_frame.pack(side="left", padx=20, pady=20)

    name_label = tk.Label(left_frame, text="", font=("Arial", 16))
    name_label.pack(pady=10)

    image_label = tk.Label(left_frame)
    image_label.pack()

    button_frame = tk.Frame(left_frame)
    button_frame.pack(pady=20)

    prev_button = tk.Button(button_frame, text="Previous", command=on_prev_button_click)
    prev_button.pack(side="left", padx=10)

    next_button = tk.Button(button_frame, text="Next", command=on_next_button_click)
    next_button.pack(side="right", padx=10)

    description_label = tk.Label(root, text="", font=("Arial", 12), wraplength=400, justify="left")
    description_label.pack(side="left", padx=20, pady=20)

    display_teletubby(current_index)
    root.mainloop()
