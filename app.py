import threading
from time import sleep
from tkinter import *
from PIL import ImageTk, Image
from utils.chat import get_response, bot_name
from utils.variables import *
CD = Default_Color


class ChatApplication:
    Change_Name_Status = False
    Username = ""

    def __init__(self) -> None:
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("ChatBot Version 1.3 | Version Française")
        self.window.resizable(width=False, height=False)
        self.window.geometry("1000x800")
        # self.window.columnconfigure(0, weight=1)
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        if self.Username == "":
            self.Username = "You"

        # put image in a label and place label as background
        imgTemp = Image.open(".\images\BG03.png")
        img2 = imgTemp.resize((width, height))
        img = ImageTk.PhotoImage(img2)

        # Add image file
        # bg = PhotoImage(file="BG01.png")

        # Show image using label
        label_img01 = Label(self.window, image=img, width=width,
                            height=height, bd=0, relief='ridge')
        label_img01.place(x=0, y=0)
        label_img01.image = img

        # Top Image
        # first_img = Image.open(".\images\Robot01.png")
        # first_img = first_img.resize((width,200))
        # photoImg =  ImageTk.PhotoImage(first_img)
        Top_img = PhotoImage(file=".\images\BG02.png")
        Top_img01 = Label(self.window, image=Top_img,
                          width=600, height=200, anchor=N, bd=0)
        Top_img01.place(relheight=0.30, relwidth=0.630, rely=0, relx=0)
        Top_img01.image = Top_img

        Title_label = Label(self.window, width=width, bg=CD.BG_COLOR, fg=CD.TEXT_COLOR,
                            text="Bienvenue sur ChatBot !", font=CD.FONT_BOLD, pady=10)
        Title_label.place(relheight=0.05,
                          relwidth=1, rely=0.26, relx=0)
        # line = Label(self.window, width=450, bg=CD.BG_GRAY)
        # line.grid(row=3)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2,
                                bg="black", fg=CD.TEXT_COLOR, font=CD.FONT, padx=10, pady=10)
        self.text_widget.place(
            relheight=0.500, relwidth=0.970, rely=0.31, relx=0.003)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        scrollbar = Scrollbar(self.window)
        scrollbar.place(relheight=0.500, relx=0.975, rely=0.310)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label widget
        bottom_label = Label(self.window, bg="black", height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, borderwidth=10, bg="black",
                               fg=CD.TEXT_COLOR, font=("Times", 20), insertbackground="white")
        self.msg_entry.place(relwidth=0.74, relheight=0.06,
                             rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=CD.FONT_BOLD,
                             width=20, bg=CD.GREEN, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

        # Second Page ( Side Column instruction )

        # Title instructions
        head_label2 = Button(self.window, text="Possible Commandes", command=lambda: self.Show_Commands(None),
                             bg="black", fg="white", font=("Times", 20), padx=10, pady=10)
        head_label2.place(relx=0.630, rely=0)

        # WC = Window Commands Possibilities

    def Show_Commands(self, event):
        self.WindowCommand = Toplevel(self.window)
        self.WindowCommand.title("Liste de toutes les commandes possibles 🤖")
        self.WindowCommand.resizable(width=False, height=False)
        self.WindowCommand.geometry("700x500")
        self.WindowCommand.config(bg="black")

        # WC = Window Commands Possibilities
        WC_Title = Label(self.WindowCommand, text="Voici une liste de commandes possible à demander: ",
                         bg="black", fg="white", padx=10, pady=10, font=("Times", 17))
        WC_Title.grid(row=0, column=0)

        First_Command_label = Label(
            self.WindowCommand, text="- Changer votre nom en demandant ( change de nom ) à Skynet, par défault, votre nom est (You).", bg="black", fg="white", font=("Times", 12), padx=10, pady=10)
        First_Command_label.grid(row=1, column=0)

        Second_Command_label = Label(
            self.WindowCommand, text="- Nettoyer la fenêtre avec la commande ( clear ) ou ( cls )", bg="black", fg="white", font=("Times", 12), padx=10, pady=10)
        Second_Command_label.grid(row=2, column=0)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, self.Username)

    def _insert_message(self, msg, sender):
        if not msg:
            return

        def User_text():
            self.msg_entry.delete(0, END)
            msgp1 = f"{sender}"
            msg1 = f": {msg}\n\n"
            self.text_widget.tag_config('user', foreground=CD.ORANGE)
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msgp1, 'user')
            self.text_widget.insert(END, msg1)
            self.text_widget.configure(state=DISABLED)

        if self.Change_Name_Status:
            self.Username = msg
            User_text()
            msgp2 = f"{bot_name}"
            self.text_widget.tag_config('UsernameW', foreground=CD.MAGENTA)
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msgp2, 'SkyNet')
            self.text_widget.insert(END, ": Bienvenue")
            self.text_widget.insert(END, f" {self.Username} \n\n", 'UsernameW')
            self.text_widget.configure(state=DISABLED)
            self.text_widget.see(END)
            self.Change_Name_Status = False
            return

        def SkyNet_text():
            sleep(0.370)
            msgp2 = f"{bot_name}"
            msg2 = f": {get_response(msg)}\n\n"
            quitting = ": Bien sûr Patron, je ferme cette application sur le champ !"
            clearing = ": Sans problème, je nettoie la fenêtre immédiatement !"
            self.text_widget.tag_config('SkyNet', foreground=CD.GREEN)
            print(msg)
            if msg.lower() == "quit" or msg.lower() == "exit":
                self.text_widget.configure(state=NORMAL)
                self.text_widget.insert(END, msgp2, 'SkyNet')
                self.text_widget.insert(END, quitting)
                self.text_widget.configure(state=DISABLED)
                self.text_widget.see(END)
                sleep(2)
                self.window.quit()
            elif msg.lower() == "clear" or msg.lower() == "cls":
                self.text_widget.configure(state=NORMAL)
                self.text_widget.insert(END, msgp2, 'SkyNet')
                self.text_widget.insert(END, clearing)
                self.text_widget.see(END)
                sleep(1)
                self.text_widget.delete('1.0', END)
                self.text_widget.insert(
                    END, "Nettoiement de la fenêtre en cours...\n")
                sleep(2)
                self.text_widget.delete('1.0', END)
                self.text_widget.insert(END, msgp2, 'SkyNet')
                self.text_widget.insert(
                    END, ": Que puis-je faire d'autre pour vous aujourd'hui ?\n\n")
                self.text_widget.configure(state=DISABLED)
                self.text_widget.see(END)
            elif msg.lower() == "change mon nom" or msg.lower() == "change de nom":
                self.Change_Name_Status = True
            else:
                self.text_widget.configure(state=NORMAL)
                self.text_widget.insert(END, msgp2, 'SkyNet')
                self.text_widget.insert(END, msg2)
                self.text_widget.configure(state=DISABLED)
                self.text_widget.see(END)

            if self.Change_Name_Status:
                self.text_widget.configure(state=NORMAL)
                self.text_widget.insert(END, msgp2, 'SkyNet')
                self.text_widget.insert(
                    END, ': Quel nom voulez-vous afficher ?\n\n')
                self.text_widget.configure(state=DISABLED)

        User_text()
        threading.Thread(target=SkyNet_text).start()


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
