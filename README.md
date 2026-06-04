# Mobile Legends Organized Lane Decision Structure (MOLDS)

A counter hero engine built with Python that equips the user with knowledge on how to face the opponent with counter picking, proper itemization, and laning strategies for laning matchups and how to gain an upper hand as early as the drafting phase.

This system was designed initially for personal use for the structure of counter picking and the hero the author will face. This can be used for live drafting phases for quick summary on how to face the possible opponents. For now, the engine looks for EXP matchups for my personal use and can be upgraded by the community in the future, should it be deemed useful.

---

## Features

- **Smart Typo Auto-Correction (Fuzzy Matching):** Integrates Python's native difflib engine to process misspelled user inputs and automatically correct with 60% similarity threshold.
- **Flexible Search Formatting (Input Normalization):** Implements additional correction for neutralizing added spaces and hyphen variances in memory, matching different punctuated names to their counterparts in the database.
- **Independent Data & Code Setup (Decoupled Architecture):** Separates the logic code from the structured hero database, allowing modifications and data changes to occur independently without modifying the production code.
- **Instant Search Performance (O(1) Capability):** Utilizes direct dictionary key mapping for quick, instant retrieval of target data that are verified, ensuring immediate feedback regardless of database size.
- **Crash‑Proof File Handling (Defensive I/O Streams):** Usage of open() to track file handling and prevent system crashes if the core data source is missing or structurally compromised.

---

## Technologies

- **Language:** Python 3.13+
- **Data Format:** JSON (JavaScript Object Notation) for serialized data modeling
- **Fuzzy Engine:** Python Standard `difflib`
- **File Management:** Python Native File System Operations

---

## How to use

1. Enter the hero of your opponent in EXP. Make sure the spelling is right or nearly right so the engine recognizes it in the database.
2. The engine then shows a summary of the opponent hero's weakness, your counter picks and itemization, and your opponent hero's gameplay so you could counter its basic combos.
3. If the hero is not in the database, the hero must be rarely used on the only available lane (EXP), for now or the database hasn't been updated yet recently.

---

## Directory

```
├── exp_counter.py     # Main application and engine logic
├── exp_heroes.json    # Database for hero gameplay and parameters
└── README.md          # Project documentation
```
