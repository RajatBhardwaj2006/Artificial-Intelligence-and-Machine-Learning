# HTML5 Markup & Web Architecture Essentials

A practical, example-driven curriculum of **HTML5 (Hypertext Markup Language)** components, semantic structures, tables, interactive form controls, and hands-on coding exercises.

---

## 📌 Overview

HTML forms the foundational backbone of the World Wide Web. This module provides atomic code examples and incremental practice labs covering:
- **Core Document Structure:** HTML5 doctype declaration, head/body separation, metadata, and Emmet workflows.
- **Typography & Semantic Tags:** Headers (`h1`–`h6`), paragraphs, text formatting (`b`, `i`, `u`, `sub`, `sup`), and HTML entities.
- **Display Semantics:** Understanding Block vs. Inline element behavior and division containers (`div`).
- **Structured Data:** Ordered lists, unordered lists, multi-level nested lists, and advanced HTML tables with `rowspan` and `colspan`.
- **Form Controls & Inputs:** Text inputs, text areas, checkboxes, radio button groups, range sliders, select dropdowns, and label associations.
- **10 Step-by-Step Practice Labs:** Progressive exercises reinforcing real-world markup creation.

---

## 📁 Repository Structure & Module Breakdown

### 1. Document Structure & Typography

| File | Concepts Covered |
|---|---|
| [`boiler.html`](boiler.html) | Standard HTML5 boilerplate template (`<!DOCTYPE html>`, `html`, `head`, `meta`, `title`, `body`). |
| [`first.html`](first.html) | Beginner starter page introducing basic headers and paragraphs. |
| [`html5.html`](html5.html) | Modern HTML5 semantic containers and layout elements. |
| [`emmets.html`](emmets.html) | Demonstrates VS Code Emmet shortcuts for rapid markup generation. |
| [`entities.html`](entities.html) | Special character entities (`&nbsp;`, `&lt;`, `&gt;`, `&amp;`, `&copy;`). |
| [`sub_&_sup.html`](sub_&_sup.html) | Subscript (`<sub>`) and superscript (`<sup>`) formatting for scientific/mathematical notation (e.g. $H_2O$, $x^2$). |
| [`tag.html`](tag.html) | Text decoration tags: bold, italics, underlines, and horizontal rules (`<hr>`). |
| [`inlineVSblock.html`](inlineVSblock.html) | Comparison of block-level elements (full line width) vs inline elements (content width only). |
| [`div.html`](div.html) | Generic division elements (`<div>`) for grouping and structural scoping. |

### 2. Lists & Tabular Data

| File | Concepts Covered |
|---|---|
| [`list.html`](list.html) | Unordered lists (`<ul>`), ordered lists (`<ol>` with numeric, alphabetic, roman numbering), and nested item hierarchies. |
| [`table.html`](table.html) | Tabular structure basics: `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, and `<td>`. |
| [`Colspan_Rowspan.html`](Colspan_Rowspan.html) | Complex table cell merging using `colspan` (horizontal span) and `rowspan` (vertical span). |

### 3. Forms & User Interactive Inputs

| File | Concepts Covered |
|---|---|
| [`from.html`](from.html) | Basic form setup, form actions, submit buttons, and `GET`/`POST` submission attributes. |
| [`from_label.html`](from_label.html) | Accessible forms associating `<label for="...">` with `<input id="...">`. |
| [`check_box.html`](check_box.html) | Multi-select checkboxes (`type="checkbox"`). |
| [`radio_button.html`](radio_button.html) | Single-choice radio button groups using identical `name` attributes. |
| [`select.html`](select.html) | Dropdown selection menus (`<select>` and `<option>`). |
| [`range.html`](range.html) | Numerical slider input controls (`type="range"` with `min`, `max`, `step`). |
| [`text_area.html`](text_area.html) | Multi-line text input fields (`<textarea rows="..." cols="...">`). |

### 4. Practice Exercises (`Practice/`)

The [`Practice/`](Practice/) folder contains 10 progressive practice problem implementations:
- [`Practice0.html`](Practice/Practice0.html) – [`Practice2.html`](Practice/Practice2.html): Headings, formatting, and bio card layouts.
- [`practice3.html`](Practice/practice3.html) – [`practice5.html`](Practice/practice5.html): Nested lists, links, and media inclusions.
- [`practice6.html`](Practice/practice6.html): Full student grade and schedule tables.
- [`practice7.html`](Practice/practice7.html) – [`Practice9.html`](Practice/Practice9.html): Comprehensive user registration forms and survey questionnaires.

---

## 🚀 How to View and Run

HTML runs natively in any modern web browser:
1. Double-click any `.html` file in your file explorer to open it in Chrome, Edge, Firefox, or Safari.
2. In VS Code, install the **Live Server** extension and click **Go Live** to preview changes in real time.

---

## 💡 Best Practices

- Always specify `alt` attributes on `<img>` tags for accessibility and SEO.
- Associate inputs with explicit `<label>` tags using matching `for` and `id` properties.
- Use semantic elements over arbitrary `<div>` soup to ensure clear page structure.
