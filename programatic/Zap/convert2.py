import json
import os

# Get the current working directory as the base path
base_path = os.getcwd()

# Define file names for JSON rules
ascan_rules_file = 'ascanrules.json'
pscan_rules_file = 'pscanrules.json'

# Define the output directory for the Obsidian notes
output_directory = os.path.join(base_path, 'Obsidian_Notebook')

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Function to load JSON data
def load_json_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)['scanners']

# Function to create an Obsidian-compatible markdown note
def create_obsidian_note(scan_rule, report_content):
    # Construct the YAML front matter
    yaml_front_matter = f"""---
title: {scan_rule['name']}
tags: [scan-result, cwe-{scan_rule.get('cweId', 'N/A')}, wasc-{scan_rule.get('wascId', 'N/A')}]
cweId: {scan_rule.get('cweId', 'N/A')}
wascId: {scan_rule.get('wascId', 'N/A')}
enabled: {scan_rule['enabled']}
policyId: {scan_rule.get('policyId', 'N/A')}
attackStrength: {scan_rule.get('attackStrength', 'N/A')}
alertThreshold: {scan_rule.get('alertThreshold', 'N/A')}
---

"""
    return yaml_front_matter + report_content

# Load scan rules from JSON files
active_scan_rules = load_json_data(os.path.join(base_path, ascan_rules_file))
passive_scan_rules = load_json_data(os.path.join(base_path, pscan_rules_file))

# Process each scan rule and generate an Obsidian note
for rule in active_scan_rules + passive_scan_rules:
    # Construct the expected markdown file name using alert ID
    expected_md_filename = f"{rule['id']}.md"
    md_file_path = os.path.join(base_path, expected_md_filename)

    # Check if the markdown report exists with the expected name
    if os.path.isfile(md_file_path):
        with open(md_file_path, 'r') as md_file:
            report_content = md_file.read()
            obsidian_note = create_obsidian_note(rule, report_content)

            # Write the note content to a new markdown file in the output directory
            note_filename = f"{rule['id']}.md"
            with open(os.path.join(output_directory, note_filename), 'w') as note_file:
                note_file.write(obsidian_note)
    else:
        print(f"No matching markdown report found for rule ID: {rule['id']}")

# Informative print to check the results at the end
print(f"Processed {len(active_scan_rules) + len(passive_scan_rules)} rules.")
print(f"Check the {output_directory} directory for the generated markdown files.")
