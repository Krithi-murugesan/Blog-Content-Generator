from crewai import Agent

def create_ideator_agent() -> Agent:
    return Agent(
        role="Topic Ideator",
        goal="Generate high-impact, SEO-friendly blog ideas",
        backstory="Expert content strategist skilled in SEO and audience intent.",
        verbose=True
    )
