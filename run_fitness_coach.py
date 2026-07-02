"""
run_fitness_coach.py

Interactive CLI for the Fitness Coach agent (fitness_coach_agent.py).
Same shape as run_agent.py, but talks to the coach persona instead of
the plain BMI agent — both reuse the same bmi_tool under the hood.

Usage:
    export OPENAI_API_KEY=sk-...
    python run_fitness_coach.py
"""

import uuid

from dotenv import load_dotenv

from fitness_coach_agent import build_agent

load_dotenv()


def main():
    print("=== Fitness Coach Agent (LangGraph) ===")
    print("Tell me your weight/height and I'll suggest a workout focus. "
          "Type 'quit' to exit.\n")

    app = build_agent()
    thread_id = str(uuid.uuid4())
    config = {"configurable": {"thread_id": thread_id}}

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit"):
            print("Goodbye!")
            break
        if not user_input:
            continue

        result = app.invoke(
            {"messages": [{"role": "user", "content": user_input}]},
            config=config,
        )
        reply = result["messages"][-1].content
        print(f"Coach: {reply}\n")


if __name__ == "__main__":
    main()
