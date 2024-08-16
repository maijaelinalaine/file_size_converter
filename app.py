from tkinter import ttk
import tkinter as tk

symbols = ["KB", "MB", "GB", "TB"]

def convert():
    size_before = int(original_size_entry.get())
    size_after = 0

    symbol_original = symbols.index(original_size.get())
    symbol_conversion = symbols.index(converted_size.get())

    conversion_multiplier = symbol_conversion - symbol_original

    if conversion_multiplier > 0:
        size_after = size_before / (1024 ** conversion_multiplier)
    else:
        size_after = size_before * (1024 ** abs(conversion_multiplier))

    new_text="result: " + str(size_after)
    converted_result_label.config(text = new_text)

window = tk.Tk()
window.geometry("300x200")
window.title("file size converter")

original_size_entry_label = tk.Label(text="original file size")
original_size_entry_label.pack()

original_size_entry = tk.Entry(width=25)
original_size_entry.pack()

original_size_label = tk.Label(text="original file size symbol")
original_size_label.pack()

original_size = ttk.Combobox(
    state="readonly",
    values=symbols
)
original_size.pack()

convert_button = tk.Button(text="convert", command=convert)
convert_button.pack()

converted_size_label = tk.Label(text="converted file size symbol")
converted_size_label.pack()

converted_size = ttk.Combobox(
    state="readonly",
    values=symbols
)
converted_size.pack()

converted_result_label = tk.Label(window, text="result: ")
converted_result_label.pack()

window.mainloop()
