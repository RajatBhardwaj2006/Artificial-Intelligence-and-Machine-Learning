# Python Programming: Zero to Mastery & Applied Scripts

A structured, 35+ module Python programming curriculum covering core syntax, control structures, data structures, functional paradigms, Object-Oriented Programming (OOP), file streams, exception handling, and applied automation utilities.

---

## 📌 Overview

This curriculum provides beginner-to-advanced Python scripts, organized systematically with numbered milestones:
- **Foundations:** Syntax, variables, dynamic typing, keywords, PEP 8 style guide, and operators.
- **Control Flow:** Conditional branching, nested conditionals, structural pattern matching (`match-case`), and loop controls.
- **Data Structures:** Lists, tuples, dictionaries, and sets with built-in manipulation methods.
- **Functions & Functional Tools:** Parameter passing, return tuples, anonymous lambda expressions.
- **Object-Oriented Programming (OOP):** Class design, `__init__` constructors, encapsulation, inheritance, and polymorphism.
- **Systems & File I/O:** Reading/writing disk files, JSON serialization, robust exception handling (`try-except-finally`).
- **Applied Scripts:** Practical tools including QR Code generators, pure Python Mean Squared Error (MSE), loop diagnostics, and Git automation bots.

---

## 📁 Sequential Curriculum Roadmap

### Stage 1: Syntax & Foundations
- [`01_first_code.py`](01_first_code.py): Standard output and initial Python execution.
- [`02_variable.py`](02_variable.py): Variable declaration, identifiers, dynamic memory references.
- [`03_Data_types.py`](03_Data_types.py): Primitive types (`int`, `float`, `str`, `bool`, `None`).
- [`04_keyword.py`](04_keyword.py): Python reserved keywords and naming rules.
- [`05_style_guide.py`](05_style_guide.py): PEP 8 formatting standards and readability best practices.
- [`06_operator.py`](06_operator.py): Arithmetic, relational, logical, assignment, and membership operators.
- [`07_operator_precedenec.py`](07_operator_precedenec.py): Operator precedence and PEMDAS evaluation order.
- [`08_type_conversion.py`](08_type_conversion.py): Implicit coercion vs explicit casting (`int()`, `float()`, `str()`).
- [`09_average.py`](09_average.py): Applied calculation of running and arithmetic means.

### Stage 2: Control Flow & Loops
- [`10_conditional.py`](10_conditional.py): `if`, `elif`, and `else` decision trees.
- [`11_Nested_if.py`](11_Nested_if.py): Multi-layer nested conditionals.
- [`12_match_case.py`](12_match_case.py): Python 3.10+ structural pattern matching.
- [`13_for_loop.py`](13_for_loop.py): Iterating over sequences, ranges (`range()`), and iterables.
- [`14_while_loop.py`](14_while_loop.py): Condition-driven while loops and termination safeguards.
- [`15_Break_continue.py`](15_Break_continue.py): Early loop exits (`break`) and step skips (`continue`).
- [`Basic_loop_explatation.py`](Basic_loop_explatation.py): Detailed execution trace of loop counters and accumulators.

### Stage 3: Functions, Strings & Data Structures
- [`16_Function.py`](16_Function.py): Function definitions, parameter signatures, docstrings, and return statements.
- [`17_lambda.py`](17_lambda.py): Anonymous single-expression lambda functions.
- [`18_Stringss.py`](18_Stringss.py): String indexing, slicing, concatenation, and formatting methods.
- [`19_list.py`](19_list.py): Dynamic mutable arrays, list comprehension, slicing, sorting, and indexing.
- [`20_Tuples.py`](20_Tuples.py): Immutable sequence packing, unpacking, and tuple operations.
- [`21_dict.py`](21_dict.py): Hash maps, key-value pairs, nested dicts, and comprehension.
- [`22_Sets.py`](22_Sets.py): Unordered unique collections, set theory (union, intersection, difference).
- [`35_Second_largest_number.py`](35_Second_largest_number.py): Algorithmic search for the second largest element in a sequence.

### Stage 4: Object-Oriented Programming (OOP)
- [`23_oops.py`](23_oops.py): Class definitions, instances, and basic object instantiation.
- [`24_init.py`](24_init.py): The `__init__` constructor method and `self` parameter binding.
- [`25_attribute.py`](25_attribute.py): Class-level attributes vs instance-level attributes.
- [`26_types_constructor.py`](26_types_constructor.py): Default constructors, parameterized constructors, and object lifecycles.
- [`27_oops_pillars.py`](27_oops_pillars.py): The 4 core OOP pillars: Encapsulation, Abstraction, Inheritance, and Polymorphism.
- [`28_polymorphism.py`](28_polymorphism.py): Method overriding, duck typing, and polymorphic behavior.
- [`29_assignment_problem.py`](29_assignment_problem.py): Applied OOP modeling challenge problem.

### Stage 5: System I/O, Error Handling & Automation
- [`30_file.py`](30_file.py): File streams, context managers (`with open()`), read, write, and append modes.
- [`31_Expection_handling.py`](31_Expection_handling.py): Exception handling blocks (`try`, `except Exception as e`, `else`, `finally`).
- [`32_JSON.py`](32_JSON.py): Serializing Python dictionaries to JSON (`json.dump`, `json.dumps`) and deserialization (`json.load`, `json.loads`).
- [`MSE.py`](MSE.py): Pure Python implementation of the Mean Squared Error (MSE) loss formula.
- [`QR.py`](QR.py): Generating scannable QR Code graphics from arbitrary URLs or text payloads.
- [`Auto_Commit_Bot`](Auto_Commit_Bot): Automation script demonstrating programmatic Git commit scheduling.
- [`PYTHON_PRACTICE/`](PYTHON_PRACTICE/): Additional problem-solving challenges (`Practice1.py`, `Practice2.py`).

---

## 🚀 Execution & Usage

Run any script directly using Python 3:

```bash
# Test structural pattern matching
python Python/12_match_case.py

# Run OOP demonstration
python Python/27_oops_pillars.py

# Test QR Code generator (requires: pip install qrcode pillow)
python Python/QR.py

# Test JSON file parsing
python Python/32_JSON.py
```
