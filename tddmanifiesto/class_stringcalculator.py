# -*- coding: utf-8 -*-
"""
String Calculator - Refactored for cumulative behavior.
Each version builds upon the previous ones.
"""


def add(numbers: str) -> int:
    """Version 1 — Up to two comma-separated numbers or empty string."""
    if numbers == "":
        return 0
    parts = numbers.split(",")
    if len(parts) == 1:
        return int(parts[0])
    return int(parts[0]) + int(parts[1])


def add_v2(numbers: str) -> int:
    """Version 2 — Handle unknown number of arguments."""
    if numbers == "":
        return 0
    parts = numbers.split(",")
    return sum(map(int, parts))


def add_v3(numbers: str) -> int:
    """Version 3 — Support commas and newlines."""
    if numbers == "":
        return 0
    parts = numbers.replace("\n", ",").split(",")
    return sum(map(int, parts))


def add_v4(numbers: str) -> int:
    """Version 4 — Validation: no separator at end."""
    if numbers == "":
        return 0
    if numbers.endswith(",") or numbers.endswith("\n"):
        raise ValueError("Invalid input: separator at the end")
    parts = numbers.replace("\n", ",").split(",")
    return sum(map(int, parts))


def add_v5(numbers: str) -> int:
    """Version 5 — Support custom delimiters."""
    if numbers == "":
        return 0

    delimiter = ","
    body = numbers

    # Detect custom delimiter
    if numbers.startswith("//"):
        header, body = numbers.split("\n", 1)
        delimiter = header[2:]

        # Validar que no termine con el delimitador custom
        if body.endswith(delimiter):
            raise ValueError("Invalid input: separator at the end")

        # Para custom delimiter, solo usar ese delimitador
        parts = body.split(delimiter)
    else:
        # Para delimitadores por defecto (coma y newline)
        if body.endswith(",") or body.endswith("\n"):
            raise ValueError("Invalid input: separator at the end")
        parts = body.replace("\n", ",").split(",")

    return sum(map(int, parts))


def add_v6(numbers: str) -> int:
    """Version 6 — Raise error if negative numbers are present."""
    if numbers == "":
        return 0

    delimiter = ","
    body = numbers

    if numbers.startswith("//"):
        header, body = numbers.split("\n", 1)
        delimiter = header[2:]

        if body.endswith(delimiter):
            raise ValueError("Invalid input: separator at the end")

        tokens = body.split(delimiter)
    else:
        if body.endswith(",") or body.endswith("\n"):
            raise ValueError("Invalid input: separator at the end")
        tokens = body.replace("\n", ",").split(",")

    nums = [int(t) for t in tokens if t.strip() != ""]

    negatives = [n for n in nums if n < 0]
    if negatives:
        raise ValueError(
            f"Negative numbers not allowed: {', '.join(map(str, negatives))}"
        )

    return sum(nums)


# pylint: disable=too-many-branches
def add_v7(numbers: str) -> int:
    """
    Version 7 — Aggregate multiple errors (negatives + mixed delimiters).
    """
    if numbers == "":
        return 0

    delimiter = ","
    body = numbers

    if numbers.startswith("//"):
        header, body = numbers.split("\n", 1)
        delimiter = header[2:]

    # Validar terminación con delimitador
    if body.endswith(delimiter) or (
        not numbers.startswith("//") and (body.endswith(",") or body.endswith("\n"))
    ):
        raise ValueError("Invalid input: separator at the end")

    # Detectar delimitadores mezclados (solo si hay custom delimiter)
    mixed_error = None
    if numbers.startswith("//"):
        i = 0
        while i < len(body):
            ch = body[i]
            # Si encontramos el inicio del delimitador custom, saltarlo completo
            if body[i:].startswith(delimiter):
                i += len(delimiter)
                continue
            # Si es dígito, signo negativo o newline (permitido), continuar
            if ch.isdigit() or ch == "-" or ch == "\n":
                i += 1
                continue
            # Si es coma y el delimitador no es coma, es un error
            if ch == ",":
                mixed_error = f"'{delimiter}' expected but ',' found at position {i}."
                break
            i += 1

    # Para extraer números cuando hay delimitadores mezclados, usar regex o parseo manual
    values = []
    negatives = []

    # Construir una versión "limpia" reemplazando delimitadores incorrectos
    clean_body = body
    if numbers.startswith("//"):
        # Reemplazar comas por el delimitador correcto para poder parsear
        clean_body = body.replace(",", delimiter)
        tokens = clean_body.split(delimiter)
    else:
        tokens = body.replace("\n", ",").split(",")

    for t in tokens:
        if not t.strip():
            continue
        try:
            n = int(t)
            if n < 0:
                negatives.append(n)
            values.append(n)
        except ValueError:
            # Si hay error al parsear, ignorar (ya detectamos el error de delimitador)
            pass

    # Recolectar errores
    errors = []
    if negatives:
        errors.append(
            f"Negative number(s) not allowed: {', '.join(map(str, negatives))}"
        )
    if mixed_error:
        errors.append(mixed_error)

    if errors:
        raise ValueError("\n".join(errors))

    return sum(values)


def add_v8(numbers: str) -> int:
    """
    Version 8 — Combine all features:
      - Custom delimiter
      - Handle newlines
      - Detect mixed delimiters
      - Detect negatives
      - Ignore numbers > 1000
    """
    if numbers == "":
        return 0

    delimiter = ","
    body = numbers

    if numbers.startswith("//"):
        header, body = numbers.split("\n", 1)
        delimiter = header[2:]

    # Validar terminación con delimitador
    if body.endswith(delimiter) or (
        not numbers.startswith("//") and (body.endswith(",") or body.endswith("\n"))
    ):
        raise ValueError("Invalid input: separator at the end")

    # Detectar delimitadores mezclados (solo si hay custom delimiter)
    mixed_error = None
    if numbers.startswith("//"):
        i = 0
        while i < len(body):
            ch = body[i]
            if body[i:].startswith(delimiter):
                i += len(delimiter)
                continue
            if ch.isdigit() or ch == "-" or ch == "\n":
                i += 1
                continue
            if ch == ",":
                mixed_error = f"'{delimiter}' expected but ',' found at position {i}."
                break
            i += 1

    # Para extraer números cuando hay delimitadores mezclados, limpiar primero
    values = []
    negatives = []

    clean_body = body
    if numbers.startswith("//"):
        # Reemplazar comas por el delimitador correcto para poder parsear
        clean_body = body.replace(",", delimiter)
        tokens = clean_body.split(delimiter)
    else:
        tokens = body.replace("\n", ",").split(",")

    for t in tokens:
        if not t.strip():
            continue
        try:
            n = int(t)
            if n < 0:
                negatives.append(n)
            # Solo agregar si es <= 1000
            if n <= 1000:
                values.append(n)
        except ValueError:
            # Si hay error al parsear, ignorar (ya detectamos el error de delimitador)
            pass

    # Recolectar errores
    errors = []
    if negatives:
        errors.append(
            f"Negative number(s) not allowed: {', '.join(map(str, negatives))}"
        )
    if mixed_error:
        errors.append(mixed_error)

    if errors:
        raise ValueError("\n".join(errors))

    return sum(values)
