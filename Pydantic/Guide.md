# Pydantic in Python

## Overview

Pydantic is a Python library used for **data validation, parsing, serialization, and structured data modeling** using Python type hints.

It is commonly used when working with external data such as:

- APIs
- JSON files
- CSV files
- Databases
- Configuration files
- User input

Pydantic ensures that incoming data matches the expected schema and raises validation errors when invalid data is provided.

---

# Key Concepts

## 1. Type Coercion (Default Behavior)

By default, Pydantic automatically converts compatible input values into the expected data type.

### Example

```python
"25" → 25
"true" → True
```

### Use Case

Useful when input data comes in different formats from APIs, files, or user input.

---

## 2. Strict Types

Pydantic can enforce strict validation without automatic type conversion.

### Example

```python
"25" ❌ int
25   ✅ int
```

### Use Case

Useful when strict schema validation and data accuracy are required.

---

## 3. Serialization

Pydantic can convert model objects into:

- Python dictionaries
- JSON format

### Use Case

Useful for:

- APIs
- Logging
- Databases
- Data pipelines

---

## 4. Dataclass vs Pydantic

### Python Dataclass

- Creates structured objects with type hints.
- Reduces boilerplate code.
- Type hints are **not validated at runtime by default** (only provide us warning and doesn't break code).
- Invalid data may be accepted without raising errors.

### Pydantic

- Validates data at runtime.
- Raises validation errors for invalid input.
- Supports:
  - Default values
  - Validators
  - Type coercion
  - Strict types
  - Serialization

---

## 5. TypedDict vs Pydantic

### TypedDict

- Defines dictionary structure using type hints.
- Helps static type checkers and IDEs.
- Does **not validate data at runtime** only provide us warning and doesn't break code).

### Pydantic

- Validates input data during execution.
- Raises validation errors for incorrect data.
- Supports:
  - Parsing
  - Default values
  - Validators
  - Serialization

---

# When to Use Pydantic

Use Pydantic when:

✅ Working with API responses  
✅ Processing JSON or CSV data  
✅ Building ETL/data pipelines  
✅ Validating configuration files  
✅ Enforcing schema consistency  
✅ Handling user input safely

---

# Conclusion

Pydantic combines **type hints + runtime validation + parsing + serialization**, making it more powerful than traditional dataclasses or TypedDict for real-world Python applications.
