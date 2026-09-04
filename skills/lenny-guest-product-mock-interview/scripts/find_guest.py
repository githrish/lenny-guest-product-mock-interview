#!/usr/bin/env python3
"""
Quick lookup for Lenny's Podcast transcript library.
Usage:
  python3 find_guest.py --guest "Shreyas Doshi"
  python3 find_guest.py --company "Google"
  python3 find_guest.py --keyword "interview"
  python3 find_guest.py --round "product sense"
  python3 find_guest.py --list-all
"""

import json
import sys
from pathlib import Path

INDEX = Path(__file__).resolve().parent.parent / "references" / "episode-index.json"

ROUND_KEYWORDS = {
    "product sense": ["design", "ux", "user experience", "wireframe", "prototype", "iteration", "ui", "persona"],
    "product metrics": ["metrics", "kpis", "data-driven", "analytics", "experimentation", "a/b testing", "okrs"],
    "product execution": ["prioritization", "roadmap", "execution", "mvp", "technical debt", "efficiency", "product development"],
    "product strategy": ["strategy", "vision", "positioning", "differentiation", "competition", "market"],
    "behavioral": ["career", "careers", "hiring", "leadership", "culture", "management", "team building", "feedback"],
    "growth": ["growth", "acquisition", "retention", "monetization", "funnel", "conversion", "viral growth"],
    "ai/technical pm": ["ai", "machine learning", "automation", "architecture", "engineering"],
}


def load_index():
    if not INDEX.exists():
        print(f"Error: index file not found at {INDEX}")
        print("Run the index builder first from the main repo.")
        sys.exit(1)
    return json.loads(INDEX.read_text())


def search_guest(episodes, name):
    name_lower = name.lower()
    return [ep for ep in episodes if name_lower in ep["guest"].lower()]


def search_company(episodes, company):
    company_lower = company.lower()
    results = []
    for ep in episodes:
        # Search title + description
        if company_lower in ep.get("title", "").lower():
            results.append(ep)
            continue
        if company_lower in ep.get("description", "").lower():
            results.append(ep)
            continue
        # Search keywords
        if any(company_lower in kw.lower() for kw in ep.get("keywords", [])):
            results.append(ep)
    return results


def search_keyword(episodes, kw):
    kw_lower = kw.lower()
    results = []
    for ep in episodes:
        if kw_lower in ep.get("title", "").lower():
            results.append(ep)
            continue
        if kw_lower in ep.get("description", "").lower():
            results.append(ep)
            continue
        if any(kw_lower in k.lower() for k in ep.get("keywords", [])):
            results.append(ep)
    return results


def search_round(episodes, round_name):
    round_lower = round_name.lower()
    keywords = ROUND_KEYWORDS.get(round_lower, [round_lower])
    results = []
    for ep in episodes:
        ep_kws = [k.lower() for k in ep.get("keywords", [])]
        if any(kw in ep_kws for kw in keywords):
            results.append(ep)
    return results


def list_all(episodes):
    for ep in episodes:
        print(f"{ep.get('date', 'N/A'):12s} | {ep['guest'][:30]:30s} | {ep.get('title', '')[:100]}")
        print(f"           slug: {ep['slug']}")
        print(f"           keywords: {', '.join(ep.get('keywords', [])[:8])}")
        print()


def print_results(results):
    if not results:
        print("No results found.")
        return
    print(f"\n=== {len(results)} episode(s) found ===\n")
    for ep in results:
        print(f"  Guest:     {ep['guest']}")
        print(f"  Title:     {ep.get('title', 'N/A')}")
        print(f"  Date:      {ep.get('date', 'N/A')}")
        print(f"  Duration:  {ep.get('duration', 'N/A')}")
        print(f"  Keywords:  {', '.join(ep.get('keywords', [])[:10])}")
        print(f"  Slug:      {ep['slug']}")
        print(f"  YouTube:   {ep.get('youtube_url', 'N/A')}")
        print()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("Options: --guest, --company, --keyword, --round, --list-all")
        sys.exit(0)

    episodes = load_index()
    arg = sys.argv[1]
    value = sys.argv[2] if len(sys.argv) > 2 else ""

    if arg == "--list-all":
        list_all(episodes)
    elif arg == "--guest":
        print_results(search_guest(episodes, value))
    elif arg == "--company":
        print_results(search_company(episodes, value))
    elif arg == "--keyword":
        print_results(search_keyword(episodes, value))
    elif arg == "--round":
        print_results(search_round(episodes, value))
    else:
        print(f"Unknown option: {arg}")
        print("Options: --guest, --company, --keyword, --round, --list-all")


if __name__ == "__main__":
    main()