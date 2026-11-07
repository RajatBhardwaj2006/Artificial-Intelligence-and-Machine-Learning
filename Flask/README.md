# Flask Web Applications & AI Assistant

A comprehensive suite of **Flask** web applications, microservices, and interactive web tools demonstrating server-side rendering with Jinja2, form processing, JSON REST APIs, template inheritance, and an LLM-powered AI Chatbot assistant.

---

## 📌 Overview

This repository section bridges backend web development and artificial intelligence:
- **Routing & HTTP Methods:** Managing `GET` and `POST` request lifecycles.
- **RESTful JSON Services:** Building microservices returning structured JSON payloads.
- **Form Handling & Validation:** Capturing user inputs from forms, processing payloads, and rendering dynamic responses.
- **Jinja2 Template Inheritance:** Structured layouts using base templates, blocks, and flash messaging.
- **AI Assistant Web Integration:** Connecting modern generative LLMs (via Groq and the OpenAI-compatible client) directly into a web interface.

---

## 📁 Repository Structure & Projects

```
Flask/
├── Ai_assistant/             # Fullstack AI Chat Assistant
│   ├── static/style.css      # Dark/modern UI styling
│   ├── templates/index.html  # Interactive chat interface
│   ├── main.py               # Flask backend integrated with Groq LLM
│   └── README.md             # Dedicated assistant documentation
├── static/                   # Static assets for core Flask apps
│   ├── app.js                # Frontend scripting
│   ├── form.css              # Form styling
│   ├── login.css             # Authentication screen styles
│   ├── resubmit.css          # Resubmission notice styling
│   └── thankyou.css          # Confirmation screen styles
├── Templates/                # Jinja2 HTML templates
│   ├── contact.html          # Contact page with flash messages
│   ├── form.html             # User registration/data entry form
│   ├── index.html            # Landing page
│   ├── layout.html           # Reusable master layout
│   ├── login.html            # Login portal
│   ├── resubmit.html         # Duplicate submission warning
│   └── thankyou.html         # Personalized confirmation page
├── API_with_Json.py          # Minimal JSON REST API endpoint
├── application.py            # Basic routing and template rendering
├── Login_website.py          # Complete multi-page form processing web app
├── template_inheritance.py   # Flash messages, redirects, and Jinja2 inheritance
├── StepUp.ipynb              # Notebook walkthrough of Flask concepts
└── README.md                 # Module documentation
```

---

## 🛠️ Prerequisites & Installation

Ensure you have Python installed, then install the dependencies:

```bash
pip install flask python-dotenv openai
```

If running the **AI Assistant**, ensure your Groq API key is configured in your environment or a `.env` file:

```env
GROQ_API_KEY="your-groq-api-key-here"
```

---

## 🚀 Applications & How to Run

### 1. JSON REST API Microservice
Returns structured JSON data with proper HTTP status codes.
```bash
python Flask/API_with_Json.py
# Access: http://127.0.0.1:5000/
```

### 2. Multi-Page Registration & Form App
Demonstrates form input parsing (`request.form`), redirection, and dynamic template rendering.
```bash
python Flask/Login_website.py
# Or via Flask CLI:
flask --app Flask/Login_website run --debug
# Access: http://127.0.0.1:5000/ (Login) or http://127.0.0.1:5000/form (Registration)
```

### 3. Template Inheritance & Flash Messages
Demonstrates session secret keys, `flash()`, and `redirect(url_for(...))`.
```bash
python Flask/template_inheritance.py
# Access: http://127.0.0.1:5000/contact
```

### 4. Interactive AI Chatbot Assistant
A full-stack chatbot with a web UI that streams user queries to Groq LLMs via an OpenAI client wrapper.
```bash
cd Flask/Ai_assistant
python main.py
# Access: http://127.0.0.1:5000/
```

---

## 💡 Architectural Best Practices Demonstrated

1. **Separation of Concerns:** Clean division between presentation (`Templates/`), styling (`static/`), and server business logic.
2. **Template Reusability:** Leveraging `layout.html` to prevent boilerplate duplication across web pages.
3. **Robust Request Parsing:** Distinguishing between `GET` render requests and `POST` payload data processing.
4. **Secure Secret Management:** Storing API keys and credentials in `.env` files rather than hardcoding in source files.
