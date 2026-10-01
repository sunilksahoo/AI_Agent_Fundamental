#!/usr/bin/env python3
"""Task 4: Extract the assistant's text from a chat completion response."""

import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise SystemExit(
        "OPENAI_API_KEY is not set. Set it in your terminal before running this script."
    )
if api_key != api_key.strip() or "\n" in api_key or "\r" in api_key:
    raise SystemExit(
        "OPENAI_API_KEY contains whitespace or a line break. Set it again as one line, then rerun."
    )

client = OpenAI(
    api_key=api_key,
    base_url=os.getenv("OPENAI_API_BASE"),
)

question = "What is Python in one sentence?"

# This sends a real API request. Model usage may incur charges.
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": question}],
)

# Chat Completions response path: response -> choices -> first choice -> message -> content
ai_text = response.choices[0].message.content

print("🎯 Successfully extracted the AI's response!")
print("\n" + "=" * 60)
print(f"Question: {question}")
print("\nAI's answer:")
print(ai_text)
print("=" * 60)
print("\nGolden path: response.choices[0].message.content")
