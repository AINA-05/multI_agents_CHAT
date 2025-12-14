# Abstract: Multi-Agent Chat System

## What is the system?
The Multi-Agent Chat System is a modular AI application where multiple specialized agents collaborate to solve user problems. Unlike a single monolithic script, this system distributes responsibilities: one agent searches for information, another analyzes it, and a third remembers it. This mimics real-world organizational structures where managers delegate tasks to specialists.

## How does it work?
The system operates on a hub-and-spoke model:
1.  **Input**: The user sends a query to the **Coordinator Agent** (the Manager).
2.  **Memory Check**: The Coordinator first asks the **Memory Agent** if this question has been answered before. The Memory Agent uses vector similarity (TF-IDF) to find semantically similar past queries.
3.  **Research**: If no memory is found, the **Research Agent** simulates a web search to retrieve raw data (e.g., facts about Neural Networks).
4.  **Analysis**: If the query is complex (e.g., "compare" or "analyze"), the **Analysis Agent** processes the raw data to provide insights or summaries.
5.  **Synthesis & Storage**: The Coordinator combines the results, displays them to the user, and sends the new knowledge to the Memory Agent for future retrieval.

## System Design

```mermaid
graph TD
    User([User]) <--> Coordinator[Coordinator Agent]
    
    Coordinator <-->|Check/Store| Memory[Memory Agent]
    Coordinator <-->|Fetch Info| Research[Research Agent]
    Coordinator <-->|Process Data| Analysis[Analysis Agent]
    
    subgraph Memory Module
    Memory <--> VectorStore[Vector DB (TF-IDF)]
    Memory <--> JSON[Persistent Storage]
    end
```

*Efficiency is achieved through the **Memory Agent**, which prevents redundant research by recalling high-confidence answers from previous interactions.*
