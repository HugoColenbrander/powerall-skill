#!/usr/bin/env python3
"""Convert Powerall MadCap Flare HTML docs to clean Markdown for LLM skill.
Version 2: improved table handling, cleaner output."""

import os
import re
from html.parser import HTMLParser
from pathlib import Path

SRC = Path("/Users/hugoc/docs-powerall-nl/docs.powerall.nl/Content/Powerall")
OUT = Path("/Users/hugoc/docs-powerall-nl/powerall-markdown")


def strip_html_to_text(html_content):
    """Extract just the text content from HTML, preserving minimal structure."""
    
    # Remove head, script, style blocks entirely
    html_content = re.sub(r'<head[^>]*>.*?</head>', '', html_content, flags=re.DOTALL|re.IGNORECASE)
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL|re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL|re.IGNORECASE)
    html_content = re.sub(r'<link[^>]*/?\s*>', '', html_content, flags=re.DOTALL|re.IGNORECASE)
    
    # Remove breadcrumb / nav sections
    html_content = re.sub(r'<div[^>]*class="[^"]*MCBreadcrumbsBox[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL|re.IGNORECASE)
    html_content = re.sub(r'<div[^>]*class="[^"]*nocontent[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL|re.IGNORECASE)
    html_content = re.sub(r'<p[^>]*class="[^"]*MCWebHelpFramesetLink[^"]*"[^>]*>.*?</p>', '', html_content, flags=re.DOTALL|re.IGNORECASE)
    
    # Remove MadCap namespace elements
    html_content = re.sub(r'<MadCap:\w+[^>]*/?\s*>', '', html_content, flags=re.DOTALL|re.IGNORECASE)
    html_content = re.sub(r'</MadCap:\w+>', '', html_content, flags=re.DOTALL|re.IGNORECASE)
    
    # Remove all HTML comments
    html_content = re.sub(r'<!--.*?-->', '', html_content, flags=re.DOTALL)
    
    # Handle tables: convert to markdown tables
    html_content = convert_tables(html_content)
    
    # Convert headings
    for i in range(1, 7):
        tag = f'h{i}'
        html_content = re.sub(
            rf'<{tag}[^>]*>(.*?)</{tag}>',
            lambda m, lvl=i: '\n\n' + '#' * lvl + ' ' + clean_inline(m.group(1)) + '\n\n',
            html_content, flags=re.DOTALL|re.IGNORECASE
        )
    
    # Convert lists
    html_content = convert_lists(html_content)
    
    # Convert paragraphs
    html_content = re.sub(r'<p[^>]*>(.*?)</p>', lambda m: '\n\n' + clean_inline(m.group(1)) + '\n\n', html_content, flags=re.DOTALL|re.IGNORECASE)
    
    # Convert line breaks
    html_content = re.sub(r'<br\s*/?\s*>', '\n', html_content, flags=re.IGNORECASE)
    
    # Bold
    html_content = re.sub(r'<(?:strong|b)[^>]*>(.*?)</(?:strong|b)>', lambda m: '**' + clean_inline(m.group(1)) + '**', html_content, flags=re.DOTALL|re.IGNORECASE)
    
    # Italic
    html_content = re.sub(r'<(?:em|i)[^>]*>(.*?)</(?:em|i)>', lambda m: '*' + clean_inline(m.group(1)) + '*', html_content, flags=re.DOTALL|re.IGNORECASE)
    
    # Remove all remaining tags
    html_content = re.sub(r'<[^>]+>', '', html_content)
    
    # Decode entities
    html_content = html_content.replace('&amp;', '&')
    html_content = html_content.replace('&lt;', '<')
    html_content = html_content.replace('&gt;', '>')
    html_content = html_content.replace('&nbsp;', ' ')
    html_content = html_content.replace('&#160;', ' ')
    html_content = html_content.replace('&#43;', '+')
    
    # Clean up whitespace
    html_content = re.sub(r'[ \t]+\n', '\n', html_content)
    html_content = re.sub(r'\n{3,}', '\n\n', html_content)
    html_content = re.sub(r'^[ \t]+', '', html_content, flags=re.MULTILINE)
    
    return html_content.strip()


def clean_inline(text):
    """Clean inline HTML to plain text."""
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&nbsp;', ' ').replace('&#160;', ' ')
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def convert_tables(html):
    """Convert HTML tables to markdown tables."""
    def table_repl(match):
        table_html = match.group(0)
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, flags=re.DOTALL|re.IGNORECASE)
        if not rows:
            return ''
        
        md_rows = []
        is_first = True
        for row in rows:
            cells = re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', row, flags=re.DOTALL|re.IGNORECASE)
            cells = [clean_inline(c).replace('|', '\\|') for c in cells]
            if cells:
                md_rows.append('| ' + ' | '.join(cells) + ' |')
                if is_first:
                    md_rows.append('| ' + ' | '.join(['---'] * len(cells)) + ' |')
                    is_first = False
        
        return '\n\n' + '\n'.join(md_rows) + '\n\n'
    
    return re.sub(r'<table[^>]*>.*?</table>', table_repl, html, flags=re.DOTALL|re.IGNORECASE)


def convert_lists(html):
    """Convert HTML lists to markdown lists."""
    # Process from innermost out - handle nested lists
    max_depth = 5
    for _ in range(max_depth):
        # Ordered lists
        def ol_repl(match):
            items = re.findall(r'<li[^>]*>(.*?)(?=</li>|$)', match.group(1), flags=re.DOTALL|re.IGNORECASE)
            lines = []
            for i, item in enumerate(items, 1):
                text = clean_inline(item).strip()
                if text:
                    lines.append(f'{i}. {text}')
            return '\n' + '\n'.join(lines) + '\n'
        
        html = re.sub(r'<ol[^>]*>(.*?)</ol>', ol_repl, html, flags=re.DOTALL|re.IGNORECASE)
        
        # Unordered lists  
        def ul_repl(match):
            items = re.findall(r'<li[^>]*>(.*?)(?=</li>|$)', match.group(1), flags=re.DOTALL|re.IGNORECASE)
            lines = []
            for item in items:
                text = clean_inline(item).strip()
                if text:
                    lines.append(f'- {text}')
            return '\n' + '\n'.join(lines) + '\n'
        
        html = re.sub(r'<ul[^>]*>(.*?)</ul>', ul_repl, html, flags=re.DOTALL|re.IGNORECASE)
    
    return html


def categorize(filename):
    """Group files by module prefix."""
    name = filename.lower()
    cat_map = [
        ('work.', 'work'), ('wba.', 'work'),
        ('warehouse.', 'warehouse'), ('barcodescanner', 'warehouse'), ('barcodes.', 'warehouse'), ('barcode', 'warehouse'),
        ('sales.', 'sales'), ('quotation.', 'sales'), ('cash.', 'sales'),
        ('finance.', 'finance'), ('p.fgl', 'finance'), ('p.gmf', 'finance'), ('p.bnk', 'finance'), ('p.kas', 'finance'), ('p.vtl', 'finance'),
        ('article.', 'article'), ('p.art', 'article'), ('p.pin', 'article'), ('p.gaa', 'article'), ('p.aib', 'article'),
        ('customer.', 'customer'), ('crm-app', 'customer'), ('crm.', 'customer'), ('relation.', 'customer'), ('contact.', 'customer'),
        ('rental.', 'rental'), ('p.rtl', 'rental'),
        ('machine.', 'machine'), ('p.mvm', 'machine'),
        ('service.', 'service'), ('p.sor', 'service'), ('p.svc', 'service'),
        ('purchase.', 'purchase'), ('p.ink', 'purchase'),
        ('faq.', 'faq'), ('faq', 'faq'),
        ('dashboard', 'dashboard'),
        ('general.', 'general'), ('p.gen', 'general'), ('p.gta', 'general'), ('p.pst', 'general'), ('p.gip', 'general'), ('alg.', 'general'),
        ('layout.', 'layout'), ('word', 'layout'),
        ('app manual', 'apps'), ('apps', 'apps'),
        ('task/', 'task'),
    ]
    for prefix, cat in cat_map:
        if name.startswith(prefix):
            return cat
    return 'other'


def main():
    htm_files = sorted(SRC.rglob("*.htm"))
    print(f"Found {len(htm_files)} .htm files")

    OUT.mkdir(parents=True, exist_ok=True)

    categories = {}
    all_content = []
    errors = []
    skipped = 0

    for fpath in htm_files:
        rel = fpath.relative_to(SRC)
        
        try:
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                html = f.read()
        except Exception as e:
            errors.append(f"{rel}: {e}")
            continue

        # Extract title
        title_match = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
        title = title_match.group(1).strip() if title_match else ""
        
        # Strip to markdown
        md = strip_html_to_text(html)
        
        if len(md.strip()) < 30:
            skipped += 1
            continue

        # Remove copyright line
        md = re.sub(r'Copyright\s*©.*$', '', md, flags=re.MULTILINE)
        md = re.sub(r'Disclaimer\s*$', '', md, flags=re.MULTILINE)
        
        # Remove "Gerelateerde onderwerpen" section (end of each page)
        md = re.sub(r'Gerelateerde onderwerpen\s*$', '', md, flags=re.MULTILINE)
        
        # Clean up trailing whitespace
        md = md.strip()

        cat = categorize(str(rel).lower())
        if cat not in categories:
            categories[cat] = []
        
        heading = title if title else str(rel.stem).replace('.', ' ')
        entry = f"## {heading}\n\n{md}\n\n---\n"
        categories[cat].append(entry)
        all_content.append(entry)

    print(f"Converted {len(all_content)} files ({skipped} skipped, {len(errors)} errors)")
    if errors:
        for e in errors[:5]:
            print(f"  ERR: {e}")

    # Write per-category files
    for cat, entries in sorted(categories.items()):
        content = f"# Powerall - {cat.upper()}\n\n" + "".join(entries)
        out_path = OUT / f"{cat}.md"
        out_path.write_text(content, encoding='utf-8')
        print(f"  {cat:15s}  {len(entries):>4} topics  {len(content):>9,} chars")

    # Write combined
    combined = "# Powerall Documentatie - Compleet\n\n" + "".join(all_content)
    (OUT / "powerall-full.md").write_text(combined, encoding='utf-8')
    print(f"\n  {'combined':15s}  {len(all_content):>4} topics  {len(combined):>9,} chars  -> powerall-full.md")

    # Total size
    total = sum(len(e) for e in all_content)
    print(f"\n  Total: {total:,} chars (~{total//1024:,} KB)")


if __name__ == '__main__':
    main()
