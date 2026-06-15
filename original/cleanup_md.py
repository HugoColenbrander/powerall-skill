#!/usr/bin/env python3
"""Post-process: clean up the converted markdown files."""

import re
from pathlib import Path

MD_DIR = Path("/Users/hugoc/docs-powerall-nl/powerall-markdown")

def clean_md(text):
    # Remove duplicate title lines right after heading
    # e.g. "## Foo Bar\n\nFoo Bar\n" -> "## Foo Bar\n\n"
    text = re.sub(r'(^## .+)\n\n\1\n', r'\1\n\n', text, flags=re.MULTILINE)
    
    # Remove lines that are just whitespace
    text = re.sub(r'^[ \t]+\n', '\n', text, flags=re.MULTILINE)
    
    # Collapse 3+ blank lines to 2
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Remove empty list items (just a number/dash with nothing)
    text = re.sub(r'^\s*\d+\.\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*-\s*\n', '', text, flags=re.MULTILINE)
    
    # Remove raw table data that appears before the markdown table
    # Pattern: lines with cell content followed by the proper markdown table
    # We'll remove lines that look like raw table cells (no | prefix) between headings and | tables
    lines = text.split('\n')
    cleaned = []
    skip_raw_table = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Detect start of raw table dump (cells without pipes, before a | table)
        if stripped and not stripped.startswith('|') and not stripped.startswith('#') and not stripped.startswith('-'):
            # Check if next lines form a markdown table
            upcoming = '\n'.join(lines[i:i+5])
            if re.search(r'\|.*\|.*\|', upcoming):
                # This might be raw table text before the markdown version - skip it
                # But only if it looks like table cell data (short lines, multiple in a row)
                if len(stripped) < 80 and i > 0 and lines[i-1].strip() == '':
                    skip_raw_table = True
        if skip_raw_table:
            if stripped.startswith('|') or stripped == '':
                skip_raw_table = False
                if stripped.startswith('|'):
                    cleaned.append(line)
            continue
        cleaned.append(line)
    
    text = '\n'.join(cleaned)
    
    # Remove "Open onderwerp met navigatie" remnants
    text = re.sub(r'Open onderwerp met navigatie.*?\n', '', text)
    
    # Remove "U bent hier:" breadcrumb remnants  
    text = re.sub(r'U bent hier:.*?\n', '', text)
    
    # Remove MadCap concept tags
    text = re.sub(r'MadCap:.*?\n', '', text)
    
    # Remove anchor remnants
    text = re.sub(r'\[?aanchor\d+\]?', '', text)
    
    # Remove "Ga naar" variable noise but keep the meaningful text after it
    text = re.sub(r'Ga naar\s+', 'Ga naar ', text)
    
    # Remove excessive whitespace lines before headings
    text = re.sub(r'\n{2,}(##)', r'\n\n\\1', text)
    
    # Final cleanup: collapse blank lines again
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    return text.strip() + '\n'


total_before = 0
total_after = 0

for f in sorted(MD_DIR.glob("*.md")):
    before = f.read_text(encoding='utf-8')
    total_before += len(before)
    after = clean_md(before)
    total_after += len(after)
    f.write_text(after, encoding='utf-8')
    saved = len(before) - len(after)
    pct = (saved / len(before) * 100) if before else 0
    print(f"  {f.name:25s}  {len(before):>8,} -> {len(after):>8,}  ({saved:>+6,} / {pct:.1f}%)")

print(f"\n  Total: {total_before:,} -> {total_after:,}  (saved {total_before - total_after:,} chars, {(total_before-total_after)/total_before*100:.1f}%)")
