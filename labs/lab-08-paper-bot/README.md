# Lab 08 — Broker API and monitored paper bot

**C728 · v1.0 · 75 minutes · Topic 4**

## Goal
Duplicate, stale-data, exposure-limit and halt events blocked.

## What you'll build
events.jsonl. A reviewed AI candidate and a runnable sample checkpoint.

## Prerequisites
Complete environment setup in the LG. Basic Python and finance. Earlier labs supply context, but sample.py rebuilds its required data independently. Run all commands from the repository root.

## Steps
1. Open labs/lab-08-paper-bot/prompt.md in your chosen assistant. Read the contract before submitting it; ask the assistant to plan first. Review any file or command access it requests. Use the same prompt in Cursor chat, Copilot chat or Claude; interface labels may differ.
2. Ask the assistant to create generated.py in this lab folder. Open its proposed code in your editor and trace the data input, signal timing, output path and assertions. Compare the function interfaces with labs/trading_core.py. Do not overwrite sample.py.
3. Run the supplied checkpoint and retain its console output. It supplies a recovery path if your AI candidate is incomplete.
```bash
python labs/lab-08-paper-bot/sample.py
```
4. Open the output files in this lab folder. Check duplicate, stale-data, exposure-limit and halt events blocked. Record the observed result in notes.md. A successful process exit alone does not establish correct strategy behaviour.
5. Run your reviewed AI candidate and compare it with the checkpoint. If an import fails, ensure it inserts the parent labs directory into sys.path as sample.py does. Include the sanitised traceback and a small fixture in the refinement prompt, then inspect and rerun the proposed correction.
```bash
python labs/lab-08-paper-bot/generated.py
```
6. Explain one change to a partner and save your accepted code plus notes. Record data source, seed, parameters and cost convention. Do not tune parameters using holdout results. Continue to the next checkpoint even if your candidate needs more work.

## Test it
Expected: duplicate, stale-data, exposure-limit and halt events blocked. Output: events.jsonl. Compare your candidate's output with the sample on the same input; numerical differences must be explained.

## Troubleshooting
- ModuleNotFoundError: activate the virtual environment and run python -m pip install -r requirements.txt from the repository root.
- No output where expected: inspect this lab folder, not the terminal's working directory; scripts resolve paths from __file__.
- Assertion fails after an AI edit: revert the smallest change, reproduce with the supplied fixture, then request a focused correction.

## Challenge
Add one independent edge-case fixture relevant to this lab and explain its expected behaviour before running it.

## Reflection
What evidence would convince you that the AI-generated change preserved the intended trading logic?

## Optional broker connection
Use an Alpaca paper-only account. Set APCA_API_KEY_ID and APCA_API_SECRET_KEY privately in your terminal, then run python labs/lab-08-paper-bot/sample.py --paper-account. It performs only GET /v2/account on https://paper-api.alpaca.markets; no order request is made. Never paste keys into prompts or notes. The offline adapter tests order intents and controls; it does not simulate exchange fills. Paper fills omit some real-market effects: https://docs.alpaca.markets/us/docs/paper-trading.
