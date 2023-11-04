# Obsidian KB Integration for OWASP ZAP Scan Reports

## Overview
This repository contains the resources and tools to integrate OWASP ZAP scan reports into the Obsidian knowledge base (KB). It includes a markdown importer plugin for converting ZAP HTML scan reports into markdown format suitable for Obsidian, templates for reporting, and a guide on how to import and manage the scan data within the KB.

## Features
- **ZAP to Markdown Converter**: A JavaScript-based importer to convert OWASP ZAP scan results from HTML to Obsidian-friendly markdown.
- **Markdown Report Templates**: Pre-formatted templates for analysts to document their investigation of each alert, streamlining the report-writing process.
- **Integration Guides**: Step-by-step documentation to help users import scan results and create reports within the Obsidian KB.

## Getting Started
1. Clone this repository to your local machine.
2. Follow the `docs/guides/import-guide.md` to set up your Obsidian environment for scan report imports.
3. Use the `src/importers/zap-to-md.js` script to convert new scan reports into markdown files.
4. Document your findings using `docs/templates/report-template.md` as a starting point.

## Contributing
We welcome contributions to this project! Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License
This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Support
If you encounter any problems or have any suggestions, please open an issue in the repository.

## Acknowledgements
- The OWASP ZAP team for providing an excellent open-source tool for security scanning.
- The Obsidian community for creating a versatile platform for knowledge management.

Thank you for using or contributing to this project!

