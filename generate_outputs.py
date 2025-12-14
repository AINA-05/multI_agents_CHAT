import os
import sys
from agents.coordinator_agent import Coordinator
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.memory_agent import MemoryAgent

# Ensure outputs directory exists
if not os.path.exists("outputs"):
    os.makedirs("outputs")

def run_scenario(filename, query, description):
    print(f"Running Scenario: {description}")
    
    # Capture stdout
    original_stdout = sys.stdout
    file_path = f"outputs/{filename}"
    
    with open(file_path, "w") as f:
        sys.stdout = f
        
        print(f"--- Scenario: {description} ---")
        print(f"Query: {query}\n")
        
        # Initialize agents (fresh for each test to be clean, or shared if memory test)
        # For memory test, we need state, so we'll handle that uniquely
        coord = Coordinator(
            research_agent=ResearchAgent(),
            analysis_agent=AnalysisAgent(),
            memory_agent=MemoryAgent()
        )
        
        response = coord.handle_query(query)
        print(f"\nFinal System Response: {response}")
        
    sys.stdout = original_stdout
    print(f"Saved output to {file_path}")

def run_all_scenarios():
    # 1. Simple Query
    run_scenario("simple_query.txt", 
                 "What are the main types of neural networks?", 
                 "Simple Information Retrieval")

    # 2. Complex Query
    run_scenario("complex_query.txt", 
                 "Research transformer architectures, analyze their computational efficiency, and summarize key trade-offs.", 
                 "Complex Research and Analysis")

    # 3. Memory Test
    # Need to prime memory first
    print("Running Memory Test (Priming run first...)")
    coord = Coordinator(ResearchAgent(), AnalysisAgent(), MemoryAgent())
    coord.handle_query("Tell me about neural networks") # Prime
    
    # Actual test run
    file_path = "outputs/memory_test.txt"
    original_stdout = sys.stdout
    with open(file_path, "w") as f:
        sys.stdout = f
        print("--- Scenario: Memory Retrieval ---")
        print("Query: What did we discuss about neural networks earlier?\n")
        response = coord.handle_query("What did we discuss about neural networks earlier?") # Should hit vector similar to "Tell me about..."
        # Note: The mock vector store might need exact semantic match or keyword override for "earlier". 
        # Since our simple vector store is TF-IDF, "neural networks" should match enough if the previous content was stored.
        print(f"\nResponse: {response}")
    sys.stdout = original_stdout

    # 4. Multi-step
    run_scenario("multi_step.txt",
                 "Find recent papers on reinforcement learning, analyze their methodologies, and identify common challenges.",
                 "Multi-step Task")

    # 5. Collaborative
    run_scenario("collaborative.txt",
                 "Compare two machine-learning approaches and recommend which is better for our use case.",
                 "Collaborative comparison")

if __name__ == "__main__":
    run_all_scenarios()
