#!/usr/bin/env python3
"""
Task 1: OpenAI SDK vs LangChain - See the Difference!
Compare the complexity of raw OpenAI SDK with LangChain's clean abstraction.

Learning Goal: Understand why LangChain simplifies AI development.
"""

import os
from pathlib import Path

import openai


MARKERS_DIR = Path(__file__).resolve().parent / "markers"


def raw_openai_approach(api_key, base_url):
    """Raw OpenAI SDK - complex and verbose"""
    print("\n🔴 RAW OPENAI SDK APPROACH")

    # TODO 1: Create OpenAI client
    client = openai.OpenAI(
        api_key=api_key,
        base_url=base_url,
    )

    # TODO 2: Make API call (notice the complexity!)
    response = client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[
            {"role": "user", "content": "Explain machine learning in one sentence"}
        ]
    )

    # TODO 3: Extract text (notice nested structure)
    if response:
        text = response.choices[0].message.content
        print(f"Response: {text[:100]}...")
        return text

    return None

def langchain_approach(api_key, base_url):
    """LangChain - clean and simple"""
    print("\n🟢 LANGCHAIN APPROACH")

    from langchain_openai import ChatOpenAI

    # TODO 4: Initialize model (so simple!)
    llm = ChatOpenAI(
        model="gpt-5.6-luna",
        api_key=api_key,
        base_url=base_url,
    )

    # TODO 5: Make the call (one line!)
    response = llm.invoke("Explain machine learning in one sentence")

    if response:
        print(f"Response: {response.content[:100]}...")
        return response.content

    return None

def main():
    print("🎯 Task 1: OpenAI SDK vs LangChain Comparison")
    print("=" * 50)

    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        print("❌ OPENAI_API_KEY is not set. No API requests were sent.")
        print("   Follow the API key setup instructions in README.md, then rerun this script.")
        return 1

    base_url = os.getenv("OPENAI_API_BASE", "").strip() or None

    try:
        # Run both approaches
        raw_result = raw_openai_approach(api_key, base_url)
        langchain_result = langchain_approach(api_key, base_url)
    except openai.AuthenticationError:
        print("❌ OpenAI rejected the API key (invalid_api_key). No key value was printed.")
        print("   Create or copy a valid API key from your OpenAI Platform account.")
        print("   Then enter it again in this terminal, without quotes or extra spaces.")
        if base_url:
            print("   You have a custom OPENAI_API_BASE set; confirm the key belongs to that endpoint.")
        return 1

    # Show the difference
    if raw_result and langchain_result:
        print("\n📊 COMPARISON:")
        print("✅ Both approaches work, but LangChain is:")
        print("  - 70% less code")
        print("  - Cleaner response handling")
        print("  - Provider agnostic")

        # Create marker
        MARKERS_DIR.mkdir(parents=True, exist_ok=True)
        with (MARKERS_DIR / "task1_complete.txt").open("w") as f:
            f.write("COMPLETED")
        print("\n✅ Task 1 completed!")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
