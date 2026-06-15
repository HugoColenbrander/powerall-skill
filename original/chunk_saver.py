#!/usr/bin/env python3
"""Helper: save scraped content chunks to a JSON file as they come in."""
import json, sys
from pathlib import Path

DATA_FILE = Path("/Users/hugoc/docs-powerall-nl/api-docs-chunks.json")

def load():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return {}

def save(data):
    DATA_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    action = sys.argv[1]
    if action == "add":
        key = sys.argv[2]
        content = sys.stdin.read()
        data = load()
        data[key] = content
        save(data)
        print(f"Added '{key}': {len(content)} chars ({len(data)} total)")
    elif action == "list":
        data = load()
        for k, v in data.items():
            print(f"  {k}: {len(v)} chars")
        print(f"Total: {len(data)} entries")
    elif action == "export":
        data = load()
        md = "# Powerall Connect API Documentation\n\n"
        md += "Source: developers.powerall.nl\n"
        md += "OpenAPI Schema: connect.powerall.io/v1/docs/swagger.json\n"
        md += "Base URL: connect.powerall.io\n"
        md += "Auth: Basic Auth (tenant name + API token)\n\n"
        for key, content in data.items():
            md += f"---\n\n## {key}\n\n{content}\n\n"
        out = Path("/Users/hugoc/docs-powerall-nl/powerall-api-docs.md")
        out.write_text(md, encoding='utf-8')
        print(f"Exported {len(data)} sections, {len(md):,} chars to {out}")
