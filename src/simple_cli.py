"""Simple CLI demo for mama-ai prototype."""

from src.model import predict_text


def run_cli():
    print("mama-ai prototype running (CLI demo)")
    while True:
        try:
            text = input("Enter text (or 'quit'): ").strip()
        except EOFError:
            break
        if text.lower() in {"q", "quit", "exit"}:
            break
        if not text:
            continue
        result = predict_text(text)
        print(f"[{result['backend']}] {result['label']} ({result['score']:.3f})")
