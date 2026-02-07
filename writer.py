from crewai import Agent

def create_writer_agent() -> Agent:
    return Agent(
        role="Content Writer",
        goal="Write engaging and informative blog drafts",
        backstory="Professional writer who explains complex topics clearly.",
        verbose=True
    )
