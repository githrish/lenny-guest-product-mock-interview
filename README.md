# PM Mock Interviews with Lenny's Podcast Guests

[![Licence: MIT](https://img.shields.io/badge/licence-MIT-blue)](LICENSE)
[![Platforms](https://img.shields.io/badge/works%20with-ChatGPT%20%7C%20Claude%20%7C%20Hermes%20%7C%20Codex-blue)]()

**Get interviewed BY Lenny's Podcast guests. Not just study their advice.**

Shreyas Doshi grills your product strategy through his 3 levels of product
work. Brian Chesky tears apart your design instincts. Nikita Bier demands
your growth numbers. April Dunford makes you defend your positioning.

300+ Lenny's Podcast guests. Every PM interview round. Their actual voice,
built from their actual transcripts. Works with ChatGPT, Claude, Hermes,
Codex, or any AI agent that loads a SKILL.md.

## Install

One step. Nothing else to clone.

```bash
npx skills add githrish/lenny-guest-product-mock-interview -g -y
```

An interview needs one transcript: the guest you get matched with. The skill
fetches that single file, around 87KB, when it needs it. The 303-episode index
ships with the skill, so it always knows exactly which one to pull.

### Other ways in

**Download the skill.** Grab
[`dist/lenny-guest-product-mock-interview.zip`](dist/lenny-guest-product-mock-interview.zip)
and drop it into any skills folder. Works with Claude, Claude Code, Codex, Cursor
and anything else that reads a skills directory. In claude.ai it lives under
Settings, then Capabilities, then Skills.

**Copy the prompt.** [`dist/prompt.md`](dist/prompt.md) is the whole skill as one
pasteable file, for ChatGPT, Claude, Gemini or any capable model. It is generated
from `skills/`, so it never drifts from the installed version, and it opens by
telling the agent which local files it does not have so it does not pretend to
run the search script.

**Clone it.**

```bash
git clone https://github.com/githrish/lenny-guest-product-mock-interview.git
```

Point your agent at `skills/lenny-guest-product-mock-interview/SKILL.md`.

### Optional: the full transcript library

Only worth it for offline use, or if you run many interviews and would rather not
fetch each time. The skill prefers local files whenever it finds them.

```bash
git clone https://github.com/ChatPRD/lennys-podcast-transcripts.git
```

Place it next to the skill. It is a 9.2MB download that expands to about 35MB.

## Demo

![Demo](https://github.com/githrish/lenny-guest-product-mock-interview/releases/download/v1.0.0/Lenny.Guest.Product.Mock.Interview.gif)

> Overview → Pick company → Pick round → Guest match → Interview. 30 seconds start to ready.

## What makes this different

Most PM interview prep is passive. Read a framework. Watch a video. Hope it
sticks. This is the opposite. You sit across from the people who actually
hire and evaluate PMs. They push back. They drill your actual work. They do
not let you off easy.

Every interview uses a real Lenny's Podcast guest. The agent loads their
transcript, studies their frameworks and voice, then interviews you in
character. 6 phases. Hard difficulty. Real feedback with direct quotes from
their episode.

## How it works

- Pick a company and round (or name a guest directly)
- Get matched with a Lenny's guest who worked there
- Upload your resume. The guest drills your actual decisions through their
  actual frameworks
- Run a full 6-phase interview: Opening, experience deep-dive, round-specific
  case, your questions, closing reaction, structured feedback

## Supported rounds

Product Sense, Product Metrics, Product Execution, Product Strategy,
Technical / System Design, Behavioral, Estimation, GTM / Product Marketing

## Guests by category

| Category | Featured Guests |
|----------|----------------|
| PM Interview & Career | Shreyas Doshi, Casey Winters, Deb Liu, Marty Cagan |
| Product Sense & Design | Brian Chesky, Tobi Lutke, Ami Vora, Bob Baxley |
| Product Strategy | April Dunford, Bob Moesta, Shishir Mehrotra |
| AI & Technical PM | Chip Huyen, Dianne Penn, Aparna Chennapragada |
| Growth & Metrics | Adam Fishman, Sean Ellis, Crystal Widjaja |
| Leadership | Claire Hughes Johnson, Ben Horowitz, Bret Taylor |

## Repository layout

```
skills/lenny-guest-product-mock-interview/
├── SKILL.md                         # the skill, and the source of truth
├── references/episode-index.json    # all 303 episodes, indexed
└── scripts/find_guest.py            # guest lookup by name, company, round, keyword
dist/
├── prompt.md                        # generated single-file prompt
└── lenny-guest-product-mock-interview.zip
scripts/build-prompt.py              # regenerates dist/ from skills/
```

Edit the skill, never `dist/`. CI regenerates `dist/` on every push that
touches `skills/`.

## Requirements

- An AI agent that supports markdown skill files
- Web access, so it can fetch the matched guest's transcript. Not needed if you
  cloned the full library
- Python 3 for the guest search script (optional)

## Contributing

This skill is open source. The transcript library is maintained separately
at [ChatPRD/lennys-podcast-transcripts](https://github.com/ChatPRD/lennys-podcast-transcripts).

## Licence

MIT. See [LICENSE](LICENSE).

## Disclaimer

Not affiliated with, endorsed by, or sponsored by Lenny's Podcast or Lenny
Rachitsky. Guest names are used to describe whose publicly published episode a
given persona is built from.

Transcripts are not part of this repository and are not redistributed by it. They
are maintained by [ChatPRD](https://github.com/ChatPRD/lennys-podcast-transcripts),
which at the time of writing publishes no licence. This skill reads them from
source at runtime; if you rely on them, check that repository for terms yourself.
