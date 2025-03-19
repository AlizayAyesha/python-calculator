import tkinter as tk
from tkinter import ttk, messagebox
import math
from .calculator import Calculator

class CalculatorGUI:
    def __init__(self, root):
        self.calc = Calculator()
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # Setup dark theme
        self.root.configure(bg="#121212")
        
        # Configure styles for dark theme
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Base theme
        
        # Configure button styles
        self.style.configure("TButton", 
                            font=("Arial", 12),
                            background="#1E1E1E",
                            foreground="#FF4455")
        
        self.style.configure("Number.TButton", 
                            font=("Arial", 14, "bold"),
                            background="#1E1E1E",
                            foreground="#FF4455")
                            
        self.style.configure("Op.TButton", 
                            font=("Arial", 14, "bold"),
                            background="#2A2A2A",
                            foreground="#FFAA00")
                            
        self.style.configure("Sci.TButton", 
                            font=("Arial", 12),
                            background="#2A2A2A",
                            foreground="#00CCFF")
                            
        self.style.configure("Mem.TButton", 
                            font=("Arial", 12),
                            background="#2A2A2A",
                            foreground="#AAFFAA")
                            
        self.style.map('TButton',
                      background=[('active', '#333333')],
                      foreground=[('active', '#FFFFFF')])
        
        # Current operation and operand
        self.current_input = ""
        self.operation_pending = False
        
        self._create_ui()
        
    def _create_ui(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg="#1A1A1A", pady=10)
        display_frame.pack(fill=tk.BOTH)
        
        # Display
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        display = tk.Entry(display_frame, textvariable=self.display_var, 
                          font=("Digital-7", 28), bd=5, relief=tk.SUNKEN, 
                          justify=tk.RIGHT, bg="#000000", fg="#FF4455",
                          insertbackground="#FF4455")
        display.pack(fill=tk.BOTH, padx=10, pady=5, ipady=10)
        
        # Main content frame with left (numbers) and right (scientific) sections
        content_frame = tk.Frame(self.root, bg="#121212")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left frame for numbers and basic operations
        left_frame = tk.Frame(content_frame, bg="#121212")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # Right frame for scientific operations
        right_frame = tk.Frame(content_frame, bg="#121212")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        # Configure grid for both frames
        for i in range(5):
            left_frame.columnconfigure(i, weight=1)
            left_frame.rowconfigure(i, weight=1)
            
        for i in range(3):
            right_frame.columnconfigure(i, weight=1)
        for i in range(7):
            right_frame.rowconfigure(i, weight=1)
            
        # Memory status display
        self.memory_status = tk.Label(left_frame, text="Memory: 0", bg="#121212", 
                                    font=("Arial", 10), fg="#AAFFAA")
        self.memory_status.grid(row=0, column=0, columnspan=5, sticky="w", padx=5, pady=(0, 10))
        
        # Number buttons in left frame
        digits = [(7, 8, 9), (4, 5, 6), (1, 2, 3), (0, ".", "C")]
        for r, row_digits in enumerate(digits, 1):
            for c, digit in enumerate(row_digits):
                if digit == "C":
                    btn = ttk.Button(left_frame, text=digit, command=self._clear, style="Op.TButton")
                else:
                    btn = ttk.Button(left_frame, text=str(digit), 
                                   command=lambda d=digit: self._add_digit(d),
                                   style="Number.TButton")
                btn.grid(row=r, column=c, sticky="nsew", padx=4, pady=4)
        
        # Operator buttons 
        operators = [
            ("+", lambda: self._set_operation("add")),
            ("-", lambda: self._set_operation("sub")),
            ("×", lambda: self._set_operation("mul")),
            ("÷", lambda: self._set_operation("div")),
        ]
        
        for i, (text, cmd) in enumerate(operators):
            btn = ttk.Button(left_frame, text=text, command=cmd, style="Op.TButton")
            btn.grid(row=i+1, column=3, sticky="nsew", padx=4, pady=4)
        
        # Equal button and clear all button
        equals_btn = ttk.Button(left_frame, text="=", command=self._calculate, style="Op.TButton")
        equals_btn.grid(row=5, column=0, columnspan=3, sticky="nsew", padx=4, pady=4)
        
        allclear_btn = ttk.Button(left_frame, text="AC", command=self._all_clear, style="Op.TButton")
        allclear_btn.grid(row=5, column=3, sticky="nsew", padx=4, pady=4)
        
        # Scientific buttons in right frame
        sci_buttons = [
            ("sin", lambda: self._scientific_func(self.calc.sin)),
            ("cos", lambda: self._scientific_func(self.calc.cos)),
            ("tan", lambda: self._scientific_func(self.calc.tan)),
            ("log₁₀", lambda: self._scientific_func(self.calc.log10)),
            ("ln", lambda: self._scientific_func(self.calc.ln)),
            ("√x", lambda: self._scientific_func(self.calc.square_root)),
            ("n!", lambda: self._scientific_func(self.calc.factorial)),
            ("x²", lambda: self._set_operation("pow")),
            ("π", lambda: self._add_constant(math.pi)),
            ("e", lambda: self._add_constant(math.e)),
        ]
        
        # Title for scientific section
        sci_title = tk.Label(right_frame, text="Scientific Functions", bg="#121212", 
                           font=("Arial", 12, "bold"), fg="#00CCFF")
        sci_title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=(0, 10))
        
        # Add scientific buttons
        for i, (text, cmd) in enumerate(sci_buttons):
            row = (i // 2) + 1
            col = i % 2
            btn = ttk.Button(right_frame, text=text, command=cmd, style="Sci.TButton")
            btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)
        
        # Memory section title
        mem_title = tk.Label(right_frame, text="Memory Functions", bg="#121212", 
                           font=("Arial", 12, "bold"), fg="#AAFFAA")
        mem_title.grid(row=6, column=0, columnspan=2, sticky="w", padx=5, pady=(10, 5))
        
        # Memory buttons at the bottom of right panel
        memory_buttons = [
            ("MC", self._memory_clear),
            ("MR", self._memory_recall),
            ("MS", self._memory_store),
            ("M+", self._memory_add),
            ("M-", self._memory_subtract),
        ]
        
        for i, (text, cmd) in enumerate(memory_buttons):
            row = 7 + (i // 3)
            col = i % 3
            btn = ttk.Button(right_frame, text=text, command=cmd, style="Mem.TButton")
            btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)
            
        # Add footer separator
        separator = ttk.Separator(self.root, orient='horizontal')
        separator.pack(fill='x', pady=5)

        # Footer with attribution
        footer = tk.Label(self.root, text="Made by Alizay Ayesha", 
                         bg="#121212", fg="#FF88AA",
                         font=("Arial", 10, "italic"))
        footer.pack(pady=5)
            
        # Key bindings for keyboard input
        self.root.bind("<Key>", self._key_press)
    
    def _add_constant(self, value):
        """Add a mathematical constant like pi or e"""
        self.calc.add(0, value)
        if value == int(value):
            self.display_var.set(str(int(value)))
        else:
            self.display_var.set(str(value))
        self.current_input = ""
        self.operation_pending = True
    
    def _add_digit(self, digit):
        if self.operation_pending:
            self.current_input = ""
            self.operation_pending = False
            
        self.current_input += str(digit)
        self.display_var.set(self.current_input)
        
    def _set_operation(self, op):
        # First store the current value
        if self.current_input:
            try:
                value = float(self.current_input)
                self.calc.add(value) if self.calc.last_result == 0 else self._calculate()
            except ValueError:
                pass
        
        self.current_operation = op
        self.operation_pending = True
        
    def _calculate(self):
        if not self.current_input and not self.operation_pending:
            return
            
        try:
            if self.current_input:
                value = float(self.current_input)
                
                if hasattr(self, 'current_operation'):
                    result = 0
                    if self.current_operation == "add":
                        result = self.calc.add(value)
                    elif self.current_operation == "sub":
                        result = self.calc.subtract(value)
                    elif self.current_operation == "mul":
                        result = self.calc.multiply(value)
                    elif self.current_operation == "div":
                        result = self.calc.divide(value)
                    elif self.current_operation == "pow":
                        result = self.calc.power(value)
                else:
                    # If no operation yet, just set the value
                    result = self.calc.add(0, value)
                    
                # Format result
                if result == int(result):
                    self.display_var.set(str(int(result)))
                else:
                    self.display_var.set(str(result))
                    
                self.current_input = ""
                self.operation_pending = True
                
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            self._all_clear()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self._all_clear()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self._all_clear()
            
        # Update memory display
        self._update_memory_display()
            
    def _scientific_func(self, func):
        try:
            # If there's input, use that
            if self.current_input:
                value = float(self.current_input)
                self.calc.add(0, value)  # Set as current value
                
            # Apply function
            result = func()
            
            # Format result
            if result == int(result):
                self.display_var.set(str(int(result)))
            else:
                self.display_var.set(str(result))
                
            self.current_input = ""
            self.operation_pending = True
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
        # Update memory display
        self._update_memory_display()
            
    def _clear(self):
        self.current_input = ""
        self.display_var.set("0")
        
    def _all_clear(self):
        self.current_input = ""
        self.calc.clear()
        self.display_var.set("0")
        if hasattr(self, 'current_operation'):
            delattr(self, 'current_operation')
            
    def _memory_clear(self):
        self.calc.memory_clear()
        self._update_memory_display()
        
    def _memory_recall(self):
        value = self.calc.memory_recall()
        if value == int(value):
            self.display_var.set(str(int(value)))
        else:
            self.display_var.set(str(value))
        self.current_input = ""
        self._update_memory_display()
        
    def _memory_store(self):
        """Store current value in memory."""
        if self.current_input:
            try:
                value = float(self.current_input)
                self.calc.add(0, value)  # Set as current value before storing
            except ValueError:
                pass
            
        self.calc.memory_store()
        self._update_memory_display()
        
    def _memory_add(self):
        if self.current_input:
            try:
                value = float(self.current_input)
                self.calc.add(0, value)  # Set as current value before adding to memory
            except ValueError:
                pass
                
        self.calc.memory_add()
        self._update_memory_display()
        
    def _memory_subtract(self):
        if self.current_input:
            try:
                value = float(self.current_input)
                self.calc.add(0, value)  # Set as current value before subtracting from memory
            except ValueError:
                pass
                
        self.calc.memory_subtract()
        self._update_memory_display()
        
    def _update_memory_display(self):
        if self.calc.memory == int(self.calc.memory):
            self.memory_status.config(text=f"Memory: {int(self.calc.memory)}")
        else:
            self.memory_status.config(text=f"Memory: {self.calc.memory}")
    
    def _key_press(self, event):
        key = event.char
        
        # Handle digits and decimal
        if key.isdigit() or key == '.':
            self._add_digit(key)
        # Handle operations
        elif key == '+':
            self._set_operation("add")
        elif key == '-':
            self._set_operation("sub")
        elif key == '*':
            self._set_operation("mul")
        elif key == '/':
            self._set_operation("div")
        elif key == '^':
            self._set_operation("pow")
        # Handle equals and enter
        elif key == '=' or event.keysym == "Return":
            self._calculate()
        # Handle escape for clear
        elif event.keysym == "Escape":
            self._all_clear()
            
def run():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run() 