TITLE = 'AI Vibe Coding for Algorithmic Trading'
SHORT_TITLE = 'C728-AI-Vibe-Coding-for-Algorithmic-Trading'
COURSE_CODE = 'C728'
VERSION = 'v1.0'
VERSION_DATE = '1 October 2026'
ORG = 'Tertiary Infotech Academy Pte Ltd'
UEN = 'UEN: 201200696W'
TRAINER = 'Dr. Alfred Ang'
DAYS = 2
MODE = 'Instructor-led demonstrations, AI pair programming and hands-on labs'
COMPANY = 'Meridian Research (fictional)'
LAB_SLUGS = {1: 'environment',
 2: 'market-data',
 3: 'indicators',
 4: 'signals',
 5: 'backtest',
 6: 'risk-review',
 7: 'optimisation',
 8: 'paper-bot'}
LEARNING_OUTCOMES = ['LO1: Specify, generate and validate Python trading code with an AI assistant.',
 'LO2: Validate price data, visualise indicators and construct causal signals.',
 'LO3: Backtest with execution delay and costs, and interpret return and risk.',
 'LO4: Validate parameters chronologically and operate a monitored paper-trading workflow.']
LO_TITLES = ['Prompt and review', 'Data and signals', 'Backtest and risk', 'Validate and monitor']
TOPICS = [{'code': '01',
  'concepts': ['A trading rule must define instrument, timing, exposure and exit.',
               'AI generates candidates; humans own assumptions, tests and risk.',
               'A prompt contract states inputs, outputs, constraints and acceptance checks.',
               'Keep secrets and account data out of prompts and Git.'],
  'num': 1,
  'subtitle': 'Python environment · prompt contracts · data ingestion',
  'title': 'Getting Started with AI Vibe Coding for Trading'},
 {'code': '02',
  'concepts': ['Validate ordering, duplicate dates, missing prices and positive values.',
               'Rolling indicators use past and current observations only.',
               'A signal is a decision; a position is exposure after execution delay.',
               'Use charts and small examples to debug generated code.'],
  'num': 2,
  'subtitle': 'Price data · indicators · signals · AI debugging',
  'title': 'Analysing Markets with AI'},
 {'code': '03',
  'concepts': ['A backtest is an execution model, not a promise of profit.',
               'Lag close-derived signals by one bar for close-to-close return accounting.',
               'Turnover incurs transaction costs; compare with buy and hold.',
               'Sharpe and drawdown describe different risks.'],
  'num': 3,
  'subtitle': 'Strategy design · backtesting · performance · refactoring',
  'title': 'Building and Backtesting Strategies with AI'},
 {'code': '04',
  'concepts': ['Choose parameters on training data; reserve an untouched time holdout.',
               'Compare parameter neighbourhoods rather than one winning setting.',
               'A broker adapter separates research from order execution.',
               'Monitor stale data, duplicate requests, rejected orders and kill switches.'],
  'num': 4,
  'subtitle': 'Parameter validation · broker API · monitoring',
  'title': 'Automating and Running Trading with AI'}]
DAY_THEMES = {1: 'From prompt to validated signal', 2: 'From backtest to monitored paper bot'}
VERSION_HISTORY = [('1.0',
  '1 October 2026',
  'C728 adaptation of the private v10 reference: four topics, eight Python labs and AI prompt packs.',
  'Tertiary Infotech')]
LG_INTRO = ('Build a reproducible long-only moving-average research pipeline with an AI coding assistant. The fictional '
 'dataset is for software learning and does not represent an investable instrument. This guide contains the '
 'complete procedures; slides focus on concepts and visual evidence.')
LG_INTRO2 = ('Work from the repository root. Each lab includes a runnable reference checkpoint, so you can rejoin '
 'without completing previous edits. Generate your own candidate before consulting sample.py; compare '
 'behaviour rather than copying blindly.')
LG_SETUP = {'conventions': ['All commands run from the repository root. Each sample writes beside its own script.',
                 'Use generated.py for AI output so the supplied checkpoint remains available.',
                 'Never paste real credentials into an AI prompt. Optional paper keys belong only in '
                 'environment variables.'],
 'needs': ['Python 3.11 or newer; basic Python and finance knowledge.',
           'Cursor, GitHub Copilot or Claude access, or trainer-led shared demonstrations.',
           'Internet for optional CSV ingestion and broker account readback; all core labs run offline.'],
 'verify_code': 'python3 -m venv .venv\n'
                'source .venv/bin/activate\n'
                'python -m pip install -r requirements.txt\n'
                'python --version',
 'verify_text': 'Use Terminal on macOS/Linux or PowerShell on Windows. On Windows use python instead of '
                'python3 and .venv\\Scripts\\Activate.ps1 instead of source .venv/bin/activate.'}
