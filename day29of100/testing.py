import tkinter as tk

root = tk.Tk()

# Create a label with right-aligned text
label = tk.Label(root, text="Right-aligned text", justify='left')
label.pack()

# Create a text area with right-aligned text
text = tk.Text(root, width=30, height=10, wrap='word')
text.pack()
text.tag_configure('left', justify='left')
text.insert('1.0', 'Right-aligned text', 'left')

root.mainloop()
