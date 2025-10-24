# -*- coding: utf-8 -*-
"""
Password Validator - Incremental versions (TDD)
Each version accumulates previous validation rules.
"""

import re


def validate_password_v1(password: str) -> dict:
    """Version 1 — At least 8 characters."""
    errors = []
    if len(password) < 8:
        errors.append("La contraseña debe tener al menos 8 caracteres")
    return {"is_valid": len(errors) == 0, "errors": errors}


def validate_password_v2(password: str) -> dict:
    """Version 2 — Also must contain at least two numbers."""
    errors = []
    if len(password) < 8:
        errors.append("La contraseña debe tener al menos 8 caracteres")

    digits = sum(ch.isdigit() for ch in password)
    if digits < 2:
        errors.append("La contraseña debe contener al menos dos números")

    return {"is_valid": len(errors) == 0, "errors": errors}


def validate_password_v3(password: str) -> dict:
    """Version 3 — Multiple errors handled together."""
    errors = []
    if len(password) < 8:
        errors.append("La contraseña debe tener al menos 8 caracteres")

    digits = sum(ch.isdigit() for ch in password)
    if digits < 2:
        errors.append("La contraseña debe contener al menos dos números")

    return {"is_valid": len(errors) == 0, "errors": errors}


def validate_password_v4(password: str) -> dict:
    """Version 4 — Must contain at least one uppercase letter."""
    errors = []
    if len(password) < 8:
        errors.append("La contraseña debe tener al menos 8 caracteres")

    digits = sum(ch.isdigit() for ch in password)
    if digits < 2:
        errors.append("La contraseña debe contener al menos dos números")

    if not any(ch.isupper() for ch in password):
        errors.append("La contraseña debe contener al menos una letra mayúscula")

    return {"is_valid": len(errors) == 0, "errors": errors}


def validate_password_v5(password: str) -> dict:
    """Version 5 — Must contain at least one special character."""
    errors = []
    if len(password) < 8:
        errors.append("La contraseña debe tener al menos 8 caracteres")

    digits = sum(ch.isdigit() for ch in password)
    if digits < 2:
        errors.append("La contraseña debe contener al menos dos números")

    if not any(ch.isupper() for ch in password):
        errors.append("La contraseña debe contener al menos una letra mayúscula")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("La contraseña debe contener al menos un carácter especial")

    return {"is_valid": len(errors) == 0, "errors": errors}
