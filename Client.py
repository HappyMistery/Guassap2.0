import grpc, grpc_tools
import tkinter as tk

import Client_pb2
import Client_pb2_grpc


#Logo position and size
def add_header(window):
    global logo
    logo = tk.PhotoImage(file="Guassap2.0.png")
    logo = logo.subsample(8)
    global header_frame
    header_frame = tk.Frame(window, bg="#222", width=window.winfo_width())
    header_frame.pack(fill=tk.X, padx=10, pady=10, anchor="nw")
    logo_label = tk.Label(header_frame if header_frame else window, image=logo, bg="#222", padx=10, pady=10)
    logo_label.pack(side=tk.LEFT, anchor="nw")

#Make the Option buttons visible
def show_options():
    for button in option_buttons:
        button.pack(pady=10)
    for button in chat_buttons:
        button.pack_forget()
    back_button.pack_forget()
    chat_frame.pack_forget()


def hide_options():
    for button in option_buttons:
        button.pack_forget()    
    back_button.pack(side="bottom", padx=10, pady=10)  # Mostrar el botón "Tirar hacia atrás"


    
def connect_Chat():
    hide_options()
    for button in chat_buttons:
        button.pack(padx=10, pady=10)
    
    
def connect_private_chat():
    for button in chat_buttons:
        button.pack_forget()
    chat_ID_label = tk.Label(chat_frame, text="Enter private chat ID:", bg="#333", fg="white", font=("Verdana", 15))
    chat_ID_label.grid(row=0, column=0, padx=10, pady=10)
    global chat_id
    chat_id = tk.Entry(chat_frame)
    chat_id.grid(row=1, column=0, padx=10)
    chat_button = tk.Button(chat_frame, text="Connect", command=start_grpc_client, bg="#555")
    chat_button.grid(row=2, column=0, padx=10, pady=15)
    chat_frame.pack(padx=10, pady=10)
    
def start_grpc_client():
    with grpc.insecure_channel('localhost:50051') as channel:
        # Crear un stub para el servicio ChatService
        stub = Client_pb2_grpc.ChatServiceStub(channel)
        request = Client_pb2.ChatId(chat_id)
        
def connect_group_chat():
    print("connect_group_chat()")
    
def subscribe_GC():
    hide_options()
    print("subscribe_GC()")
    
def discover_chats():
    hide_options()
    print("discover_chats()")
    
def access_insult_channel():
    hide_options()
    print("access_insult_channel()")

def start():
    #Create the window
    global window
    window = tk.Tk()
    window.title("Guassap2.0")
    window.geometry("750x500+300+100")  # Width x height + X offset + Y offset
    window.configure(bg="#333")
    
    add_header(window)
    
    def set_username_and_close():
        global username
        username = username_entry.get()
        usr_label = tk.Label(header_frame, text=username, bg="#222", fg="white", font=("Verdana", 15))
        usr_label.pack(anchor="ne", padx=10, pady=30)
        frame.destroy()
        show_options()
    
    frame = tk.Frame(window, bg="#333")
    frame.pack(pady=10, anchor="n")
    
    username_label = tk.Label(frame, text="Enter Username:", bg="#333", fg="white", font=("Verdana", 15))
    username_label.grid(row=0, column=0, padx=10, pady=10)
    username_entry = tk.Entry(frame)
    username_entry.grid(row=1, column=0, padx=10)
    username_button = tk.Button(frame, text="Login", command=set_username_and_close, bg="#555")
    username_button.grid(row=2, column=0, padx=10, pady=15)
    
    global option_buttons
    option_buttons = []
    button_names = ["Connect chat", "Subscribe to group chat", "Discover chats", "Access insult channel"]
    button_commands = ["connect_Chat()", "subscribe_GC()", "discover_chats()", "access_insult_channel()"]
    for i, name in enumerate(button_names):
        button = tk.Button(window, text=f"{name}", command=lambda i=i: eval(button_commands[i]), 
                           font=("Arial", 14), width=20, padx=10, pady=10, bg="#777", activebackground="#575")
        option_buttons.append(button)
    
    global chat_buttons
    chat_buttons = []
    private_chat = tk.Button(window, text="Private Chat", command=connect_private_chat, 
                           font=("Arial", 14), width=20, padx=10, pady=10, bg="#777", activebackground="#575")
    group_chat = tk.Button(window, text="Group Chat", command=connect_group_chat, 
                           font=("Arial", 14), width=20, padx=10, pady=10, bg="#777", activebackground="#575")
    chat_buttons.append(private_chat)
    chat_buttons.append(group_chat)
    
    global chat_frame
    chat_frame = tk.Frame(window, bg="#333")
    
    global back_button 
    back_button = tk.Button(window, text="Back to Menu", command=show_options,
                            font=("Arial", 12), width=15, padx=10, pady=10, bg="#777", activebackground="#575")

    window.mainloop()


