# OpenAI Python setup: Task 1

This folder is a portable starting point based on `First_AI_API_Call/task_1_import_setup.py`.
Task 1 only imports the SDK; it does not send an API request or need an API key.

## 1. Create and activate a virtual environment

From the project root in Terminal:

```bash
cd OpenAI_Import_Setup
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Install the OpenAI Python package

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 3. Run Task 1

```bash
python task_1_import_setup.py
```

You should see a success message and the installed SDK version. Keep the virtual
environment active for later tasks. When you return to this project, activate it
again with `source .venv/bin/activate`.

## Next: API key

You do not need a key for Task 1. Later tasks that make API requests need an API
key set as `OPENAI_API_KEY`; avoid putting the key directly in a Python file or
committing it to source control.

## Task 2: Initialize the client

After creating a replacement API key, enter it without displaying it in
Terminal. In the macOS default shell (zsh), run this and paste the key at the
prompt, then press Return:

```bash
read -s "OPENAI_API_KEY?Paste API key: "; export OPENAI_API_KEY; echo
```

This keeps the key out of the visible command and avoids accidentally adding a
line break inside the value. Do not paste the key into chat or commit it to the
project.

If you use a compatible custom endpoint, you can also set
`OPENAI_API_BASE="https://your-endpoint.example/v1"`. Otherwise, the SDK uses
OpenAI's default endpoint. Then run:

```bash
python task_2_client_initialization.py
```

This initializes a client but does not send an API request. The key stays out of
the script and is not printed.

## Task 3: Make an API call

With the virtual environment active and `OPENAI_API_KEY` set in the same
Terminal session, run:

```bash
python task_3_api_call_explained.py
```

This sends a real request using `gpt-4.1-mini`; API usage may incur charges.
The script prints the model's reply and the total token count.

## Task 4: Extract the response

Run this with the virtual environment active and `OPENAI_API_KEY` set:

```bash
python task_4_extract_response.py
```

It makes another API request, then extracts the answer from
`response.choices[0].message.content`. API usage may incur charges.

## Task 5: Inspect tokens and estimate cost

Run this with the virtual environment active and `OPENAI_API_KEY` set:

```bash
python task_5_tokens_and_costs.py
```

It makes a real API request, reads the input, output, and total token counts,
then estimates the standard text token cost for `gpt-4.1-mini`. Actual charges
can differ, including when cached input applies; check the [current API pricing](https://developers.openai.com/api/docs/pricing).
