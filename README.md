# Multi-Agent Chat System

A collaborative Multi-Agent System (MAS) designed to answer user queries through a network of specialized agents. This system demonstrates role separation, inter-agent coordination, and adaptive memory.

## Architecture

The system consists of a **Coordinator Agent** that manages three worker agents:

1.  **Research Agent**: Retrieves information from a simulated knowledge base.
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

