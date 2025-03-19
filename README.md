# 🧮 Python Scientific Calculator

A fully-featured scientific calculator built with Python, offering both CLI and GUI interfaces.

![image](https://github.com/user-attachments/assets/e5aed7d9-c087-469b-acf7-02e71dc7c488)

## ✨ Features

- 🔢 Basic arithmetic operations (add, subtract, multiply, divide)
- 💾 Memory operations (store, recall, add, subtract, clear)
- 🧠 Last result tracking for chained operations
- 🌙 Dark theme with customizable UI
- ⌨️ Full keyboard support
- 📱 Responsive design

## 📋 Requirements

- Python 3.8+
- Tkinter (included in standard Python installation)

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/AlizayAyesha/python-calculator.git
cd python-calculator

# Install in development mode
pip install -e .
```

## 📖 Usage

### GUI Calculator

```bash
# Launch the graphical calculator
calcgui
```

### Command Line Calculator

```bash
# Launch the command line calculator
mycalc
```

### As a Python Module

```python
from calc import Calculator

# Create a calculator instance
calc = Calculator()

# Perform calculations
result = calc.add(5, 3)     # 8
result = calc.subtract(10, 4)  # 6
result = calc.multiply(2, 3)   # 6
```

## 🏗️ Project Structure

```

## 🧪 Testing

Run the test suite with:

```bash
# Run all tests
pytest
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👩‍💻 Author

Made with ❤️ by Alizay Ayesha
