from crewai import Agent

def create_editor_agent() -> Agent:
    return Agent(
        role="Editor",
        goal="Improve clarity, tone, structure, and SEO quality",
        backstory="Senior editor refining drafts into publication-ready content.",
        verbose=True
    )
