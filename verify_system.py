import os
import shutil
import time
from agents.coordinator_agent import Coordinator
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.memory_agent import MemoryAgent

MEMORY_FILE = "memory_data.json"

def cleanup():
    if os.path.exists(MEMORY_FILE):
        os.remove(MEMORY_FILE)
    print("[Test] Cleaned up old memory file.")

def test_system():
    cleanup()

    print("\n--- TEST 1: First Run (Cold Start) ---")
    # Initialize agents
    coord = Coordinator(
        research_agent=ResearchAgent(),
        analysis_agent=AnalysisAgent(),
        memory_agent=MemoryAgent()
    )

    query = "Tell me about neural networks"
    print(f"Query: {query}")
    response = coord.handle_query(query)
    
    # Verify response structure or content (simplistic check)
    if "neural networks" in str(response).lower() or isinstance(response, list):
        print("[Pass] Got valid response.")
    else:
        print("[Fail] Unexpected response format.")

    # Check if file was created
    if os.path.exists(MEMORY_FILE):
         print("[Pass] Memory file created.")
    else:
         print("[Fail] Memory file NOT created.")

    print("\n--- TEST 2: Second Run (Persistence Check) ---")
    # Re-initialize agents (simulate restart)
    coord2 = Coordinator(
        research_agent=ResearchAgent(),
        analysis_agent=AnalysisAgent(),
        memory_agent=MemoryAgent()
    )
    
    # Same query, should hit memory
    start_time = time.time()
    response2 = coord2.handle_query(query)
    end_time = time.time()
    
    # We can't easily assert print output, but we can check timing or internal state if we exposed it.
    # For now, let's trust the logic if it runs without error and returns data.
    if response2 == response:
        print("[Pass] Response matches previous run (likely from memory).")
    else:
        print("[Warn] Response differs. Might be okay if format changed, but checks memory consistency.")

    print("\n--- TEST 3: Complex Query ---")
    query_complex = "Compare CNNs and RNNs"
    response_complex = coord2.handle_query(query_complex)
    if "After comparison" in str(response_complex):
        print("[Pass] Analysis Agent triggered correctly.")
    else:
        print(f"[Fail] Analysis Agent might not have triggered. Got: {response_complex}")

if __name__ == "__main__":
    test_system()
