from .calculator import Calculator

__all__ = ['Calculator']

def main() -> None:
    print("Hello from calc!")

def mycalc() -> None:
    """Interactive calculator demo."""
    from difflib import get_close_matches
    
    calc = Calculator()
    print("Interactive Calculator Demo")
    print("=========================")
    print("Type 'help' for commands, 'exit' to quit")
    
    # Command aliases dictionary
    aliases = {
        'add': ['add', 'addition', 'plus', 'sum', '+'],
        'sub': ['sub', 'subtract', 'subtraction', 'substract', 'minus', 'difference', '-'],
        'mul': ['mul', 'multiply', 'multiplication', 'product', '*', 'times'],
        'div': ['div', 'divide', 'division', 'quotient', '/'],
        'sqrt': ['sqrt', 'squareroot', 'square_root', 'root'],
        'sin': ['sin', 'sine'],
        'cos': ['cos', 'cosine'],
        'tan': ['tan', 'tangent'],
        'log': ['log', 'log10', 'logarithm'],
        'ln': ['ln', 'natural_log', 'loge'],
        'fact': ['fact', 'factorial', '!'],
        'result': ['result', 'ans', 'answer'],
        'clear': ['clear', 'clr', 'reset'],
        'm+': ['m+', 'memory_add', 'memory+'],
        'm-': ['m-', 'memory_subtract', 'memory-'],
        'mr': ['mr', 'memory_recall', 'recall'],
        'mc': ['mc', 'memory_clear', 'clearmem'],
        'exit': ['exit', 'quit', 'bye', 'q'],
        'help': ['help', 'h', '?', 'commands']
    }
    
    # Flatten aliases for lookup
    command_map = {}
    for main_cmd, alias_list in aliases.items():
        for alias in alias_list:
            command_map[alias] = main_cmd
    
    # All valid commands
    all_commands = list(command_map.keys())
    
    while True:
        command_input = input("\nEnter command: ").strip().lower()
        
        # Split input into parts
        parts = command_input.split()
        if not parts:
            continue
            
        # Extract the command (first word)
        cmd = parts[0]
        
        # Look for exact match or suggest alternatives
        if cmd in command_map:
            main_cmd = command_map[cmd]
            
            if main_cmd == 'exit':
                break
            elif main_cmd == 'help':
                print("\nAvailable commands:")
                print("  add X Y    - Add two numbers (Example: add 5 3)")
                print("  sub X Y    - Subtract Y from X (Example: sub 10 4)")
                print("  mul X Y    - Multiply two numbers (Example: mul 3 4)")
                print("  div X Y    - Divide X by Y (Example: div 10 2)")
                print("  sqrt X     - Square root of X (Example: sqrt 9)")
                print("  sin X      - Sine of X (radians) (Example: sin 1.57)")
                print("  cos X      - Cosine of X (radians) (Example: cos 0)")
                print("  tan X      - Tangent of X (radians) (Example: tan 0.78)")
                print("  log X      - Log base 10 of X (Example: log 100)")
                print("  ln X       - Natural log of X (Example: ln 2.71)")
                print("  fact X     - Factorial of X (Example: fact 5)")
                print("  result     - Show current result")
                print("  clear      - Clear current result")
                print("  m+         - Add result to memory")
                print("  m-         - Subtract result from memory")
                print("  mr         - Recall memory")
                print("  mc         - Clear memory")
                print("  exit       - Exit the calculator")
                print("\nTIPS: Commands must follow the format shown above.")
                print("      For example, type 'sub 10 5' to subtract 5 from 10.")
                print("      The calculator recognizes many variations like 'subtract', 'plus', etc.")
            elif main_cmd == 'result':
                print(f"Current result: {calc.last_result}")
            elif main_cmd == 'clear':
                calc.clear()
                print(f"Result cleared: {calc.last_result}")
            elif main_cmd == 'm+':
                calc.memory_add()
                print(f"Added to memory: Memory = {calc.memory}")
            elif main_cmd == 'm-':
                calc.memory_subtract()
                print(f"Subtracted from memory: Memory = {calc.memory}")
            elif main_cmd == 'mr':
                print(f"Memory recall: {calc.memory_recall()}")
            elif main_cmd == 'mc':
                calc.memory_clear()
                print("Memory cleared")
            else:
                # Operations requiring arguments
                try:
                    if main_cmd in ['add', 'sub', 'mul', 'div']:
                        if len(parts) < 3:
                            print(f"Error: {main_cmd} requires two numbers")
                            print(f"Example: {main_cmd} 10 5")
                            continue
                            
                        a = float(parts[1])
                        b = float(parts[2])
                        
                        if main_cmd == 'add':
                            result = calc.add(a, b)
                            print(f"{a} + {b} = {result}")
                        elif main_cmd == 'sub':
                            result = calc.subtract(a, b)
                            print(f"{a} - {b} = {result}")
                        elif main_cmd == 'mul':
                            result = calc.multiply(a, b)
                            print(f"{a} * {b} = {result}")
                        elif main_cmd == 'div':
                            result = calc.divide(a, b)
                            print(f"{a} / {b} = {result}")
                    
                    elif main_cmd in ['sqrt', 'sin', 'cos', 'tan', 'log', 'ln', 'fact']:
                        if len(parts) < 2:
                            print(f"Error: {main_cmd} requires one number")
                            print(f"Example: {main_cmd} 10")
                            continue
                            
                        a = float(parts[1])
                        
                        if main_cmd == 'sqrt':
                            result = calc.square_root(a)
                            print(f"sqrt({a}) = {result}")
                        elif main_cmd == 'sin':
                            result = calc.sin(a)
                            print(f"sin({a}) = {result}")
                        elif main_cmd == 'cos':
                            result = calc.cos(a)
                            print(f"cos({a}) = {result}")
                        elif main_cmd == 'tan':
                            result = calc.tan(a)
                            print(f"tan({a}) = {result}")
                        elif main_cmd == 'log':
                            result = calc.log10(a)
                            print(f"log10({a}) = {result}")
                        elif main_cmd == 'ln':
                            result = calc.ln(a)
                            print(f"ln({a}) = {result}")
                        elif main_cmd == 'fact':
                            result = calc.factorial(int(a))
                            print(f"{int(a)}! = {result}")
                
                except ValueError as e:
                    print(f"Error: {e}")
                    print("Make sure you're using numbers for calculations.")
                    print(f"Example: '{main_cmd} 5 3' (not '{main_cmd} five three')")
                except ZeroDivisionError:
                    print("Error: Cannot divide by zero")
                except Exception as e:
                    print(f"Error: {e}")
        else:
            # Command not recognized - suggest alternatives
            suggestions = get_close_matches(cmd, all_commands, n=3, cutoff=0.6)
            
            if suggestions:
                print(f"Unknown command: '{cmd}'")
                print(f"Did you mean: {', '.join(suggestions)}?")
            else:
                print(f"Unknown command: '{cmd}'")
            
            print("Type 'help' to see all available commands")

def gui():
    """Launch the calculator GUI."""
    from .gui import run
    run()
