"""
run_agent.py

Interactive CLI for the BMI agent. Unlike main.py (which calls the
BMISkill class directly with no LLM involved), this drives the skill
through a LangGraph tool-calling agent: you type natural language, the
agent decides whether/how to call `bmi_tool`, and replies in natural
language.

Usage:
    export OPENAI_API_KEY=sk-...
    python run_agent.py
"""

import uuid

from dotenv import load_dotenv

from agent import build_agent

load_dotenv()  # loads OPENAI_API_KEY from a local .env file, if present


def main():
    print("=== BMI Agent (LangGraph) ===")
    print("Ask me about your BMI in plain English. Type 'quit' to exit.\n")

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
        print(f"Agent: {reply}\n")


if __name__ == "__main__":
    main()
    
# You: I weigh 70kg and I'm 1.75m tall, what's my BMI?
# user "python3.10.12.genai" 
