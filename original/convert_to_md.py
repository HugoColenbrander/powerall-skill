#!/usr/bin/env python3
"""Convert Powerall MadCap Flare HTML docs to clean Markdown for LLM skill."""

import os
import re
from html.parser import HTMLParser
from pathlib import Path

SRC = Path("/Users/hugoc/docs-powerall-nl/docs.powerall.nl/Content/Powerall")
OUT = Path("/Users/hugoc/docs-powerall-nl/powerall-markdown")

class HTMLToMarkdown(HTMLParser):
    """Strip MadCap Flare HTML to clean Markdown."""

    def __init__(self):
        super().__init__()
        self.output = []
        self.skip_tags = {'script', 'style', 'link', 'meta', 'noscript', 'head'}
        self.in_skip = 0
        self.current_tag = None
        self.in_ol = 0
        self.in_ul = 0
        self.in_td = False
        self.in_th = False
        self.row_cells = []
        self.in_table = False
        self.table_rows = []
        self.in_header_row = False
        self.list_counters = []
        self.last_was_block = False
        self.in_h1 = False
        self.title = ""

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        self.current_tag = tag

        if tag in self.skip_tags:
            self.in_skip += 1
            return

        if tag == 'h1':
            self.in_h1 = True
        elif tag in ('h2', 'h3', 'h4', 'h5', 'h6'):
            level = int(tag[1])
            self._block()
            self.output.append('#' * level + ' ')
        elif tag == 'p':
            self._block()
        elif tag == 'br':
            self.output.append('\n')
        elif tag == 'strong' or tag == 'b':
            self.output.append('**')
        elif tag == 'em' or tag == 'i':
            self.output.append('*')
        elif tag == 'ol':
            self.in_ol += 1
            self.list_counters.append(1)
            self._block()
        elif tag == 'ul':
            self.in_ul += 1
            self._block()
        elif tag == 'li':
            self._block()
            indent = '  ' * (self.in_ol + self.in_ul - 1)
            if self.in_ol > 0:
                num = self.list_counters[-1] if self.list_counters else 1
                self.output.append(f'{indent}{num}. ')
                if self.list_counters:
                    self.list_counters[-1] += 1
            else:
                self.output.append(f'{indent}- ')
        elif tag == 'table':
            self.in_table = True
            self.table_rows = []
            self._block()
        elif tag == 'tr':
            self.row_cells = []
            self.in_header_row = False
        elif tag == 'th':
            self.in_th = True
            self.in_header_row = True
        elif tag == 'td':
            self.in_td = True
        elif tag == 'a':
            pass  # skip links, keep text
        elif tag == 'img':
            alt = ''
            for name, val in attrs:
                if name == 'alt':
                    alt = val
            if alt:
                self.output.append(f'[{alt}]')

    def handle_endtag(self, tag):
        tag = tag.lower()

        if tag in self.skip_tags:
            self.in_skip -= 1
            return

        if tag == 'h1':
            self.in_h1 = False
            self.output.append('\n\n')
            self.last_was_block = True
        elif tag in ('h2', 'h3', 'h4', 'h5', 'h6'):
            self.output.append('\n\n')
            self.last_was_block = True
        elif tag == 'p':
            self.output.append('\n\n')
            self.last_was_block = True
        elif tag in ('strong', 'b'):
            self.output.append('**')
        elif tag in ('em', 'i'):
            self.output.append('*')
        elif tag == 'ol':
            if self.in_ol > 0:
                self.in_ol -= 1
                if self.list_counters:
                    self.list_counters.pop()
            self.output.append('\n')
            self.last_was_block = True
        elif tag == 'ul':
            if self.in_ul > 0:
                self.in_ul -= 1
            self.output.append('\n')
            self.last_was_block = True
        elif tag == 'li':
            self.output.append('\n')
        elif tag == 'th':
            self.in_th = False
            cell_text = ''.join(self.output).split('\n')[-1].strip().replace('|', '\\|')
            self.row_cells.append(cell_text)
            # remove the text we just captured from output
        elif tag == 'td':
            self.in_td = False
            cell_text = ''.join(self.output).split('\n')[-1].strip().replace('|', '\\|')
            self.row_cells.append(cell_text)
        elif tag == 'tr':
            if self.row_cells:
                self.table_rows.append((self.row_cells, self.in_header_row))
            self.row_cells = []
        elif tag == 'table':
            self.in_table = False
            # Render collected table
            if self.table_rows:
                header_row = None
                for i, (cells, is_header) in enumerate(self.table_rows):
                    if is_header or i == 0:
                        header_row = cells
                        break
                for i, (cells, is_header) in enumerate(self.table_rows):
                    line = '| ' + ' | '.join(cells) + ' |'
                    self.output.append(line + '\n')
                    if i == 0 or (header_row and i == 1 and not self.table_rows[0][1]):
                        sep = '| ' + ' | '.join(['---'] * len(cells)) + ' |'
                        self.output.append(sep + '\n')
                self.output.append('\n')
                self.table_rows = []

    def handle_data(self, data):
        if self.in_skip > 0:
            return

        # Skip MadCap variable noise
        if 'mc-variable' in str(self.current_tag):
            return

        text = data
        # Collapse whitespace
        text = re.sub(r'[ \t]+', ' ', text)
        text = text.strip('\r')
        if text:
            if self.last_was_block and not text.startswith((' ', '\n', '\t')):
                self.last_was_block = False
            self.output.append(text)

    def _block(self):
        self.last_was_block = False

    def get_markdown(self):
        raw = ''.join(self.output)
        # Clean up excessive newlines
        raw = re.sub(r'\n{3,}', '\n\n', raw)
        # Clean up MadCap remnants
        raw = re.sub(r'MadCap:.*?$', '', raw, flags=re.MULTILINE)
        raw = re.sub(r'\[?aanchor\d+\]?', '', raw)
        raw = re.sub(r'Open onderwerp met navigatie', '', raw)
        raw = re.sub(r'U bent hier:.*', '', raw)
        raw = raw.strip()
        return raw


