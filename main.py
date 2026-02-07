import argparse
import os
from core.config import Settings
from core.logging import get_logger
from crew.blog_crew import build_blog_crew

logger = get_logger("BlogGenerator")

def run(topic: str):
    Settings.validate()
    crew = build_blog_crew(topic)

    logger.info(f"Starting blog generation for topic: {topic}")
    result = crew.kickoff()

    os.makedirs(Settings.OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(Settings.OUTPUT_DIR, "final_blog.md")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result[-1])

    logger.info(f"Blog successfully generated at {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Blog Content Generator using CrewAI")
    parser.add_argument("--topic", required=True, help="Topic for blog generation")
    args = parser.parse_args()

    run(args.topic)
