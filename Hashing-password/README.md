# 🔐 Password Hash Generator

A simple yet powerful **command-line Python tool** that generates cryptographic hashes for passwords using widely used hashing algorithms such as **SHA256, SHA512, and MD5**.

This project demonstrates core concepts of **cryptography, CLI development, and Python standard libraries**.

---

## 🚀 Project Overview

The **Password Hash Generator** converts a plain text password into a secure hashed value using Python’s built-in `hashlib` library.

It supports multiple hashing algorithms and can be used either:

* Via command-line arguments
* Or interactive user input (fallback mode)

This makes it both **developer-friendly and beginner-friendly**.

---

## ⚙️ How It Works

1. User provides a password (via command line or input prompt).
2. User selects hashing algorithm (MD5 / SHA256 / SHA512).
3. Python’s `hashlib` processes the input.
4. The password is encoded and passed to the hashing function.
5. A fixed-length hexadecimal hash is generated as output.

👉 Hashing is a **one-way process**, meaning original password cannot be retrieved from the hash.

---

## ✨ Features

* 🔐 Supports multiple hashing algorithms

  * SHA256 (default)
  * SHA512
  * MD5
* 💻 Command-line interface (CLI)
* 🧠 Interactive fallback input system
* ⚡ Fast and lightweight execution
* 🔒 Secure one-way hashing mechanism
* 📦 Built using Python standard library only (no external dependencies)

---

## 🛠️ Technologies Used

* Python 3
* hashlib
* argparse
* sys (for CLI handling)

---

## 📂 Project Structure

```text id="hashproj01"
Hashing-password/
│
├── main.py
└── README.md
```

---

## ▶️ How to Run

### 🔹 Method 1: Direct Run

```bash id="run01"
python main.py
```

Then enter password manually when prompted.

---

### 🔹 Method 2: Command Line Arguments

```bash id="run02"
python main.py mypassword -t sha256
```

Other options:

```bash
python main.py mypassword -t md5
python main.py mypassword -t sha512
```

---

## 💡 Example Output

```text id="out01"
==============================
 Hash Generator
==============================
Type   : sha256
Input  : mypassword
Output : 34819d7beeabb9260a5c854bc85b3e44...
==============================
```

---

## 🔍 Key Concepts Covered

This project helps understand:

* Cryptographic hashing
* One-way encryption principles
* Command-line argument parsing
* Python standard library usage
* Secure data transformation

---

## ⚠️ Important Note

* MD5 is considered **cryptographically weak** and should not be used for secure password storage in real-world applications.
* This project is created for **educational purposes only**.

---

## 📈 Future Improvements

* 🔑 Add salted hashing for better security
* 🧾 File hashing support
* 🖥️ GUI version using Tkinter
* 🔐 Password strength checker
* 📊 Hash comparison tool

---

## 👨‍💻 Author

Developed as a Python mini-project to demonstrate understanding of:

* Cryptography basics
* CLI tool development
* Secure hashing concepts

---

## 📜 License

This project is open-source and available under the MIT License.

---

⭐ If you like this project, consider giving it a star on GitHub!
