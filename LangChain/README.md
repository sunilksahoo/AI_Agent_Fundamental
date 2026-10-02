# LangChain Lab

This folder contains the LangChain environment verifier and its dependencies. Use a Python 3.10 or newer virtual environment for this project. The steps below use Python 3.12, which is installed on this machine.

## Set up the environment

From the repository root, run:

```bash
cd LangChain
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The `LangChain/.venv` environment is separate from the one in `OpenAI_Import_Setup`.

## Verify the environment

With the virtual environment active, run:

```bash
python verify_environment.py
```

The verifier checks the Python version, required packages, and OpenAI environment variables. It creates `LangChain/code` and `LangChain/markers` if they do not exist. If all required packages are available, it writes `VERIFIED` to `LangChain/markers/environment_verified.txt`.

The verifier does not make an API request, so an API key is not needed to run it.

## Configure the OpenAI API key

Tasks that make API requests need an `OPENAI_API_KEY`. Enter it in the same terminal window where you will run the task. The prompt intentionally hides what you type or paste; paste the key and press Return.

For zsh:

```zsh
read -s "OPENAI_API_KEY?Paste API key: "
echo
export OPENAI_API_KEY
```

For bash:

```bash
read -s -p "Paste API key: " OPENAI_API_KEY
echo
export OPENAI_API_KEY
```

To confirm the key was loaded without displaying it:

```bash
python -c 'import os; print("OPENAI_API_KEY is set" if os.getenv("OPENAI_API_KEY") else "OPENAI_API_KEY is missing")'
```

If you use a compatible custom endpoint, set `OPENAI_API_BASE` in the same terminal session:

```bash
export OPENAI_API_BASE="https://your-endpoint.example/v1"
```

Do not put API keys in source files or commit them to Git.

If a task reports `invalid_api_key`, create or copy a valid API key from your OpenAI Platform account and enter it again in the same terminal session. The task strips accidental leading or trailing whitespace, but it cannot repair a revoked, mistyped, or incorrect key. Never paste the key into chat or source code.

If you are using the default OpenAI endpoint, clear any custom endpoint setting before rerunning:

```bash
unset OPENAI_API_BASE
```

## Configure Task 2 provider keys

Task 2 calls each provider's own API. `OPENAI_API_BASE` only configures the OpenAI model; an OpenAI key and OpenAI endpoint cannot authenticate Gemini or Grok requests. Create API keys with Google AI Studio and xAI, then load them in the same terminal session (do not paste keys into source files or chat):

```zsh
read -s "GOOGLE_API_KEY?Paste Google AI Studio API key: "
echo
export GOOGLE_API_KEY
read -s "XAI_API_KEY?Paste xAI API key: "
echo
export XAI_API_KEY
```

Install the Task 2 provider integrations after updating requirements:

```bash
python -m pip install -r requirements.txt
```

The current script uses OpenAI and Gemini through their native LangChain integrations. The X.AI setup is included but commented out; uncomment it and set `XAI_API_KEY` if you want to include Grok.

## Run Task 1: OpenAI SDK vs. LangChain

**Raw OpenAI SDK:**

1. Line 22: create the OpenAI client using the API key and optional base URL passed into the function.
2. Lines 29–34: call the model `gpt-5.6-luna` with the `user` role and the machine-learning question.
3. Line 38: extract the response text from `response.choices[0].message.content`.

**LangChain:**

4. Lines 50–55: initialize `ChatOpenAI` with the model, API key, and optional base URL.
5. Line 58: invoke the model with the same question.

The current script already has these values filled in. The two approaches make separate requests, so their generated answers may differ.

After creating the virtual environment and setting a valid `OPENAI_API_KEY` in the current terminal session, run:

```bash
cd LangChain
source .venv/bin/activate
python task_1_openai_vs_langchain.py
```

The script sends two API requests to compare the OpenAI SDK with LangChain, so API usage may incur charges. It saves `LangChain/markers/task1_complete.txt` when both requests succeed. If the key is missing, the script reports that without sending requests; if OpenAI rejects it, confirm that it is a valid, active API key.

### Task 2: Multi-Model A/B Testing

`task_2_multi_model.py` sends the same prompt to OpenAI and Google Gemini and prints each response. It writes a completion marker to `LangChain/markers/task2_complete.txt` after both calls succeed. Set `OPENAI_API_KEY` and `GOOGLE_API_KEY` in the terminal first, as described above.

Run it from the repository root:

```bash
cd LangChain
source .venv/bin/activate
python task_2_multi_model.py
```

The script currently uses `gpt-5.6-luna` and `gemini-3.8-flash`. It uses separate provider integrations, so `OPENAI_API_BASE` does not configure Gemini. API calls may incur charges.

To compare alternative models (`gpt-4.1-mini` and `gemini-3.7-flash`) with the same API keys, run:

```bash
python task_2_multi_model_alternative.py
```

This creates `LangChain/markers/task2_alternative_complete.txt` after both model calls succeed. A custom `OPENAI_API_BASE` must support `gpt-4.1-mini`.

**What is Multi-Model Support?**

**Definition:** The ability to switch between AI providers (OpenAI, Google, X.AI) using the same code interface—no rewrites needed!

Think of it like USB ports: the same interface, different devices. LangChain is your universal adapter for AI models.

**The Real-World Problem**

Your boss: “We're spending $50K/month on OpenAI. Can we use something cheaper?”

You: “Give me 2 minutes. I'll test 3 providers right now!”

**What You'll Test:**

- **OpenAI GPT-4:** The industry standard ($$$)
- **Google Gemini:** 3x cheaper, just as good? ($$)
- **X.AI Grok:** 2x faster responses ($)

**Pro Tip:** Companies save 40% on average by finding the right model mix. Some use GPT-4 for complex tasks, Gemini for simple queries!

### Task 3: Template Magic

**What are Prompt Templates?**

**Definition:** Reusable prompt blueprints with `{placeholders}` that get filled dynamically—like f-strings for AI prompts.

Think of them like Mad Libs for AI—same structure, different words each time!

**The Copy-Paste Nightmare**

Without templates, you'd end up with dozens of near-identical prompt strings scattered across your codebase. Changing one word means editing every file.

**One Template to Rule Them All**

A single template with variables can be reused with different values every time. See the Solution tab for an example.

**Real Impact:** Uber reduced their prompt maintenance time by 85% using templates. One template update updates thousands of prompts!

### Task 4: AI Text to Clean Data

**What are Output Parsers?**

**Definition:** Tools that transform unstructured AI text into structured Python data (lists, dicts, objects) your code can actually use.

It's like having a translator between human-readable AI responses and computer-friendly data structures.

**The Problem Every Developer Faces**

AI: "The benefits are improved efficiency, cost savings, and better scalability."

Your code needs a list, but all it has is a string.

**LangChain Parsers to the Rescue**

A list parser converts AI text directly into a Python list, and a JSON parser converts it into a structured dictionary. See the Solution tab for an example.

**Fun Fact:** Spotify uses output parsers to extract song recommendations from AI, processing 10,000+ requests per minute!

### Task 5: The Magic Pipe Operator

**What is Chain Composition?**

**Definition:** Connecting LangChain components with the `|` operator to create data pipelines—like Unix pipes for AI.

Each component does ONE thing perfectly. Chain them together to build complex AI workflows!

**From Chaos to Elegance**

Without chains, you manually pass data between four separate steps and variables. With chains, the same pipeline collapses into a single line using the `|` operator. See the Solution tab for a comparison.

**The Power of |**

Just like Unix pipes, data flows left to right through as many components as you need—each one doing a single job well.

**Master Move:** Amazon's recommendation engine uses 50+ chained components. Each team owns different parts, but they all connect with `|`.

## Congratulations!

**You've Mastered:**

- Provider abstraction with LangChain
- Switching between AI providers instantly
- Creating reusable prompt templates
- Parsing AI responses into structured data
- Building chains with the pipe operator
- Writing 70% less code than vanilla OpenAI

**Key Takeaway:** `prompt | llm | parser`

One interface, any provider—no vendor lock-in!

## Resume work later

From the repository root, activate this project's environment again:

```bash
cd LangChain
source .venv/bin/activate
```

When you are finished, leave the virtual environment with:

```bash
deactivate
```
