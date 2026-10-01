# AI Vibe Coding for Algorithmic Trading

Use an AI pair programmer to build, review and validate reproducible Python trading research.

| Course detail | Information |
|---|---|
| Course code | `C728` |
| Programme | Non-WSQ commercial short course |
| Duration | 2 days / 15 instructional hours |
| Registration | [View course details and register](https://www.tertiarycourses.com.sg/ai-vibe-coding-for-algorithmic-trading.html) |
| Version | v1.0 · 1 October 2026 |

## About the course

Learn a controlled AI coding workflow for quantitative trading: specify the strategy, inspect generated Python, validate market data, build indicators, backtest with costs, interpret risk, and monitor paper-trading intents. Basic Python and finance knowledge are prerequisites.

## Learning outcomes

- Specify, generate and validate trading code with an AI assistant.
- Validate price data, visualise indicators and construct causal signals.
- Backtest with execution delay and costs, and interpret return and risk.
- Validate parameters chronologically and operate a monitored paper-trading workflow.

## Topics covered

1. Getting Started with AI Vibe Coding for Trading
2. Analysing Markets with AI
3. Building and Backtesting Strategies with AI
4. Automating and Running Trading with AI

## Labs

- [Lab 01 — Environment and AI workflow](labs/lab-01-environment/README.md) · [Python checkpoint](labs/lab-01-environment/sample.py) · [Prompt PDF](labs/lab-01-environment/Prompt.pdf)
- [Lab 02 — Fetch and validate price data](labs/lab-02-market-data/README.md) · [Python checkpoint](labs/lab-02-market-data/sample.py) · [Prompt PDF](labs/lab-02-market-data/Prompt.pdf)
- [Lab 03 — Indicators and visual evidence](labs/lab-03-indicators/README.md) · [Python checkpoint](labs/lab-03-indicators/sample.py) · [Prompt PDF](labs/lab-03-indicators/Prompt.pdf)
- [Lab 04 — Generate and debug trading signals](labs/lab-04-signals/README.md) · [Python checkpoint](labs/lab-04-signals/sample.py) · [Prompt PDF](labs/lab-04-signals/Prompt.pdf)
- [Lab 05 — Build a cost-aware backtest](labs/lab-05-backtest/README.md) · [Python checkpoint](labs/lab-05-backtest/sample.py) · [Prompt PDF](labs/lab-05-backtest/Prompt.pdf)
- [Lab 06 — Performance, risk and code review](labs/lab-06-risk-review/README.md) · [Python checkpoint](labs/lab-06-risk-review/sample.py) · [Prompt PDF](labs/lab-06-risk-review/Prompt.pdf)
- [Lab 07 — Optimise without leaking the future](labs/lab-07-optimisation/README.md) · [Python checkpoint](labs/lab-07-optimisation/sample.py) · [Prompt PDF](labs/lab-07-optimisation/Prompt.pdf)
- [Lab 08 — Broker API and monitored paper bot](labs/lab-08-paper-bot/README.md) · [Python checkpoint](labs/lab-08-paper-bot/sample.py) · [Prompt PDF](labs/lab-08-paper-bot/Prompt.pdf)

## Public package

- [C728-AI-Vibe-Coding-for-Algorithmic-Trading-v1.0.pdf](courseware/C728-AI-Vibe-Coding-for-Algorithmic-Trading-v1.0.pdf)
- [C728-AI-Vibe-Coding-for-Algorithmic-Trading-v1.0.pptx](courseware/C728-AI-Vibe-Coding-for-Algorithmic-Trading-v1.0.pptx)
- [LG-C728-AI-Vibe-Coding-for-Algorithmic-Trading.docx](courseware/LG-C728-AI-Vibe-Coding-for-Algorithmic-Trading.docx)
- [LG-C728-AI-Vibe-Coding-for-Algorithmic-Trading.pdf](courseware/LG-C728-AI-Vibe-Coding-for-Algorithmic-Trading.pdf)
- [LP-C728-AI-Vibe-Coding-for-Algorithmic-Trading.docx](courseware/LP-C728-AI-Vibe-Coding-for-Algorithmic-Trading.docx)
- [LP-C728-AI-Vibe-Coding-for-Algorithmic-Trading.pdf](courseware/LP-C728-AI-Vibe-Coding-for-Algorithmic-Trading.pdf)
- [Learner Guide Markdown](LG-C728-AI-Vibe-Coding-for-Algorithmic-Trading.md)

Each lab has its own folder with a Python checkpoint, AI prompt in Markdown and PDF, and detailed procedures. The Learner Guide mirrors those procedures; slides provide visual concepts and lab goals. Install [requirements.txt](requirements.txt) in a Python virtual environment before running samples. See the LG for complete setup and commands.

All core labs run offline on seeded synthetic observations. An optional read-only Alpaca paper-account connection uses private environment variables. The sample does not submit broker orders. Backtests use a simplified close-to-close exposure model; paper and live results can differ. This course teaches software research, not investment recommendations.

## Public and private distribution

The current deck, LP, LG and complete labs are public. `reference/` and `assessment/` are private and excluded, along with credentials, dependencies and superseded archives. There are no formal course assessment deliverables in this package. Never add broker credentials or personal account information to this repository.

## Sources and provider

Syllabus and duration: [official C728 course page](https://www.tertiarycourses.com.sg/ai-vibe-coding-for-algorithmic-trading.html). Technical references: [Python virtual environments](https://docs.python.org/3/library/venv.html), [Copilot best practices](https://docs.github.com/en/copilot/get-started/best-practices), and [Alpaca paper trading](https://docs.alpaca.markets/us/docs/paper-trading).

Provided by **Tertiary Infotech Academy Pte Ltd** · [Tertiary Courses](https://www.tertiarycourses.com.sg/).
