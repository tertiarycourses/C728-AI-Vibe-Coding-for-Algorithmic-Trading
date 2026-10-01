DOMAIN4 = [{'build': 'training-grid.csv and holdout.json',
  'desc': 'Use AI to build and review optimise without leaking the future; demonstrate the result '
          'with executable evidence.',
  'num': 7,
  'objective': 'LO4: Validate parameters chronologically and operate a monitored paper-trading '
               'workflow.',
  'services': 'Python · AI coding assistant · synthetic dataset',
  'steps': [('Read the complete procedure in the lab README.', ''),
            ('Generate, review and verify a candidate against the checkpoint.',
             'python labs/lab-07-optimisation/sample.py')],
  'test': '9 training candidates and 252 holdout observations',
  'title': 'Optimise without leaking the future',
  'topic': 4},
 {'build': 'events.jsonl',
  'desc': 'Use AI to build and review broker api and monitored paper bot; demonstrate the result '
          'with executable evidence.',
  'num': 8,
  'objective': 'LO4: Validate parameters chronologically and operate a monitored paper-trading '
               'workflow.',
  'services': 'Python · AI coding assistant · synthetic dataset',
  'steps': [('Read the complete procedure in the lab README.', ''),
            ('Generate, review and verify a candidate against the checkpoint.',
             'python labs/lab-08-paper-bot/sample.py')],
  'test': 'duplicate, stale-data, exposure-limit and halt events blocked',
  'title': 'Broker API and monitored paper bot',
  'topic': 4}]
