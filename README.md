
## Multi-Agent Chat System

A collaborative Multi-Agent System (MAS) designed to answer user queries through a network of specialized agents. This system demonstrates role separation, inter-agent coordination, and adaptive memory.
responsibilities: one agent searches for information, another analyzes it, and a third remembers it. This mimics real-world organizational structures where managers delegate tasks to specialists. 
## Project Overview:
This project implements a multi-agent AI system without using any Large Language Model (LLM). The primary objective of the system is to demonstrate agent-based architecture, orchestration logic, and
memory handling using deterministic and explainable techniques rather than generative models. The system is composed of multiple specialized agents, each assigned a well-defined role. A
Coordinator Agent acts as the central planner and router, analyzing user queries and delegating tasks to
appropriate agents. The Research Agent handles factual and information-based queries, while the
Analysis Agent is responsible for logical reasoning, comparisons, and structured analysis. A dedicated
Memory Agent manages contextual storage and retrieval using a vector-based similarity mechanism. Instead of relying on LLMs, the system uses rule-based decision making, modular agent design, and a
TF-IDF vector memory system to simulate intelligent behavior. This approach ensures deterministic
outputs, transparency, and full control over system behavior, eliminating common issues such as
hallucinations and unpredictable responses. The architecture is designed to be LLM-ready, allowing future integration of generative models without
structural changes. The project is containerized using Docker, ensuring environment consistency, portability, and ease of deployment. Although currently operated via a command-line interface (CLI), the
system can be extended to support web-based or graphical interfaces using frameworks such as FastAPI, Streamlit, or React. Overall, this project demonstrates a foundational implementation of AI agent engineering, focusing on
orchestration, memory, and explainable intelligence, making it suitable for learning, research, and future
scalable AI system development. 

## Architecture

The system consists of a **Coordinator Agent** that manages three worker agents:

1.  **Research Agent**: Retrieves information from a simulated Knowledge Base.
2.  **Analysis Agent**: Processes data, compares concepts, and summarizes findings.
3.  **Memory Agent**: Manages long-term persistence (JSON) and retrieval (Vector Search + TF-IDF).

**Flow**:
User Query -> Coordinator -> [Memory Check] -> Research -> [Analysis if complex] -> Storage -> Response.

## Features

-   **Task Decomposition**: Complex queries are broken down into research and analysis steps.
-   **Structured Memory**: Facts are stored with confidence scores and timestamps.
-   **Persistence**: Memory is saved to disk (`memory_data.json`) and persists across restarts.
-   **Vector Search**: Uses TF-IDF and Cosine Similarity to find checking past interactions.

## How to Run

### Prerequisites
-   Python 3.10+
-   `pip install -r requirements.txt`

### Running Locally
```bash
python main.py
```
Type `exit` to quit.

### Running with Docker
```bash
docker-compose up --build
```

## detailed Design
-   **Coordinator**: The central "brain" that routes tasks.
-   **Memory**: Implemented using `sklearn` for vectorization and a JSON file for persistent storage.

