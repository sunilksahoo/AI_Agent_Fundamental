#!/usr/bin/env python3
"""Task 3: Send a message to an OpenAI model and print its reply."""

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

# This sends a real API request. Model usage may incur charges.
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": "Hello AI, please introduce yourself in one sentence.",
        }
    ],
)

ai_text = response.choices[0].message.content
print("✅ API call successful!")
print(f"\n🤖 AI said: {ai_text}")
print(f"\n📊 Total tokens used: {response.usage.total_tokens}")
