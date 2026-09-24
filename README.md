# Hospital Management System

A simple command-line **Hospital Management System** built with Python and Object-Oriented Programming (OOP).

This project demonstrates basic patient management using Python classes, inheritance, lists, and a menu-driven interface.

## Features

* Add new patients
* View all registered patients
* Remove patients by Patient ID
* Display patient information
* Medical fee tracking
* Menu-driven command-line interface
* Object-Oriented Programming implementation

## Technologies Used

* **Python 3**
* Object-Oriented Programming (OOP)
* Python Standard Library

No external packages are required.

## Project Structure

```text
Hospital-Management-System/
├── main.py
└── README.md
```

## OOP Design

The project uses three main classes.

### Person

The `Person` class stores common personal information:

* Name
* Age

It also provides the `show_info()` method.

### Patient

The `Patient` class inherits from `Person` and adds:

* Patient ID
* Disease
* Medical Fee

It overrides `show_info()` to display the complete patient information.

### Admin

The `Admin` class provides patient management operations:

* Add patient
* Remove patient

## How It Works

When the program starts, it displays a menu:

```text
1. Add Patient
2. Show All Patients
3. Remove Patient
4. Exit
```

### Add Patient

Select option `1` and enter:

```text
Patient Name
Patient Age
Patient ID
Disease
Medical Fee
```

The patient is then stored in the in-memory patient list.

### Show All Patients

Select option `2` to display information for all currently registered patients.

Example:

```text
--- Patient Info ---
Name: John Doe
Age: 35
Patient ID: 1001
Disease: Fever
Medical Fee: 500.0
```

### Remove Patient

Select option `3` and enter the Patient ID.

The matching patient is removed from the patient list.

### Exit

Select option `4` to close the program.

## Installation

Clone the repository:

```bash
git clone https://github.com/Naeeryasar/Hospital-Management-System.git
cd Hospital-Management-System
```

Check Python:

```bash
python --version
```

## Run the Program

```bash
python main.py
```

On some systems:

```bash
python3 main.py
```

## Data Storage

The current version stores patient records in a Python list while the program is running.

```python
Patients = []
```

This means the patient data is **not permanently saved**. All records are lost when the program exits.

## Current Limitations

This is a basic educational project. It currently does not include:

* Database storage
* User authentication
* Doctor management
* Appointment scheduling
* Room/bed management
* Prescription management
* Billing history
* Permanent patient records
* GUI or web interface

## Future Improvements

The system can be expanded with:

* MySQL or SQLite database
* Patient search
* Doctor management
* Appointment management
* Hospital departments
* Medicine and prescription management
* Billing and payment records
* User login and role management
* Graphical user interface
* Web-based hospital management system
* Patient report generation

## Learning Objectives

This project is useful for learning:

* Classes and objects
* Inheritance
* Method overriding
* Encapsulation
* Lists and data management
* User input
* Conditional statements
* Loops
* Basic CRUD-style operations

## Author

**Naeer Yasar**

GitHub: https://github.com/Naeeryasar

## Repository

https://github.com/Naeeryasar/Hospital-Management-System
