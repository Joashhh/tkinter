from tkinter import *
import yaml

window = Tk()
window.geometry("420x420")
window.title("CCT")
window.config(background="#e0f9ff")
window.mainloop()

with open('idk.yaml', 'r') as file:
  app = yaml.safe_load(file)
  
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

Chapter = StringVar()
chapter_entry = ttk.Entry(mainframe, width=7, textvariable=chapter)
chapter_entry.grid(column=2, row=1, sticky=(W, E))

flag = "flag"
             
def confirm_action():
  messagebox.showinfo("Confirmed")

def flag_input():
  user_input = flag_textbox.get("1.0", tk.END).strip()
  if user_input:
    if user_input == flag: 
      flag_message.showinfo("Flag", "Correct flag entered!")
    else:
      flag_message.showerror("Flag", "Incorrect flag. Try again.")

def run_bash_command():
    try:
        bash_message = subprocess.run(['ls', '/nonexistent_directory'], capture_output=True, text=True)
        
        if bash_message.returncode != 0:  # If the command failed
            messagebox.showerror("Error", f"Command failed with error: {result.stderr}")
        else:
            messagebox.showinfo("Bash Output", result.stdout)
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")
