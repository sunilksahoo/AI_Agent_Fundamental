#!/usr/bin/env python3
"""Task 5: Inspect token usage and estimate the text API cost."""

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

prompt = "Explain one benefit of using AI for customer support in a business."

# This sends a real API request. Model usage may incur charges.
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": prompt}],
)

# Token counts are provided by the API response.
input_tokens = response.usage.prompt_tokens
output_tokens = response.usage.completion_tokens
total_tokens = response.usage.total_tokens

print("📊 Token usage report:")
print("=" * 50)
print(f"  Your prompt used: {input_tokens} tokens")
print(f"  AI response used: {output_tokens} tokens")
print(f"  Total tokens:     {total_tokens} tokens")
print("=" * 50)

# GPT-4.1 mini standard text pricing: $0.40/M input and $1.60/M output.
# Convert those rates to dollars per 1,000 tokens for the calculation below.
input_price_per_1k = 0.0004
output_price_per_1k = 0.0016

input_cost = input_tokens / 1000 * input_price_per_1k
output_cost = output_tokens / 1000 * output_price_per_1k
estimated_cost = input_cost + output_cost

print("\n💰 Estimated cost for this call:")
print("-" * 50)
print(f"  Input:  ${input_cost:.8f} ({input_tokens} tokens)")
print(f"  Output: ${output_cost:.8f} ({output_tokens} tokens)")
print(f"  Total:  ${estimated_cost:.8f}")
print("-" * 50)
print("Estimate assumes standard, uncached text token rates.")
print("Check current rates: https://developers.openai.com/api/docs/pricing")
