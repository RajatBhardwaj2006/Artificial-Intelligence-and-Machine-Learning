# AI Agent Architecture & Workflows

An end-to-end collection of intelligent, autonomous AI agents built using the **Agno** framework, powered by high-speed **Groq** LLM inference and extended with domain-specific tools (Web Search, Financial Intelligence, YouTube Video Summarization, SQLite Memory, and Multi-Agent Collaboration).

---

## 📌 Overview

This directory demonstrates modern agentic AI patterns:
- **Autonomous Tool Use:** Agents equipped with external APIs (DuckDuckGo, Yahoo Finance, YouTube Tools).
- **Persistent Agentic Memory:** Storing user session memory in an SQLite database for cross-prompt personalization.
- **Multi-Agent Teams:** Orchestrating multiple specialized agents under a centralized team leader.
- **Interactive UI:** A Streamlit frontend for video content analysis.

---

## 📁 File Structure & Breakdown

| File | Type | Description |
|---|---|---|
| [`agent.py`](agent.py) | CLI Script | Educational agent using DuckDuckGo search to explain complex technical concepts in concise, student-friendly terms. |
| [`analyzer.py`](analyzer.py) | Module | Production-grade YouTube video analyst agent with structured prompt engineering for timestamping, segmentation, and topic extraction. |
| [`finance.py`](finance.py) | CLI Script | Financial research assistant utilizing `YFinanceTools` to evaluate equities, analyze historical metrics, and provide structured investment suggestions. |
| [`memory.py`](memory.py) | CLI Script | Demonstrates stateful conversation memory with `SqliteDb`, agentic recall, and user profile management (`get_user_memories`). |
| [`multi_agent.py`](multi_agent.py) | CLI Script | Multi-agent collaboration pattern with an `Answer & Translation Team` orchestrating parallel responses across English, German, and Spanish agents. |
| [`ui.py`](ui.py) | Streamlit App | Interactive web application allowing users to input any YouTube video URL and generate a structured analytical breakdown. |
| [`Youtube_Video_Analyzer.py`](Youtube_Video_Analyzer.py) | CLI Script | Standalone YouTube analyzer script featuring real-time streaming output for fast comprehension of video materials. |

---

## 🛠️ Tech Stack & Dependencies

- **Agent Framework:** [Agno](https://github.com/agno-agi/agno) (formerly Phidata)
- **Inference Engine:** [Groq](https://groq.com/) (`openai/gpt-oss-120b` or custom models)
- **Tools & Integrations:**
  - `agno.tools.duckduckgo` for real-time web grounding
  - `agno.tools.yfinance` for live stock quotes and historical metrics
  - `agno.tools.youtube` for transcript extraction and video metadata analysis
- **Storage:** `SqliteDb` for persistent conversation memory
- **UI Framework:** Streamlit
- **Environment:** `python-dotenv`, `rich`

---

## 🚀 Getting Started

### 1. Prerequisites & Environment Setup

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install agno groq duckduckgo-search yfinance youtube-transcript-api streamlit python-dotenv rich
```

### 2. Configure Environment Variables

Create a `.env` file in the root or module directory:

```env
GROQ_API_KEY="your-groq-api-key-here"
```

---

## 💻 Usage Examples

### 1. Run the General Search Agent
```bash
python AIAgent/agent.py
```

### 2. Run the Stock & Financial Analyst Agent
```bash
python AIAgent/finance.py
```

### 3. Run the Persistent Memory Demo
```bash
python AIAgent/memory.py
```

### 4. Run the Multilingual Agent Team
```bash
python AIAgent/multi_agent.py
```

### 5. Launch the YouTube Video Analyzer Web App
```bash
streamlit run AIAgent/ui.py
```

---

## 🧠 Key Agentic Design Patterns Demonstrated

1. **ReAct & Tool Augmented Generation:** Agents autonomously decide when to query search engines or financial APIs before generating an answer.
2. **Deterministic Prompt Guidelines:** Structured prompting enforces markdown tables, precise timestamp formats, and category tagging.
3. **Session-Level Personalization:** User identifiers (`user_id`) allow agents to recall user preferences across separate interactions.
4. **Agent-to-Agent Delegation:** Team configurations distribute user prompts across specialized agents and synthesize collaborative results.
