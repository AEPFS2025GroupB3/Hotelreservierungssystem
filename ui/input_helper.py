import sys
from enum import Enum


class YesOrNo(Enum):
    YES = 1
    NO = 0


class EmptyInputError(ValueError):
    """Custom exception for empty input."""
    pass


class OutOfRangeError(ValueError):
    """Custom exception for values outside the allowed range."""

    def __init__(self, value, min_value, max_value):
        super().__init__(f"Input {value} is out of range ({min_value} to {max_value}).")
        self.value = value
        self.min_value = min_value
        self.max_value = max_value


class StringLengthError(ValueError):
    """Custom exception for strings that are too short or too long."""

    def __init__(self, value, min_length, max_length):
        super().__init__(f"Input '{value}' must be between {min_length} and {max_length} characters long.")
        self.value = value
        self.min_length = min_length
        self.max_length = max_length


def input_valid_string(prompt: str, min_length: int = 0, max_length: int = sys.maxsize) -> str:
    """Gültige Texteingabe verlangen, mit Längenprüfung und Zahlen-Ausschluss."""
    while True:
        user_input = input(prompt).strip()

        if user_input == "":
            print("Eingabe darf nicht leer sein.")
            continue

        if user_input.isdigit():
            print("Bitte gib Text ein keine Zahl.")
            continue

        if not (min_length <= len(user_input) <= max_length):
            print(f"Eingabe muss zwischen {min_length} und {max_length} Zeichen lang sein.")
            continue

        return user_input



def input_valid_int(prompt: str, min_value: int = -sys.maxsize, max_value: int = sys.maxsize,
                    default: int = None) -> int:
    """Eingabe einer gültigen Ganzzahl mit Wiederholversuch bei Fehlern."""
    while True:
        user_input = input(prompt).strip()

        if user_input == "":
            if default is not None:
                return default
            else:
                print("Eingabe darf nicht leer sein.")
                continue

        try:
            value = int(user_input)
        except ValueError:
            print("Ungültige Eingabe! Bitte gib eine Zahl ein.")
            continue

        if value < min_value or value > max_value:
            print(f"Zahl muss zwischen {min_value} und {max_value} liegen.")
            continue

        return value



def input_valid_float(
        prompt: str,
        min_value: float = -float('inf'),
        max_value: float = float('inf'),
        default: float = None
) -> float:
    """Function to get a valid float within a range, raising specific exceptions."""
    user_input = input(prompt).strip()

    if user_input == "":
        if default is None:
            raise EmptyInputError("Input cannot be empty.")
        else:
            return default

    try:
        value = float(user_input)  # Versuch, die Eingabe in eine Fließkommazahl umzuwandeln
    except ValueError as err:
        raise ValueError("Invalid input. Please enter a valid float number.") from err  # Exception-Chaining

    if value < min_value or value > max_value:
        raise OutOfRangeError(value, min_value, max_value)  # Eigene Exception für Werte außerhalb des Bereichs

    return value  # Gültige Zahl zurückgeben


def input_y_n(prompt: str, default: YesOrNo = None) -> bool:
    """Ja/Nein-Eingabe mit Wiederholung bei ungültiger Eingabe"""
    y = ['y', 'yes']
    n = ['n', 'no']

    while True:
        user_input = input(prompt).strip().lower()

        if user_input in y:
            return True
        elif user_input in n:
            return False
        elif user_input == "" and default is not None:
            return bool(default.value)
        else:
            print("Ungültige Eingabe! Bitte geben Sie 'y' oder 'n' ein.")


# Für User Story 7

from datetime import datetime, date

def input_valid_date(prompt: str) -> date:
    """Function to get a valid date input in the format YYYY-MM-DD."""
    while True:
        user_input = input(prompt).strip()
        try:
            return datetime.strptime(user_input, "%Y-%m-%d").date()
        except ValueError:
            print("Ungültiges Datum. Bitte im Format YYYY-MM-DD eingeben.")

