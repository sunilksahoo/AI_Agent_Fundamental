# Master Prompt Engineering with LangChain

**The Problem:** Your AI gives vague, unhelpful responses. Different results every time. Not following your instructions properly…

**The Solution:** Master 4 powerful prompting techniques! Control AI behavior like a pro with zero-shot, one-shot, few-shot, and chain-of-thought prompting.

**What You'll Learn:**

- Zero-shot prompting - Direct commands without examples
- One-shot prompting - Learning from a single example
- Few-shot prompting - Multiple examples for consistency
- Chain-of-thought - Step-by-step reasoning
- Compare techniques side-by-side

**Did You Know?** GitHub Copilot uses few-shot prompting to generate code, while ChatGPT uses chain-of-thought for complex math problems!

## Set up the environment

This lab uses LangChain with its OpenAI integration. Use Python 3.10 or newer; Python 3.12 is recommended.

From the repository root, create and activate a virtual environment, then install the packages:

```bash
cd Prompt_Engineering_with_LangChain
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The environment verifier also makes an OpenAI API request. Set `OPENAI_API_KEY` in the same terminal session before running it. `OPENAI_API_BASE` is optional and is only needed when using a custom OpenAI-compatible endpoint. Do not put API keys in source files or commit them to Git.

For zsh, enter the key without displaying it:

```zsh
read -s "OPENAI_API_KEY?Paste API key: "
echo
export OPENAI_API_KEY
# Optional: set this only when using a custom OpenAI-compatible endpoint.
# export OPENAI_API_BASE="https://your-endpoint.example/v1"
```

## Environment Verification

Verify your prompt engineering lab setup before starting the tasks.

**Script:** `verify_environment.py`

This script checks:

- LangChain and langchain-openai packages
- OpenAI API key and optional base URL configuration
- Prompt template utilities
- Creation of a verification marker

With the virtual environment active and `OPENAI_API_KEY` set, open a terminal in `Prompt_Engineering_with_LangChain` and run:

```bash
python verify_environment.py
```

## Task 1: Zero-Shot Prompting (2 minutes)

**What is Zero-Shot Prompting?**

**Definition:** Asking the AI to perform a task without providing any examples—like asking a chef to cook without showing them a recipe. The AI relies entirely on its pre-trained knowledge and your instructions.

**The Problem with Vague Prompts**

A prompt like `"write a policy"` is too vague—it produces a generic, unhelpful response.

**The Power of Specific Prompts**

A prompt like `"Write a 200-word GDPR-compliant data privacy policy for European customers with 30-day retention period"` produces a targeted, useful result.

**Real Impact:** Anthropic found that specific zero-shot prompts improved response accuracy by 73% over vague requests!

## Task 2: One-Shot Prompting

**What is One-Shot Prompting?**

**Definition:** Providing one example for the AI to follow—like showing a chef one dish before asking them to cook something similar. The AI learns your format, style, and structure from a single example.

**The Magic of Examples**

Show the AI your company's policy format once, and it will replicate it for new policies. For example, a REFUND POLICY with 5 numbered sections becomes a REMOTE WORK POLICY with the same 5 sections!

**Pro Tip:** Amazon uses one-shot prompting for product descriptions—one example ensures thousands of listings follow the same format!

## Task 3: Few-Shot Prompting

**What is Few-Shot Prompting?**

**Definition:** Providing multiple examples to teach consistent patterns—like training a chef with several dishes before they create their own. The AI learns nuanced patterns, tone, and style from diverse examples.

**Why Multiple Examples Matter**

- Learn tone: professional yet friendly
- Learn structure: consistent formatting
- Learn patterns: how to handle different scenarios

**Real Impact:** GitHub Copilot uses few-shot learning from your codebase to generate contextually relevant code suggestions!

## Task 4: Chain-of-Thought Prompting

**What is Chain-of-Thought Prompting?**

**Definition:** Guiding the AI through step-by-step reasoning—like teaching a chef to plan a meal from ingredients to plating. The AI breaks down complex problems into manageable steps.

**The Power of Structured Thinking**

Without chain-of-thought, a prompt like "Fix the policy" produces a vague response. With chain-of-thought, working through Step 1, Step 2, and Step 3 produces a comprehensive solution!

## Task 5: Technique Showdown

**The Ultimate Comparison**

Test all 4 techniques on the same problem to see which works best!

**Head-to-Head Battle**

- **Zero-Shot:** Quick and general
- **One-Shot:** Format consistency
- **Few-Shot:** Style and tone mastery
- **Chain-of-Thought:** Complex reasoning

**Key Insight:** Different techniques for different tasks—now you'll know exactly when to use each one!

## Congratulations!

**You've Mastered:**

- Zero-Shot Prompting for direct instructions
- One-Shot Prompting for format teaching
- Few-Shot Prompting for consistent style
- Chain-of-Thought for complex reasoning
- Choosing the right technique for each task
- Writing prompts that get perfect responses

**Key Takeaway:** Right technique = 10x better results. Zero-shot for quick, few-shot for style, chain-of-thought for reasoning!
