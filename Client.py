from concurrent import futures
import threading
import grpc
import tkinter as tk

import Client_pb2
import Client_pb2_grpc
import NameServer_pb2
import NameServer_pb2_grpc
import MessageBroker_pb2
import MessageBroker_pb2_grpc

from ClientPrivateChat import private_chat

class ChatServiceServicer(Client_pb2_grpc.ChatServiceServicer):
    def SendPrivateMessage(self, request, context):
        private_chat.send_message(request)
        empty = Client_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return empty
    
    def RecievePrivateMessage(self, request, context):
        response = Client_pb2.Message()
        response = private_chat.recieve_message()
        display_message(response.content, False)
        empty = Client_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return empty

#Header that contains the logo and Username
def add_header(w):
    global logo
    global header_frame
    global logo_label
    header_frame = tk.Frame(w, bg="#222", width=w.winfo_width())
    header_frame.pack(fill=tk.X, padx=10, pady=10, anchor="nw")
    logo_label = tk.Label(header_frame, image=logo, bg="#222", padx=10, pady=10)
    logo_label.pack(side=tk.LEFT, anchor="nw")

#Takes the user to the login/register window
def switch_user():
    frame.pack(pady=10, anchor="n")
    hide_options()
    back_button.pack_forget()
    usr_label.pack_forget()

#Makes the Option buttons visible
def show_options():
    global connected
    for button in option_buttons:
        button.pack(pady=10)
    for button in chat_buttons:
        button.pack_forget()
    switch_user_button.pack(side="bottom", padx=10, pady=10)
    back_button.pack_forget()
    chat_frame.pack_forget()
    connect_gc_frame.pack_forget()
    subscribe_gc_frame.pack_forget()
    if connected:
        cli_server.stop(grace=None)
        connected = False


def hide_options():
    for button in option_buttons:
        button.pack_forget()    
    switch_user_button.pack_forget()
    back_button.pack(side="bottom", padx=10, pady=10)  # Mostrar el botón "Tirar hacia atrás"