def convert_file(filepath):
    """Convert a single .htm file to Markdown."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            html = f.read()
    except Exception as e:
        return None, str(e)

    parser = HTMLToMarkdown()
    try:
        parser.feed(html)
    except Exception as e:
        return None, str(e)

    md = parser.get_markdown()
    
    # Extract title from <title> tag
    title_match = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
    title = title_match.group(1).strip() if title_match else ""
    
    return title, md


def categorize(filename):
    """Group files by module prefix."""
    name = filename.lower().replace('.htm', '')
    
    categories = {
        'work': ['work.', 'wba.', 'work.'],
        'warehouse': ['warehouse.', 'barcodescanner', 'barcodes.', 'barcode'],
        'sales': ['sales.', 'quotation.', 'cash.'],
        'finance': ['finance.', 'p.fgl', 'p.gmf', 'p.bnk', 'p.kas', 'p.vtl'],
        'article': ['article.', 'p.art', 'p.pin', 'p.gaa', 'p.aib'],
        'customer': ['customer.', 'crm-app', 'crm.', 'relation.', 'contact.'],
        'rental': ['rental.', 'p.rtl'],
        'machine': ['machine.', 'p.mvm'],
        'service': ['service.', 'p.sor', 'p.svc'],
        'purchase': ['purchase.', 'p.ink'],
        'faq': ['faq.', 'faq'],
        'dashboard': ['dashboard'],
        'general': ['general.', 'p.gen', 'p.gta', 'p.pst', 'p.gip', 'alg.'],
        'layout': ['layout.', 'word'],
        'apps': ['app manual', 'apps'],
        'task': ['task/'],
    }
    
    for cat, prefixes in categories.items():
        for prefix in prefixes:
            if name.startswith(prefix):
                return cat
    return 'other'


def main():
    htm_files = sorted(SRC.rglob("*.htm"))
    print(f"Found {len(htm_files)} .htm files")

    OUT.mkdir(parents=True, exist_ok=True)

    # Collect per-category
    categories = {}
    all_content = []
    errors = []
    total_chars = 0

    for fpath in htm_files:
        rel = fpath.relative_to(SRC)
        title, md = convert_file(fpath)
        
        if md is None:
            errors.append(f"ERROR: {rel}: {title}")
            continue
        
        if len(md.strip()) < 20:
            continue  # skip near-empty files

        cat = categorize(str(rel))
        if cat not in categories:
            categories[cat] = []
        
        # Use title as heading, fall back to filename
        heading = title if title else str(rel.stem).replace('.', ' ')
        entry = f"## {heading}\n\n{md}\n\n---\n"
        categories[cat].append(entry)
        all_content.append(entry)
        total_chars += len(entry)

    print(f"Converted {len(all_content)} files, {total_chars:,} chars total")
    if errors:
        print(f"{len(errors)} errors:")
        for e in errors[:10]:
            print(f"  {e}")

    # Write per-category files
    for cat, entries in sorted(categories.items()):
        content = f"# Powerall Documentatie - {cat.upper()}\n\n{''.join(entries)}"
        out_path = OUT / f"{cat}.md"
        out_path.write_text(content, encoding='utf-8')
        print(f"  {cat}: {len(entries)} topics, {len(content):,} chars -> {out_path.name}")

    # Write combined file
    combined = "# Powerall Documentatie - Compleet\n\n"
    combined += "".join(all_content)
    combined_path = OUT / "powerall-full.md"
    combined_path.write_text(combined, encoding='utf-8')
    print(f"\nCombined: {len(all_content)} topics, {len(combined):,} chars -> powerall-full.md")

    # Stats
    sizes = []
    for cat, entries in sorted(categories.items()):
        sizes.append(f"  {cat}: {len(entries)} topics")
    print("\nSummary:")
    print('\n'.join(sizes))


if __name__ == '__main__':
    main()
