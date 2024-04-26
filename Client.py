import grpc, grpc_tools
import tkinter as tk

#Logo position and size
def add_logo(window):
    global logo
    logo = tk.PhotoImage(file="Guassap2.0.png")
    logo = logo.subsample(8)
    logo_label = tk.Label(window, image=logo, bg="#333")
    logo_label.pack(anchor="nw", padx=10, pady=10)

#Make the Option buttons visible
def show_options():
    for button in option_buttons:
        button.pack(pady=10)

def connect_Chat():
    print("connect_Chat()")
    
def subscribe_GC():
    print("subscribe_GC()")
    
def discover_chats():
    print("discover_chats()")
    
def access_insult_channel():
    print("access_insult_channel()")

def start():
    #Create the window
    window = tk.Tk()
    window.title("Guassap2.0")
    window.geometry("750x500+300+100")  # Width x height + X offset + Y offset
    window.configure(bg="#333")
    
    add_logo(window)
    
    def set_username_and_close():
        global username
        username = username_entry.get()
        frame.destroy()
        show_options()
    
    frame = tk.Frame(window, bg="#333")
    frame.pack(pady=10)
    
    username_label = tk.Label(frame, text="Enter Username:", bg="#333", fg="white", font=("Verdana", 15))
    username_label.grid(row=0, column=0, padx=10, pady=10)
    
    username_entry = tk.Entry(frame)
    username_entry.grid(row=1, column=0, padx=10)
    
    username_button = tk.Button(frame, text="Login", command=set_username_and_close, bg="#555")
    username_button.grid(row=2, column=0, padx=10, pady=15)
    
    welcome_label = tk.Label(window, text="Welcome back {username}!", bg="#333", fg="white", font=("Verdana", 15))
    
    global option_buttons
    option_buttons = []
    button_names = ["Connect chat", "Subscribe to group chat", "Discover chats", "Access insult channel"]
    button_commands = ["connect_Chat()", "subscribe_GC()", "discover_chats()", "access_insult_channel()"]
    for i, name in enumerate(button_names):
        button = tk.Button(window, text=f"{name}", command=lambda i=i: eval(button_commands[i]), 
                           font=("Arial", 14), width=20, padx=10, pady=10, bg="#777", activebackground="#575")
        option_buttons.append(button)

    window.mainloop()


