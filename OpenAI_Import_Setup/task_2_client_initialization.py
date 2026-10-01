#!/usr/bin/env python3
"""Task 2: Initialize an OpenAI client using environment variables."""

import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise SystemExit(
        "OPENAI_API_KEY is not set. Set it in your terminal, then run this script again."
    )

# OPENAI_API_BASE is optional. Leave it unset to use OpenAI's default endpoint.
client = OpenAI(
    api_key=api_key,
    base_url=os.getenv("OPENAI_API_BASE"),
)

print("✅ Step 2 complete: OpenAI client initialized!")
print("- API key: configured (value hidden)")
print(f"- Base URL: {os.getenv('OPENAI_API_BASE') or 'OpenAI default'}")
