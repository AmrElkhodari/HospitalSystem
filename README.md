# 🏥 Hospital Queue Management System

A Python command-line application for managing patient queues across multiple hospital specializations, with priority-based ordering (Normal, Urgent, Super Urgent).

---

## 📋 Features

- **20 specializations** (e.g. Children, Surgery, Cardiology, etc.)
- **Priority queue** per specialization — Super Urgent → Urgent → Normal
- **10-patient capacity** per specialization
- Add, view, serve, and remove patients through an interactive menu

---

## 🗂️ Project Structure

```
hospital-system/
│
├── main.py      # Entry point — program loop and menu handling
├── core.py      # Hospital class with all queue logic
└── ui.py        # User input and display functions
```

---

## ▶️ How to Run

**Requirements:** Python 3.10+

```bash
python main.py
```

No external libraries needed — pure Python standard library.

---

## 📖 Usage Guide

The program loops a 5-option menu: **Add patient / Print all / Get next / Remove leaving / Exit.**

### Add a New Patient

Prompted for specialization (1–20), name, and status:

| Status Code | Meaning      | Queue Position                             |
|:-----------:|:-------------|:-------------------------------------------|
| `0`         | Normal       | Added to the end of the queue              |
| `1`         | Urgent       | Added after existing urgents, before normals |
| `2`         | Super Urgent | Added after existing super-urgents, first in line |

> If the specialization already has 10 patients, the system will decline the addition.

### Print / Get Next / Remove

- **Print all** — lists every occupied specialization in Super Urgent → Urgent → Normal order.
- **Get next** — serves and removes the highest-priority patient for a given specialization; informs the doctor if the queue is empty.
- **Remove leaving** — removes a patient by name before they're seen; reports if the name isn't found.

---

## ⚙️ Core Logic — `Hospital` Class

| Method | Parameters | Returns | Description |
|:---|:---|:---|:---|
| `add_patient` | `name: str, status: int, specialization_number: int` | `bool` | Adds patient; `False` if specialization is full |
| `retrieve_all_patients` | — | `str` | Formatted list of all patients by specialization |
| `get_next_patient` | `specialization_number: int` | `str \| None` | Serves the highest-priority patient; `None` if empty |
| `remove_leaving_patient` | `name: str, specialization_number: int` | `bool` | Removes named patient; `False` if not found |

> **Note:** `specialization_number` in the `Hospital` class is **0-indexed** (0–19). `ui.py` handles the conversion from user-facing 1-based input.

---

## 🏗️ Internal Data Structure

The hospital data is stored as a list of 20 specializations, each containing 3 sub-lists:

```
patients[specialization_index][priority_level]

priority_level:
  0 → Normal
  1 → Urgent
  2 → Super Urgent
```

Patients within the same priority level are served in **FIFO** (first-in, first-out) order.

---

## 👨‍💻 Author

Project developed as part of a Python Programming course by **Mostafa S. Ibrahim**.
