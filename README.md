<picture>
  <img alt="bank application icon" src="images/icons/smartbank_icon.png">
</picture>

# Smart Banking Services

## A Bank Graphical User Interface project based on Python Tkinter library

### Overview

This project is a comprehensive banking application designed to provide a secure and user-friendly banking experience. It integrates various functionalities, including GUI interfaces, RFID technology for secure authentication/identification, and email notifications.

### Objective

The main objective of this project is to develop a secure and user-friendly banking application that incorporates RFID technology for user authentication, a graphical user interface (GUI) for various banking operations, and automated email notifications via SMTP. Additionally, the project employs SQLite for efficient database management.

This project aims to:

- Teach the basics of GUI design using Tkinter.
- Demonstrate database management with SQLite.
- Explore secure user authentication through RFID technology.
- Implement automated email notifications using SMTP.

This project is intended for educational purposes only and is not a fully-fledged industry-ready banking application. It provides basic functionalities compared to modern banking solutions and serves as an introductory platform for beginner developers/programmers to learn about these technologies.

### Description

This multi-functional banking application leverages advanced technologies to offer an efficient and secure banking experience. The application combines RFID technology for secure user authentication, Tkinter for a graphical user interface, SQLite for database management, and SMTP for sending email notifications. The system aims to simplify and secure personal and small business banking operations.

### Functionalities

1.  **User Authentication via RFID and Security Pin:**

    - Utilizes RFID cards or tags for user authentication.
    - Reads the RFID tag’s unique ID to identify which bank account belongs to the user.
    - Ensures secure access to authorized users only.

2.  **Graphical User Interface (GUI):**

    - Developed using Python's Tkinter library.
    - Main window provides navigation options for various banking operations.
    - Separate windows for each banking operation (e.g., account creation, account deletion, cash deposit, cash withdrawal, amount transfer, balance inquiry).

3.  **Banking Operations:**

    - Create Account: Allows users to create new bank accounts by entering necessary details into a form.
    - Delete Account: Enables users to delete existing bank accounts.
    - Deposit Money: Facilitates depositing money into a user's account.
    - Withdraw Money: Allows users to withdraw money from their account.
    - Transfer Money: Enables transferring money between different accounts.
    - Check Balance: Provides users with the current balance of their account.

4.  **Automated Email Notifications:**

    - Sends email notifications to users for important account activities.
    - Uses SMTP with OAuth2 for secure email transmission.
    - Keeps users informed about transactions, enhancing transparency and security.

5.  **Database Management with SQLite:**

    - Uses SQLite for storing and managing user account information and transaction details.
    - Ensures data is stored securely and can be easily queried for various operations.

### Technologies Used

- Python
- Tkinter (for GUI)
- RFID technology (for secure user authentication and identification)
- SQLite (for database management)
- SMTP with OAuth2 (for sending email notifications)

### Requirements

- Python 3.10.x or above
- Tkinter library
- SQLite
- Other required Python libraries (Can be installed using the provided scripts)
- Email account configured for SMTP with OAuth2
- Google Cloud Platform setup for Gmail API

### Hardware Requirements

- EM-18 RFID reader module and 125KHz RFID tags/cards
- USB to TTL/UART Adapter (FT232RL, CP2102, CH340G, etc.)

### Prerequisites

Before running the project, ensure you have the following installed and configured:

