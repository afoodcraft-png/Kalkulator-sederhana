import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    current_text = entry.get()
    
    if button_text == "=":
        try:
            math_expression = current_text.replace('x', '*')
            hasil = eval(math_expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(hasil))
        except ZeroDivisionError:
            messagebox.showerror("Error", "Lu dongo apa gimana? ga bisa bagi nol!")
            entry.delete(0, tk.END)
        except SyntaxError:
            messagebox.showerror("Error", "SMD rendah")
            entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Error ege: {e}")
            entry.delete(0, tk.END)
            
    elif button_text == "C":
        entry.delete(0, tk.END)
        
    else:
        entry.insert(tk.END, button_text)

# --- KONFIGURASI TEMA WARNA & FONT ---
BG_COLOR = "#000000"          
ENTRY_BG = "#303030"          
TEXT_COLOR = "#FFFFFF"       
NUM_BTN_COLOR = "#404040"    
OP_BTN_COLOR = "#FF9500"     
C_BTN_COLOR = "#FF3B30"      
FONT_DISPLAY = ("Arial", 36, "bold")
FONT_BUTTON = ("Arial", 16, "bold")

root = tk.Tk()
root.title("Kalkulator SDM Tinggi")
root.geometry("320x480")
root.resizable(False, False)
root.configure(bg=BG_COLOR) 

entry = tk.Entry(root, font=FONT_DISPLAY, borderwidth=0, relief="flat", 
                 justify='right', bg=ENTRY_BG, fg=TEXT_COLOR)
entry.grid(row=0, column=0, columnspan=4, padx=15, pady=25, ipady=15, sticky="nsew")

buttons = [
    ('C', 1, 0, 3), 
    ('/', 1, 3, 1),
    ('7', 2, 0, 1), ('8', 2, 1, 1), ('9', 2, 2, 1), ('x', 2, 3, 1),
    ('4', 3, 0, 1), ('5', 3, 1, 1), ('6', 3, 2, 1), ('-', 3, 3, 1),
    ('1', 4, 0, 1), ('2', 4, 1, 1), ('3', 4, 2, 1), ('+', 4, 3, 1),
    ('0', 5, 0, 2), ('.', 5, 2, 1), ('=', 5, 3, 1)
]

for (text, row, col, colspan) in buttons:
    action = lambda x=text: on_click(x)
    
    if text == 'C':
        btn_bg = C_BTN_COLOR
    elif text in ['/', 'x', '-', '+', '=']:
        btn_bg = OP_BTN_COLOR
    else:
        btn_bg = NUM_BTN_COLOR
        
    
    btn = tk.Button(root, text=text, font=FONT_BUTTON, relief="flat",
                    bg=btn_bg, fg=TEXT_COLOR, command=action,
                    activebackground="#505050", activeforeground=TEXT_COLOR) # Efek saat diklik
    
    btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()