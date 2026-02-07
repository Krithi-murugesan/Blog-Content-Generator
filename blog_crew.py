from crewai import Crew
from tasks.idea_task import create_idea_task
from tasks.draft_task import create_draft_task
from tasks.edit_task import create_edit_task

def build_blog_crew(topic: str) -> Crew:
    idea_task = create_idea_task(topic)
    draft_task = create_draft_task()
    edit_task = create_edit_task()

    return Crew(
        agents=[
            idea_task.agent,
            draft_task.agent,
            edit_task.agent
        ],
        tasks=[
            idea_task,
            draft_task,
            edit_task
        ],
        process="sequential",
        verbose=True
    )
