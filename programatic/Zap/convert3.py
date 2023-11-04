import json
import os
import re
import yaml

# Function to sanitize filenames
def sanitize_filename(text):
    return re.sub(r'[\\/*?:"<>|]', "", text)

# Function to read the JSON file and return a dictionary of rules
def read_json_rules(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

# Function to read a markdown file and return its content
def read_markdown_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

# Function to parse markdown content, separating front matter and main content
def parse_markdown_content(markdown_content):
    parts = markdown_content.split('---')
    front_matter = parts[1]
    main_content = parts[2].strip()
    metadata = yaml.safe_load(front_matter)
    return metadata, main_content

# Ensure the 'results' directory exists
results_dir = 'results'
os.makedirs(results_dir, exist_ok=True)

# Read the scan rules from the JSON files
active_scan_rules = read_json_rules('ascanrules.json')
passive_scan_rules = read_json_rules('pscanrules.json')

# Merge active and passive scan rules
all_scan_rules = active_scan_rules['scanners'] + passive_scan_rules['scanners']

# Iterate over each rule and create a combined markdown file
for rule in all_scan_rules:
    markdown_filename = f"{rule['id']}.md"
    if os.path.exists(markdown_filename):
        markdown_content = read_markdown_file(markdown_filename)
        metadata, description = parse_markdown_content(markdown_content)
    else:
        metadata = {}
        description = "No detailed description available."

    # Combine references from JSON and markdown metadata if available
    references = metadata.get('references', [])
    if 'code' in metadata:
        references.append(metadata['code'])

    combined_references = '\n'.join(references) if references else 'No references provided.'

    combined_content = f"""
# {metadata.get('title', sanitize_filename(rule['name']))}

**ID:** {metadata.get('alertid', rule['id'])}
**Risk Level:** {metadata.get('risk', 'Not specified')}
**CWE ID:** {metadata.get('cwe', 'Not specified')}
**WASC ID:** {metadata.get('wasc', 'Not specified')}
**Attack Strength:** {rule.get('attackStrength', 'Not specified')}
**Alert Threshold:** {rule.get('alertThreshold', 'Not specified')}

## Rule Description
{description}

## Solution
{metadata.get('solution', 'No solution provided.')}

## References
{combined_references}
"""

    # Save the combined content to a new markdown file in the 'results' directory
    result_file_path = os.path.join(results_dir, f"{sanitize_filename(rule['name'])}.md")
    with open(result_file_path, 'w', encoding='utf-8') as file:
        file.write(combined_content)
