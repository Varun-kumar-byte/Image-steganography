import cv2
import os
import tkinter as tk
from tkinter import filedialog

# Function to encrypt the message
def encrypt_message():
    global img_path  # Use the global img_path variable
    global img       # Use the global img variable
    global msg       # Use the global msg variable

    img_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    img = cv2.imread(img_path)

    msg = entry_msg.get()
    password = entry_password.get()

    d = {chr(i): i for i in range(255)}

    m = 0
    n = 0
    z = 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite("encrypted_image.png", img)

    os.system('start encrypted_image.png')

# Function to decrypt the message
def decrypt_message():
    global img_path  # Use the global img_path variable
    global img       # Use the global img variable
    global msg       # Use the global msg variable

    img_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    img = cv2.imread(img_path)

    decrypted_message = ""
    n = 0
    m = 0
    z = 0

    password = entry_password.get()
    pas = entry_passcode.get()

    if password == pas:
        for i in range(len(msg)):
            decrypted_message = decrypted_message + chr(img[n, m, z])
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        print("Decrypted Message:", decrypted_message)  # Print to console
        lbl_result.config(text=f"Decrypted Message: {decrypted_message}")
    else:
        lbl_result.config(text="Invalid Passcode")

# Create main window
root = tk.Tk()
root.title("Image Steganography")

# Declare global variables
img_path = ""
img = None
msg = ""

# Create widgets
label_msg = tk.Label(root, text="Enter secret message:")
entry_msg = tk.Entry(root)

label_password = tk.Label(root, text="Enter password:")
entry_password = tk.Entry(root, show="*")

btn_encrypt = tk.Button(root, text="Encrypt", command=encrypt_message)

label_passcode = tk.Label(root, text="Enter passcode for Decryption:")
entry_passcode = tk.Entry(root, show="*")

btn_decrypt = tk.Button(root, text="Decrypt", command=decrypt_message)

lbl_result = tk.Label(root, text="")

# Arrange widgets in grid
label_msg.grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_msg.grid(row=0, column=1, padx=5, pady=5)
label_password.grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_password.grid(row=1, column=1, padx=5, pady=5)
btn_encrypt.grid(row=2, column=0, columnspan=2, pady=10)
label_passcode.grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_passcode.grid(row=3, column=1, padx=5, pady=5)
btn_decrypt.grid(row=4, column=0, columnspan=2, pady=10)
lbl_result.grid(row=5, column=0, columnspan=2, pady=10)

# Run the Tkinter main loop
root.mainloop()
