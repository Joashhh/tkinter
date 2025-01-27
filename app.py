import tkinter

window = Tk()
window.geometry("420x420")
window.title("CCT)
window.config(background="#e0f9ff")
window.mainloop()
flag = "flag"
             
def confirm_action():
  messagebox.showinfo("Confirmed")

def flag_input():
  user_input = flag_textbox.get("1.0", tk.END).strip()
  if user_input:
    if user_input == flag:
      messagebox.showinfo("Flag", "Correct flag entered!")
    else:
      messagebox.showerror("Flag", "Incorrect flag. Try again.")
