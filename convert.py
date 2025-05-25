import markdown
import sys
from pathlib import Path

def convert_md_to_html(md_file, html_file):
    with open(md_file, 'r') as f:
        text = f.read()
    html = markdown.markdown(text)
    with open(html_file, 'w') as f:
        f.write(html)

if __name__ == "__main__":
    md_file = sys.argv[1] if len(sys.argv) > 1 else "sample.md"
    html_file = "output.html"
    convert_md_to_html(md_file, html_file)
    print(f"Converted '{md_file}' to '{html_file}'")
