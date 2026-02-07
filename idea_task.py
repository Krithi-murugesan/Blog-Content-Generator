from crewai import Task
from agents.ideator import create_ideator_agent

def create_idea_task(topic: str) -> Task:
    return Task(
        description=(
            f"Generate 5 SEO-friendly blog ideas for '{topic}'. "
            "Each should include a title and brief description."
        ),
        expected_output="List of blog ideas with titles and descriptions.",
        agent=create_ideator_agent()
    )
