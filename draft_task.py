from crewai import Task
from agents.writer import create_writer_agent

def create_draft_task() -> Task:
    return Task(
        description=(
            "Choose the best blog idea and write a full blog post draft in markdown. "
            "Include title, intro, headings, subheadings, and conclusion."
        ),
        expected_output="Complete blog draft in markdown format.",
        agent=create_writer_agent()
    )