- Python 3.x: Install Python from the official website [here](https://www.python.org/downloads/).
- Tkinter: Usually comes with Python installations. If not, install it using pip install tk.
- SQLite: Comes with Python installations. No additional installation required.
- RFID Reader and Tags: Ensure you have compatible RFID hardware.
- Google Cloud Platform setup: Create a project on Google Cloud Platform and configure the Gmail API for email functionality. Steps given below.

#### Setting up Gmail API for SMTP

1. **Create a project in the Google Cloud Platform Console:**

   - Go to the [Google Cloud Platform Console](https://console.cloud.google.com).
   - Click on the project dropdown and select "New Project".
   - Enter a project name and click "Create".

2. **Enable the Gmail API:**

   - In the Google Cloud Platform Console, go to the "APIs & Services" > "Library".
   - Search for "Gmail API" and click on it.
   - Click "Enable".

3. **Set up the OAuth consent screen:**

   - Go to "APIs & Services" > "OAuth consent screen".
   - Choose "External" and click "Create".
   - Fill in the required information and save.

4. **Create OAuth 2.0 credentials:**

   - Go to "APIs & Services" > "Credentials".
   - Click "Create Credentials" and select "OAuth 2.0 Client IDs".
   - Choose "Desktop app" for the application type and click "Create".
   - Download the credentials JSON file and save it in your project directory as credentials.json.

### Project Setup

#### Hardware Connections

Connect the EM-18 RFID Module pins and USB to TTL Adapter pins according to the pin assignment below:

| USB to UART Adapter | EM-18 RFID Reader Module |
| ------------------: | ------------------------ |
|                  RX | TX                       |
|              VCC/5V | VCC/5V                   |
|                 GND | GND                      |

![RFID Reader Module Connection](/images/Hardware/rfid_hardware.jpg)

<details open>
<summary>Automatic Setup</summary>

1. **Clone the repository:**

```bash
git clone https://github.com/atechofficials/smart-banking-application.git
```

2. **Navigate to the project directory:**

```bash
cd smart-banking-application
```

<details open>
<summary>For Linux:</summary>
Run the setup_and_run.sh file to automatically create a Python virtual environment, install the required libraries, and launch the project.

```sh
chmod +x setup_and_run.sh
./setup_and_run.sh
```

</details>

<details>
<summary>For Windows:</summary>
Run the setup_and_run.bat file to automatically create a Python virtual environment, install the required libraries, and launch the project.

```batch
setup_and_run.bat
```

</details>
</details>

<details>
<summary>Manual Setup</summary>

1. **Clone the repository:**

```bash
git clone https://github.com/atechofficials/smart-banking-application.git
```

2. **Navigate to the project directory:**

```bash
cd smart-banking-application
```

3. **Create a virtual environment:**

```bash
python -m venv smartbankvenv
```

4. **Activate the virtual environment:**

<details open>
<summary>Linux:</summary>

```bash
source smartbankvenv/bin/activate
```

</details>

<details>
<summary>Windows:</summary>

```bash
.\smartbankvenv\Scripts\activate
```

</details>

5. **Install required Python packages:**

```bash
pip install -r requirements.txt
```

6. **Ensure the _credentials.json_ file is in the project directory.**

7. **Run the application:**

```bash
python bank_gui.py
```

</details>

### Usage

1. Launch the application: Start the application by running python bank_gui.py.

2. Navigate the GUI: Use the provided navigation options/menu buttons to perform various banking operations.

3. User Identification: Use the RFID tag/card to for user identification/bank account fetch in forms.

4. Email Notifications: Ensure your email is correctly configured to receive transaction notifications.

### Contributing

We welcome contributions to enhance this project! As an educational tool, it serves as a great starting point for developers to learn about GUI design, database management, secure authentication, and automated notifications.

**To contribute:**

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Open a Pull Request.

By contributing, you can help add new features, optimize existing code, and improve the overall functionality of the application.

### Learning Resources/References

**RFID Reader Module**

- https://electrosome.com/em-18-rfid-reader-raspberry-pi
- https://www.electronicshub.org/raspberry-pi-rfid-reader-interface
- https://embetronicx.com/tutorials/tech_devices/how-does-rfid-works

**Python Tkinter Library/Module (for GUI creation)**

- https://www.geeksforgeeks.org/how-to-install-tkinter-in-windows/
- https://realpython.com/python-gui-tkinter/
- https://www.geeksforgeeks.org/python-gui-tkinter/
- https://www.geeksforgeeks.org/how-to-resize-image-in-python-tkinter/
- https://www.tutorialspoint.com/how-to-resize-an-image-using-tkinter
- https://www.geeksforgeeks.org/python-pil-image-resize-method/
- https://www.geeksforgeeks.org/iconphoto-method-in-tkinter-python/
- https://www.geeksforgeeks.org/python-tkinter-messagebox-widget/
- https://docs.python.org/3/library/tkinter.messagebox.html
- https://www.geeksforgeeks.org/python-tkinter-entry-widget/
- https://www.geeksforgeeks.org/radiobutton-in-tkinter-python/
- https://www.tutorialspoint.com/how-to-clear-the-contents-of-a-tkinter-text-widget
- https://www.tutorialspoint.com/python/tk_text.htm
- https://www.geeksforgeeks.org/how-to-use-images-as-backgrounds-in-tkinter/
- https://www.tutorialspoint.com/how-to-create-a-hyperlink-with-a-label-in-tkinter
- https://www.tutorialspoint.com/python/tk_fonts.htm
- https://pythonhosted.org/pyserial/shortintro.html#opening-serial-ports

**Installing Required Python Libraries/Modules**

- pip install tk (Tkinter library to create GUI applications using Python)
- pip install pyserial (Python Serial Library for serial communication with RFID Reader Module)
- python3 -m pip install --upgrade Pillow (Pillow Library for image display in Python Tkinter GUI)
- pip install smtplib (to send email using SMTP in Python)
- pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client (Google authentication, OAuth2 libraries and other dependencies for secure email communication)

**Python SQLite Library/Module (for database)**

- https://www.geeksforgeeks.org/python-sqlite/

**Google OAuth2 Implementation for Python**

- https://github.com/googleapis/google-api-python-client/blob/main/docs/oauth.md

**Python Pickle Library/Module (for Serialization)**

- https://www.geeksforgeeks.org/understanding-python-pickling-example/
- https://realpython.com/python-pickle-module/

**Flow Chart Symbols**

- https://www.zenflowchart.com/flowchart-symbols

**Flow Chart Maker**

- draw.io (https://app.diagrams.net/)

### License

This project is licensed under the GNU GPLv3 License - see the [LICENSE](./LICENSE) file for details.
