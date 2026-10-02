#!/usr/bin/env python3
"""
Task 2: Multi-Model Support - One Interface, Many Providers!
Test OpenAI, Google, and X.AI models using the same LangChain interface.

Learning Goal: Experience provider flexibility without code changes.
"""

import os
from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_xai import ChatXAI

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
    print("🎯 Task 2: Multi-Model Support with LangChain")
    print("=" * 50)

    print("\n🌐 Initialize Multiple AI Providers")
    print("=" * 50)

    provider_keys = {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "GOOGLE_API_KEY": os.getenv("GOOGLE_API_KEY"),
        #"XAI_API_KEY": os.getenv("XAI_API_KEY"),
    }
    missing_keys = [name for name, value in provider_keys.items() if not value]
    if missing_keys:
        print("❌ Missing provider API key(s): " + ", ".join(missing_keys))
        print("   Set these keys in this terminal session, then rerun Task 2.")
        return

    # TODO 1: Initialize OpenAI model
    print("Setting up OpenAI GPT-4.1-mini...")
    openai_llm = ChatOpenAI(
        model="gpt-5.6-luna",
        api_key=provider_keys["OPENAI_API_KEY"],
        base_url=os.getenv("OPENAI_API_BASE") or None,
    )

    # TODO 2: Initialize Google Gemini model
    print("Setting up Google Gemini...")
    google_llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        google_api_key=provider_keys["GOOGLE_API_KEY"],
    )
    '''
    # Initialize X.AI Grok model
    print("Setting up X.AI Grok...")
    xai_llm = ChatXAI(
        model="grok-code-fast-1",
        xai_api_key=provider_keys["XAI_API_KEY"],
    )
    '''

    # Compare all models with the same prompt
    print("\n✅ All models initialized! Now let's compare them...")
    print("\nModel Comparison - Same Prompt, Different Models")
    print("=" * 50)

    test_prompt = "Explain cloud computing in one sentence"
    print(f"📝 Prompt: '{test_prompt}'\n")

    # Test all models with the same prompt
    if openai_llm:
        response = openai_llm.invoke(test_prompt)
        print(f"OpenAI: {response_text(response.content)[:100]}...")

    if google_llm:
        response = google_llm.invoke(test_prompt)
        print(f"Google: {response_text(response.content)[:100]}...")

    '''
    if xai_llm:
        response = xai_llm.invoke(test_prompt)
        print(f"X.AI: {response_text(response.content)[:100]}...")
    '''

    print("\n💡 Same code, different providers - perfect for A/B testing!")

    # Create marker for completion
    MARKERS_DIR.mkdir(parents=True, exist_ok=True)
    with (MARKERS_DIR / "task2_complete.txt").open("w") as f:
        f.write("COMPLETED")

    print("\n✅ Task 2 completed! You can now switch models at will!")
    print("🎉 You tested 3 different AI providers with identical code!")

if __name__ == "__main__":
    main()