# Function to display chat messages
def display_message(message, is_user, is_gc_msg=False):
    global username
    
    estimated_width = len(message) + 2
    estimated_height = int((len(message) // (chat_window.winfo_width() / 13)) % (chat_window.winfo_width() / 13)) + 1
    
    if(is_gc_msg):
        msg_info = message.split(":", 1)
        if(msg_info[0] == username): 
            is_user=True
            message = msg_info[1]
        else:
            estimated_height=estimated_height+1
            message = f"{msg_info[0]}:\n{msg_info[1]}"
        
    msg_color = "#777" if is_user else "#555"
    text_color = "white" if msg_color == "#555" else "black"
    side = 'e' if is_user else 'w'
    
    new_message = tk.Text(message_container, width=estimated_width, height=estimated_height, wrap=tk.WORD, bg=msg_color, fg=text_color, font=("Verdana", 13))
    new_message.insert(tk.INSERT, message)
    new_message.config(state=tk.DISABLED)
    new_message.pack(anchor=side, padx=5, pady=2)

def create_chat_window(chatter, isGroupChat=False):
    global chat_window
    chat_window = tk.Toplevel(window)
    chat_window.title(f'Guassap2.0 - Chat with {chatter}')
    chat_window.geometry("570x750+350+20")  # Width x height + X offset + Y offset
    chat_window.configure(bg="#333")
    add_header(chat_window)
    global usr_label
    usr_label = tk.Label(header_frame, text=chatter, bg="#222", fg="white", font=("Verdana", 15))
    usr_label.pack(anchor="n", pady=33)
        

    # Function to send message
    def send_message():
        global empty
        global username
        if(not isGroupChat):
            message = message_entry.get()
            empty = Client_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
            if message:
                display_message(message, True)
                message_entry.delete(0, tk.END)
                with grpc.insecure_channel(response.address) as channel:
                    stub = Client_pb2_grpc.ChatServiceStub(channel)
                    message = Client_pb2.Message(content=message)
                    stub.SendPrivateMessage(message)
                    stub.RecievePrivateMessage(empty)
            return
        message = message_entry.get()
        if message:
            display_message(message, True)
            message_entry.delete(0, tk.END)
            with grpc.insecure_channel('localhost:50050') as channel:
                stub = MessageBroker_pb2_grpc.MessageBrokerStub(channel)
                msg = MessageBroker_pb2.ChatMessage(content=message, sender=username, group_chat=chatter)
                stub.PublishMessageToGroupChat(msg)
                

    # Create chat history Text widget
    global message_container
    chat_history = tk.Frame(chat_window, bg="#333")
    chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    message_container = tk.Canvas(chat_history, bg="#333")
    message_container.pack(fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(message_container, orient=tk.VERTICAL, command=message_container.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    bottom_frame = tk.Frame(chat_window, bg="#444")
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

    # Message entry field
    global message_entry
    message_entry = tk.Entry(bottom_frame, bg="#777" ,font=("Verdana", 14))
    message_entry.pack(padx=20, pady=10, side=tk.LEFT, fill=tk.X, expand=True)
    
    send_button = tk.Button(bottom_frame, text="Send", font=("Verdana", 14), command=send_message, bg="#8FEAE7", activebackground="#3C8CAE")
    send_button.pack(padx=10, pady=10, side=tk.RIGHT)
    
    global username
    if(isGroupChat):
        with grpc.insecure_channel('localhost:50050') as channel:
            stub = MessageBroker_pb2_grpc.MessageBrokerStub(channel)
            gc_id = MessageBroker_pb2.ChatMessage(content='', sender=username, group_chat=chat_id.get())
            messages = stub.ConsumeMessagesFromGroupChat(gc_id)
            for msg in messages:
                msg_info = f"{msg.sender}:{msg.content}"
                display_message(msg_info, False, True)
    
    
def connect_Chat():
    hide_options()
    for button in chat_buttons:
        button.pack(padx=10, pady=10)
    
    
def connect_private_chat():
    global user_port
    global cli_server
    global connected
    cli_server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    Client_pb2_grpc.add_ChatServiceServicer_to_server(ChatServiceServicer(), cli_server)
    cli_server.add_insecure_port(f'localhost:{user_port}')
    cli_server.start()
    connected = True
    
    for button in chat_buttons:
        button.pack_forget()
    user_ID_label = tk.Label(chat_frame, text="Who do you want to chat with?", bg="#333", fg="white", font=("Verdana", 15))
    user_ID_label.grid(row=0, column=0, padx=10, pady=10)
    global user_id
    user_id = tk.Entry(chat_frame)
    user_id.grid(row=1, column=0, padx=10)
    chat_button = tk.Button(chat_frame, text="Connect", command=start_grpc_client, bg="#555", activebackground="#575")
    chat_button.grid(row=2, column=0, padx=10, pady=15)
    chat_frame.pack(padx=10, pady=10)
    
    
def start_grpc_client():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = NameServer_pb2_grpc.NameServerStub(channel)
        target = NameServer_pb2.UserAddress(username=user_id.get(), ip_address='localhost')
        global response
        response = stub.GetUserInfo(target)
        channel.close()
        if(response.address == 'None'):
            no_user_lbl = tk.Label(window, text=f'User {user_id.get()} does not exist', bg="#333", fg="white", font=("Verdana", 15))
            no_user_lbl.pack(pady=10, padx=10)
            no_user_lbl.after(1500, no_user_lbl.destroy)
            return
    try:
        with grpc.insecure_channel(response.address) as channel:
            stub = Client_pb2_grpc.ChatServiceStub(channel)
            message = Client_pb2.Message(content='testing connection')
            stub.SendPrivateMessage(message)
        print(f'Connecting with {user_id.get()} with address {response.address}')
        create_chat_window(user_id.get())
    except Exception as e:
        no_user_lbl = tk.Label(window, text=f'User {user_id.get()} is not connected', bg="#333", fg="white", font=("Verdana", 15))
        no_user_lbl.pack(pady=10, padx=10)
        no_user_lbl.after(1500, no_user_lbl.destroy)
        return

        
def connect_group_chat():
    for button in chat_buttons:
        button.pack_forget()
    gc_ID_label = tk.Label(connect_gc_frame, text="Which chat you want to connect to?", bg="#333", fg="white", font=("Verdana", 15))
    gc_ID_label.grid(row=0, column=0, padx=10, pady=10)
    global chat_id
    chat_id = tk.Entry(connect_gc_frame)
    chat_id.grid(row=1, column=0, padx=10)
    connect_button = tk.Button(connect_gc_frame, text="Connect", command=start_group_chat, bg="#555", activebackground="#575")
    connect_button.grid(row=2, column=0, padx=10, pady=15)
    connect_gc_frame.pack(padx=10, pady=10)
    
def start_group_chat():
    with grpc.insecure_channel('localhost:50050') as channel:
        stub = MessageBroker_pb2_grpc.MessageBrokerStub(channel)
        gc = MessageBroker_pb2.ChatMessage(content='check', sender=username, group_chat=chat_id.get())
        subscribed = MessageBroker_pb2.Subscription(subscribed='')
        subscribed = stub.SubscribeToGroupChat(gc)
    if(subscribed.subscribed == 'False'):
        gc_connection_refused_lbl = tk.Label(window, text=f'You can\'t connect to group chat {chat_id.get()} if you are not subscribed to it!', bg="#333", fg="white", font=("Verdana", 15))
        gc_connection_refused_lbl.pack(pady=10, padx=10)
        gc_connection_refused_lbl.after(1500, gc_connection_refused_lbl.destroy)
    else:
        create_chat_window(chat_id.get(), True)
    
def subscribe_GC():
    hide_options()
    
    for button in chat_buttons:
        button.pack_forget()
    gc_ID_label = tk.Label(subscribe_gc_frame, text="Which chat you want to subscribe to?", bg="#333", fg="white", font=("Verdana", 15))
    gc_ID_label.grid(row=0, column=0, padx=10, pady=10)
    global chat_id
    chat_id = tk.Entry(subscribe_gc_frame)
    chat_id.grid(row=1, column=0, padx=10)
    subscribe_button = tk.Button(subscribe_gc_frame, text="Subscribe", command=subscribe_to_gc, bg="#555", activebackground="#575")
    subscribe_button.grid(row=2, column=0, padx=10, pady=15)
    subscribe_gc_frame.pack(padx=10, pady=10)
    
def subscribe_to_gc():
    with grpc.insecure_channel('localhost:50050') as channel:
        stub = MessageBroker_pb2_grpc.MessageBrokerStub(channel)
        gc = MessageBroker_pb2.ChatMessage(content='', sender=username, group_chat=chat_id.get())
        stub.SubscribeToGroupChat(gc)
    sub_lbl = tk.Label(window, text=f'Subscribed to group chat {chat_id.get()}!', bg="#333", fg="white", font=("Verdana", 15))
    sub_lbl.pack(pady=10, padx=10)
    sub_lbl.after(1500, sub_lbl.destroy)
    
def discover_chats():
    hide_options()
    print("discover_chats()")
    
def access_insult_channel():
    hide_options()
    print("access_insult_channel()")








def start():
    #Create the window
    global connected
    connected = False
    global window
    window = tk.Tk()
    window.title("Guassap2.0")
    window.geometry("750x500+300+100")  # Width x height + X offset + Y offset
    window.configure(bg="#333")
    
    global logo
    logo = tk.PhotoImage(file="./Guassap2.0.png")
    logo = logo.subsample(8)
    
    add_header(window)
    
    
    def set_username_and_close():
        global username
        global user
        global user_port
        username = username_entry.get()
        
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = NameServer_pb2_grpc.NameServerStub(channel)
            user = NameServer_pb2.UserAddress(username=username, ip_address='localhost')
            response =  stub.RegisterUser(user)
            myself = NameServer_pb2.UserAddress(username=username, ip_address='localhost')
            my_info = stub.GetUserInfo(myself)
            user_port=my_info.address.split(":")[1]
            channel.close()
        if response.success:
            print("Usuari Registrat")
        else:
            print("Usuari Identificat")
        
        global usr_label
        usr_label = tk.Label(header_frame, text=username, bg="#222", fg="white", font=("Verdana", 15))
        usr_label.pack(anchor="ne", padx=10, pady=30)
        frame.pack_forget()
        show_options()
    
    global frame
    frame = tk.Frame(window, bg="#333")
    frame.pack(pady=10, anchor="n")
    
    username_label = tk.Label(frame, text="Enter Username:", bg="#333", fg="white", font=("Verdana", 15))
    username_label.grid(row=0, column=0, padx=10, pady=10)
    username_entry = tk.Entry(frame)
    username_entry.grid(row=1, column=0, padx=10)
    username_button = tk.Button(frame, text="Login/Register", command=set_username_and_close, bg="#555", activebackground="#575")
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
    global subscribe_gc_frame
    global connect_gc_frame
    chat_frame = tk.Frame(window, bg="#333")
    subscribe_gc_frame = tk.Frame(window, bg="#333")
    connect_gc_frame = tk.Frame(window, bg="#333")
    
    global back_button 
    back_button = tk.Button(window, text="Back to Menu", command=show_options,
                            font=("Arial", 12), width=15, padx=10, pady=10, bg="#777", activebackground="#575")
    
    global switch_user_button 
    switch_user_button = tk.Button(window, text="Switch User", command=switch_user,
                            font=("Arial", 12), width=15, padx=10, pady=10, bg="#777", activebackground="#575")

    window.mainloop()

start()