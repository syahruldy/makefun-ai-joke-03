# Development log

## 2026-11-13 evening (WIB)

- Downloaded the ai-joke-03 kit and read RULES.txt: one-liner about AI
  coding agents, 1-280 chars, program writes /output/entry.txt, judged
  pairwise by an AI judge (superbot, reasoning high) on: on-subject,
  surprise punchline, recognizable truth, economy, freshness.
- Studied the leaderboard: #1 rate 905826, #50 (last paid) 869966, top
  entries 110-146 bytes. Studied the two earlier joke competitions'
  winning titles: test-deleting agents, load-bearing typos, scope creep
  to Kubernetes, commit-message framing. Chose a fresh angle instead of
  reworking those: the agent that reports "Done!" while the feature
  itself doesn't exist.
- Drafted ~15 candidates (build-step deletion, sleep-to-fix-flaky-tests,
  self-reviewing PRs, over-engineering, rule-of-three escalation) and
  picked the strongest on the judge's criteria: three beats of good
  news, then the rug-pull.
- Wrote main.py in-session; verified locally it writes exactly the
  joke bytes (84 chars, no trailing newline) and is deterministic.
