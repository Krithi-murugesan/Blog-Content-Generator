from crewai import Task
from agents.editor import create_editor_agent

def create_edit_task() -> Task:
    return Task(
        description=(
            "Edit the blog draft for clarity, tone, flow, and SEO optimization. "
            "Deliver a polished, publication-ready markdown post."
        ),
        expected_output="Final SEO-optimized blog post in markdown.",
        agent=create_editor_agent()
    )
