
from agents.coordinator_agent import Coordinator
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.memory_agent import MemoryAgent

def main():
    coordinator_agent = Coordinator(
        research_agent=ResearchAgent(),
        analysis_agent=AnalysisAgent(),
        memory_agent=MemoryAgent()
    )

    print("Multi-Agent Chat System (type 'exit' to quit)\n")

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

        response = coordinator_agent.handle_query(user_input)
        print("System:", response)

if __name__ == "__main__":
    main()


