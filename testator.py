import tkinter
from tkinter import messagebox
import random
import string

window = tkinter.Tk()
window.title('Encrypter')
window.geometry('500x500')
window.configure(bg='#202020')
frame = tkinter.Frame(bg='#202020')

def genPassword(length):
    pwd = ""
    i = 0
    while i < int(length):
        pwd = pwd + random.choice(alphabet)
        i = i + 1
    return pwd
def vigenere(message, key, direction=1):
    key_index = 0
    encrypted_message = ''
    for char in message:
        key_char = key[key_index % len(key)]
        key_index += 1
        offset = alphabet.index(key_char)
        index = alphabet.find(char)
        new_index = (index + offset*direction) % len(alphabet)
        encrypted_message += alphabet[new_index]
    return encrypted_message
def decrypt():
    if decryptator_entry.get() != '' and keydetator_entry.get() != '':
        messagebox.showinfo(title='Decrypted message', message=f'Decrypted message : {vigenere(decryptator_entry.get(), keydetator_entry.get(), -1)}')
    else:
        messagebox.showerror(title='Error', message='Encrypted message or key invalid :(')
def encrypt():
    if encryptator_entry.get() != '' and keytator_entry.get() != '':
        passer =  genPassword(keytator_entry.get())
        messagebox.showinfo(title='Encrypted message', message=f'Encrypted message : {vigenere(encryptator_entry.get(), passer)}\nKey : {passer}')
    else:
        messagebox.showerror(title='Error', message='Message or key number invalid :(')

encrypt_title = tkinter.Label(frame, text='Encryption', bg='#202020', fg='red', font=('Constantia', 20))
decrypt_title = tkinter.Label(frame, text='Decryption', bg='#202020', fg='red', font=('Constantia', 20))
encryptator = tkinter.Label(frame, text='Message to encrypt : ', bg='#202020', fg='red', font=('Constantia', 12))
decryptator = tkinter.Label(frame, text='Message to decrypt : ', bg='#202020', fg='red', font=('Constantia', 12))
keytator = tkinter.Label(frame, text='Generate key : ', bg='#202020', fg='red', font=('Constatia', 12))
keydetator = tkinter.Label(frame, text='Key : ', bg='#202020', fg='red', font=('Constatia', 12))
encryptator_entry = tkinter.Entry(frame, bg='red', fg='#202020', font=('Constatia', 12))
decryptator_entry = tkinter.Entry(frame, bg='red', fg='#202020', font=('Constatia', 12))
keytator_entry = tkinter.Entry(frame, bg='red', fg='#202020', font=('Constatia', 12))
keydetator_entry = tkinter.Entry(frame, show='*', bg='red', fg='#202020', font=('Constatia', 12))
encryptator_button = tkinter.Button(frame, text='Encrypt', bg='red', fg='#202020', font=('Constantia', 12), command=encrypt)
decryptator_button = tkinter.Button(frame, text='Decrypt', bg='red', fg='#202020', font=('Constantia', 12), command=decrypt)
quit_program = tkinter.Button(frame, text='Quit', bg='red', fg='#202020', font=('Constantia', 12), command=exit)

#encrypt
encrypt_title.grid(row=0, column=0, columnspan=2, pady=20)
encryptator.grid(row=1, column=0)
keytator.grid(row=2, column=0)
encryptator_entry.grid(row=1, column=1)
keytator_entry.grid(row=2, column=1, pady=10)
encryptator_button.grid(row=2, column=2)
#decrypt
decrypt_title.grid(row=3, column=0, columnspan=2, pady=20)
keydetator.grid(row=5, column=0)
decryptator.grid(row=4, column=0)
decryptator_entry.grid(row=4, column=1, pady=10)
keydetator_entry.grid(row=5, column=1)
decryptator_button.grid(row=5, column=2)
#other
quit_program.grid(row=6, column=3, pady=30)

frame.pack()

alphabet = '    ' + ' ' + string.punctuation + string.ascii_letters + string.digits

window.mainloop()