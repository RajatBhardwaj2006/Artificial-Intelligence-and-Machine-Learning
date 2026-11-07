# OpenAI API & Generative AI Applications

Practical implementations and hands-on Jupyter Notebooks demonstrating integration with the **OpenAI SDK**, **OpenRouter**, multimodal vision models, automated text/email summarization systems, and generative image generation.

---

## 📌 Overview

This directory provides concrete examples of building generative AI solutions using modern LLM APIs:
- **Client Configuration:** Initializing the standard `OpenAI` Python SDK with custom endpoints (OpenAI, OpenRouter, Groq).
- **Chat & Responses API:** Structuring system instructions, user prompts, assistant roles, and temperature controls.
- **Multimodal Vision:** Feeding image inputs and base64-encoded strings to vision-capable models for analysis and captioning.
- **Image Generation & Editing:** Prompting generative image models and executing reference-guided image transformations.
- **Domain Applications:** Autonomous personal assistants for email summarization, key action item extraction, and query resolution.

---

## 📁 Notebooks & Module Index

| File | Primary Focus | Key Concepts & Deliverables |
|---|---|---|
| [`openai_api.ipynb`](openai_api.ipynb) | Master API Guide | Core OpenAI client setup, `responses.create` and `chat.completions.create`, parameter tuning (`temperature`, `max_tokens`), building a full `PersonalAssistant` class, and multimodal queries. |
| [`Email_summarize.ipynb`](Email_summarize.ipynb) | Email Summarizer | Object-oriented `Email_assistant` implementation that digests lengthy email threads, isolates critical deadlines/action items, and outputs concise summaries. |
| [`Generate_image.ipynb`](Generate_image.ipynb) | Generative Image Studio | Generating high-fidelity images from detailed text descriptions and demonstrating reference-based image editing pipelines. |
| [`Image_response.ipynb`](Image_response.ipynb) | Vision Understanding | Sending image URLs and image data to multimodal models for semantic analysis, description, and visual reasoning. |
| [`Response.ipynb`](Response.ipynb) | Chat Completions | Concise blueprint for querying open-weight and proprietary models via OpenRouter with streaming/non-streaming completions. |

---

## 🛠️ Prerequisites & Installation

Install the OpenAI client library and supporting tools:

```bash
pip install openai python-dotenv jupyter pillow
```

Configure your API credentials in your environment or a `.env` file:

```bash
# For direct OpenAI access:
export OPENAI_API_KEY="sk-..."

# Or for OpenRouter access:
export OPENROUTER_API_KEY="sk-or-..."
```

---

## 🚀 How to Run

Launch the notebooks in Jupyter:

```bash
jupyter notebook OpenAI/
```

- Start with [`openai_api.ipynb`](openai_api.ipynb) for a thorough walkthrough of client initialization and prompting patterns.
- Open [`Email_summarize.ipynb`](Email_summarize.ipynb) to test the email assistant pipeline.
- Open [`Generate_image.ipynb`](Generate_image.ipynb) to experiment with image generation.

---

## 💡 Practical AI Design Patterns

### 1. Robust System Prompting
Using structured system messages to ground the model persona:
```python
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": "You are an executive assistant. Be concise and prioritize action items."},
        {"role": "user", "content": email_text}
    ]
)
```

### 2. Base64 Multimodal Ingestion
Encoding local image files into base64 data URIs allows sending local visuals to cloud vision endpoints without hosting them publicly.
