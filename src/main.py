"""Entry point for mama-ai.

For now this just runs a simple placeholder that you can swap with
CLI, FastAPI, or Streamlit entrypoints.
"""

from .simple_cli import run_cli


if __name__ == "__main__":
    run_cli()
