# Wikipedia Article Search

## Overview
This project provides a simple command-line tool for searching Wikipedia article titles. Users can perform basic searches, apply advanced filtering options, and retrieve metadata for Wikipedia articles.

## Features
- **Basic Search**: Search for articles by keyword.
- **Advanced Search Options**:
  - Filter by maximum title length.
  - Limit the number of search results.
  - Retrieve a random article from results.
  - Check if a favorite article is in the results.
  - Search using multiple keywords.
- **Metadata Retrieval**: Fetch additional article details like contributor username, timestamp, and word count.

## Installation
### Prerequisites
- Python 3.x
- `requests` library (install using `pip install requests`)

### Clone Repository
```bash
git clone https://github.com/yourusername/wiki-search.git
cd wiki-search
```

## Usage
Run the program from the command line:
```bash
python search.py
```
Follow the prompts to enter search keywords and select advanced search options.

## File Structure
- `search.py` - Main script for running the search functionality.
- `wiki.py` - Handles Wikipedia API requests and metadata extraction.
- `search_tests_helper.py` - Contains helper functions for testing search functions.

## Contribution
Feel free to submit pull requests or open issues to suggest improvements.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Acknowledgments
This project uses Wikipedia's API to fetch article information.