LAB_NOTE = ('Each lab folder includes sample.py, prompt.md and Prompt.pdf. Detailed procedures are in this guide and '
 'its README.')
LG_NEXT_STEPS = ['Repeat the pipeline on an authorised price CSV and record its source, adjustment convention and timezone.',
 'Add a second strategy with independently specified rules and tests.',
 'Continue paper observation across different market conditions before considering any separate live '
 'implementation.']
LG_GLOSSARY = [('Look-ahead bias', 'Using information that was unavailable at the simulated decision time.'),
 ('Turnover', 'Absolute change in portfolio exposure.'),
 ('Drawdown', 'Equity divided by its running peak minus one.'),
 ('Holdout', 'Chronological observations excluded from parameter selection.'),
 ('Paper trading', 'Simulated orders; results differ from live execution.')]
COURSE_OVERVIEW = {'arc': ['Describe → generate → review → run → compare → refine'],
 'concepts': [('Contract', 'State data, timing and acceptance checks.'),
              ('Evidence', 'Run checks and inspect charts.'),
              ('Risk', 'Model costs and exposure limits.'),
              ('Control', 'Paper mode and observable failures.')],
 'concepts_title': 'Own the logic',
 'framework': [('Specify', 'Describe the smallest useful change.'),
               ('Generate', 'Ask for a plan and focused code.'),
               ('Inspect', 'Read assumptions and data access.'),
               ('Verify', 'Run known-result tests before accepting.')],
 'framework_title': 'The AI review loop',
 'section_title': 'Research before execution',
 'statement': {'body': 'Demand causal signals, reproducible inputs and visible failure handling.',
               'headline': 'A plausible chart is not proof.',
               'kicker': 'RESEARCH DISCIPLINE'}}
SCHEDULE = {1: ('From prompt to validated signal',
     [('09:00', '09:20', 20, 'admin', 'Welcome and AI review briefing'),
      ('09:20', '10:00', 40, 'topic', 'Topic 1: Getting Started with AI Vibe Coding for Trading'),
      ('10:00', '10:45', 45, 'lab', 'Lab 1: Environment and AI workflow'),
      ('10:45', '11:00', 15, 'break', 'Tea break'),
      ('11:00', '12:15', 75, 'lab', 'Lab 2: Fetch and validate price data'),
      ('12:15', '12:45', 30, 'topic', 'Topic 2: Analysing Markets with AI'),
      ('12:45', '13:45', 60, 'lunch', 'Lunch'),
      ('13:45', '14:15', 30, 'topic', 'Visual demonstration and code review'),
      ('14:15', '15:30', 75, 'lab', 'Lab 3: Indicators and visual evidence'),
      ('15:30', '15:45', 15, 'break', 'Tea break'),
      ('15:45', '17:00', 75, 'lab', 'Lab 4: Generate and debug trading signals'),
      ('17:00',
       '18:00',
       60,
       'recap',
       'Learning reinforcement: compare evidence, peer review, extension and recap')]),
 2: ('From backtest to monitored paper bot',
     [('09:00', '09:20', 20, 'admin', 'Day 1 retrieval and checkpoint recovery'),
      ('09:20', '10:00', 40, 'topic', 'Topic 3: Building and Backtesting Strategies with AI'),
      ('10:00', '10:45', 45, 'lab', 'Lab 5: Build a cost-aware backtest'),
      ('10:45', '11:00', 15, 'break', 'Tea break'),
      ('11:00', '12:15', 75, 'lab', 'Lab 6: Performance, risk and code review'),
      ('12:15', '12:45', 30, 'topic', 'Topic 4: Automating and Running Trading with AI'),
      ('12:45', '13:45', 60, 'lunch', 'Lunch'),
      ('13:45', '14:15', 30, 'topic', 'Visual demonstration and code review'),
      ('14:15', '15:30', 75, 'lab', 'Lab 7: Optimise without leaking the future'),
      ('15:30', '15:45', 15, 'break', 'Tea break'),
      ('15:45', '17:00', 75, 'lab', 'Lab 8: Broker API and monitored paper bot'),
      ('17:00',
       '18:00',
       60,
       'recap',
       'Learning reinforcement: compare evidence, peer review, extension and recap')])}
