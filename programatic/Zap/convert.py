import json
import os

def parse_md_content(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content

def create_obsidian_note(alert, md_content, output_folder):
    # Start with YAML Frontmatter
    note_content = "---\n"
    note_content += f"title: {alert.get('name', 'Unknown Alert')}\n"
    note_content += f"alert_id: {alert.get('id', 'N/A')}\n"
    note_content += "---\n\n"
    
    # Extracting essential details from the alert dictionary
    note_content += f"# {alert.get('name', 'Unknown Alert')}\n\n"
    note_content += f"- **Alert ID**: [[{alert.get('id', 'N/A')}]]\n"  # Linking to itself for easy copying and referencing
    if 'policyId' in alert:
        note_content += f"- **Policy ID**: {alert['policyId']}\n"
    if 'cweId' in alert:
        note_content += f"- **CWE ID**: {alert['cweId']} #CWE{alert['cweId']}\n"  # Added as a tag for easy searching
    if 'wascId' in alert:
        note_content += f"- **WASC ID**: {alert['wascId']}\n"
    if 'quality' in alert:
        note_content += f"- **Quality**: {alert['quality']}\n"
    if 'status' in alert:
        note_content += f"- **Status**: {alert['status']}\n"
    if 'enabled' in alert:
        note_content += f"- **Enabled**: {alert['enabled']}\n\n"
    
    # Appending the content from the .md file
    note_content += md_content
    
    # Writing to the Obsidian note file
    with open(os.path.join(output_folder, f"{alert['id']}_combined.md"), 'w') as f:
        f.write(note_content)

def main():
    # Load JSON files
    with open("ascanrules.json", 'r') as f:
        ascanrules = json.load(f)['scanners']
    with open("pscanrules.json", 'r') as f:
        pscanrules = json.load(f)['scanners']
    
    # Combine both lists
    all_alerts = ascanrules + pscanrules

    # Directory paths
    md_folder = "."  # Assuming .md files are in the current directory
    output_folder = "./obsidian_notes"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over each alert and create an Obsidian note
    for alert in all_alerts:
        alert_id = alert['id']
        possible_filenames = [f"{alert_id}.md", f"{alert_id.replace('-', '_')}.md"]
        for filename in possible_filenames:
            md_file_path = os.path.join(md_folder, filename)
            if os.path.exists(md_file_path):
                md_content = parse_md_content(md_file_path)
                create_obsidian_note(alert, md_content, output_folder)
                break

if __name__ == "__main__":
    main()
