#!/usr/bin/env python3
"""Run the Task 2 comparison with alternative OpenAI and Gemini models."""

import os
from pathlib import Path

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

MARKERS_DIR = Path(__file__).resolve().parent / "markers"


def response_text(content):
    """Return readable text from either plain or block-based model content."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(
            block.get("text", "")
            for block in content
            if isinstance(block, dict) and block.get("type") == "text"
        )
    return str(content)


def main():
    print("🎯 Task 2: Alternative Model Comparison")
    print("=" * 50)

    provider_keys = {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "GOOGLE_API_KEY": os.getenv("GOOGLE_API_KEY"),
    }
    missing_keys = [name for name, value in provider_keys.items() if not value]
    if missing_keys:
        print("❌ Missing provider API key(s): " + ", ".join(missing_keys))
        print("   Set these keys in this terminal session, then rerun.")
        return

    print("Setting up OpenAI GPT-4.1-mini...")
    openai_llm = ChatOpenAI(
        model="gpt-4.1-mini",
        api_key=provider_keys["OPENAI_API_KEY"],
        base_url=os.getenv("OPENAI_API_BASE") or None,
    )

    print("Setting up Google Gemini 3.7 Flash...")
    google_llm = ChatGoogleGenerativeAI(
        model="gemini-3.7-flash",
        google_api_key=provider_keys["GOOGLE_API_KEY"],
    )

    prompt = "Explain cloud computing in one sentence"
    print(f"\n📝 Prompt: '{prompt}'\n")

    response = openai_llm.invoke(prompt)
    print(f"OpenAI (GPT-4.1-mini): {response_text(response.content)}")

    response = google_llm.invoke(prompt)
    print(f"Google (Gemini 3.7 Flash): {response_text(response.content)}")
    print("ℹ️ The Google SDK notice above is informational; Gemini returned a response.")

    MARKERS_DIR.mkdir(parents=True, exist_ok=True)
    (MARKERS_DIR / "task2_alternative_complete.txt").write_text("COMPLETED")
    print("\n✅ Alternative model comparison completed!")


if __name__ == "__main__":
    main()
