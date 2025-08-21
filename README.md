# 🧪 Pytest Selenium Assignment: letskodeit.com Practice Page

Automated web testing assignment using **Python**, **Selenium**, and **Pytest**.  
You will learn how to interact with all major types of web elements (radio buttons, checkboxes, dropdowns, alerts, tables, iframes, and more) on [letskodeit.com Practice Page](https://www.letskodeit.com/practice) using different locator strategies.

---

## 📁 Project Structure
```
pytest_selenium_assignment/
├── tests/
│ └── test_practice_page.py # All test cases
├── conftest.py # Pytest setup/teardown for browser
├── requirements.txt # Project dependencies
└── README.md
```

---

## 🚀 Getting Started

1. Clone the Repository
```bash
git clone https://github.com/Abhay-Anand-INT/INT_Python_Selenium
cd INT_Python_Selenium
```
2. Install Dependencies
Make sure you have Python 3.x installed.
```bash
pip install -r requirements.txt
```
3. Download ChromeDriver
Download ChromeDriver that matches your browser.

```
Place it in your system PATH or specify its path in conftest.py.
```


## 📝 How to Run the Tests
Run all tests with:
```bash
pytest
```

Or run a specific test:
```bash
pytest tests/test_practice_page.py::test_radio_buttons
```

## 🧩 What’s Covered?
Each section of the Practice Page is automated: <br>
✅ Open and verify Practice Page title<br>
✅ Radio Button selection<br>
✅ Checkbox selection<br>
✅ Switch to new Window/Tab and back<br>
✅ Single and Multi-Select Dropdowns<br>
✅ Auto-suggest input and selection<br>
✅ Enable/Disable elements<br>
✅ Show/Hide elements<br>
✅ Alerts & Confirms (with text check)<br>
✅ Mouse Hover (showing menu)<br>
✅ Extract and check Web Table content<br>
✅ Interact with iFrames<br>

## 💡 Best Practices Demonstrated
- Using different locator strategies (ID, NAME, XPATH, CSS_SELECTOR)
- Pytest fixtures for setup/teardown (conftest.py)
- Writing independent, atomic test cases
- Assertions after each action

## ❓ Troubleshooting
Q.) WebDriver errors? <br>
A.) Ensure ChromeDriver matches your Chrome version and is in your PATH. <br>
<br>
Q.) Elements not interactable? <br>
A.) Some actions may require a brief time.sleep() or, ideally, explicit Selenium waits. <br> 

## 🙌 Credits
Practice page: letskodeit.com
