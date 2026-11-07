# CSS Fundamentals & UI Styling Lab

A hands-on, practical repository of **Cascading Style Sheets (CSS3)** modules, layouts, UI components, and design exercises covering core styling mechanics, positioning, typography, inheritance, transitions, and component builds.

---

## 📌 Overview

This directory provides interactive demos, code snippets, and mini-projects illustrating foundational to intermediate CSS concepts:
- **Selectors & Specificity:** Applying rules to elements, classes, IDs, and nested hierarchies.
- **The Box Model:** Margin, border, padding, dimensions, and box sizing.
- **CSS Positioning & Layouts:** In-depth exploration of normal flow, static, relative, absolute, and fixed positioning.
- **Inheritance & Cascade:** How CSS properties propagate down DOM trees and how conflicts resolve.
- **Typography & Color:** Font families, weights, alignments, decoration, and modern color theory.
- **Interactive UI Components:** Card hover animations, social media button styling, and a CSS traffic light simulator.

---

## 📁 Repository Structure & Modules

### 1. Interactive Demos & Components

| Demo / Component | HTML File | CSS File | Highlights & Key Techniques |
|---|---|---|---|
| **Card Hover Effects** | [`card_hover.html`](card_hover.html) | [`card_hover.css`](card_hover.css) | Hover transitions, shadows, smooth scale transforms, and border-radius. |
| **Traffic Light Simulator** | [`trafic.html`](trafic.html) | [`trafic.css`](trafic.css) | Fixed dimensional containers, circle styling with `border-radius: 50%`, and glow effects. |
| **CSS Positioning Lab** | [`static.html`](static.html) | [`static.css`](static.css) | Static, relative, and absolute offset demonstration (`top`, `left`, `z-index`). |
| **Social UI Components** | [`index.html`](index.html) | [`facebook.css`](facebook.css) / [`style.css`](style.css) | Branding buttons, navigation elements, input styling, and form aesthetics. |

### 2. Core Concept Studies

| Study Area | Key Files | Description |
|---|---|---|
| **Inheritance & Cascade** | [`Inheritance.html`](Inheritance.html)<br>[`inheritance_demo.html`](inheritance_demo.html)<br>[`inheri.css`](inheri.css)<br>[`inheritance_style.css`](inheritance_style.css) | Demonstrates inherited properties (e.g., text, color, typography) vs non-inherited properties (e.g., borders, margins, padding). |
| **Typography & Fonts** | [`font_properties.css`](font_properties.css)<br>[`text_properties.css`](text_properties.css) | Font stacks, weights, styles, letter-spacing, line-height, text-transform, and text-align. |
| **Color Schemes** | [`color.css`](color.css) | RGB, RGBA, Hexadecimal color notations, background fills, and opacity adjustments. |
| **Box Model & Layout** | [`part3.html`](part3.html)<br>[`part3.css`](part3.css) | Content-box vs border-box, padding distributions, outline vs border. |

### 3. Practice & Assessment Tasks

- [`PracticeQs.html`](PracticeQs.html) & [`Index1.html`](Index1.html): Comprehensive collection of practice prompts for styling exercises.
- [`Tasks/`](Tasks/): Dedicated challenge folder:
  - [`Tasks/task.html`](Tasks/task.html): Test harness page.
  - [`Tasks/task1.css`](Tasks/task1.css): Basic box model layout assignment.
  - [`Tasks/task2.css`](Tasks/task2.css): Advanced selectors and layout challenge.

---

## 🚀 How to View and Experiment

No build step or server is required. You can preview any file directly in your browser:

1. **Direct Browser Launch:**
   - Double click any `.html` file (e.g., [`card_hover.html`](card_hover.html) or [`trafic.html`](trafic.html)) to open it in your default web browser.

2. **VS Code Live Server:**
   - If using VS Code, right-click any HTML file and select **Open with Live Server** to enable real-time hot reloading upon saving changes.

---

## 💡 Best Practices Demonstrated

- Separation of concerns between markup ([HTML](../HTML/)) and presentation ([CSS](./)).
- DRY (Don't Repeat Yourself) styling using modular CSS classes.
- Responsive units and predictable box-model behavior.
- Clean selector naming conventions.
