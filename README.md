# Technical Documentation Scraper & Multi-Level Content Rewriter

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Azure OpenAI](https://img.shields.io/badge/Azure-OpenAI-green.svg)](https://azure.microsoft.com/en-us/products/ai-services/openai-service)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent system that scrapes technical documentation and automatically rewrites content at multiple difficulty levels (Beginner, Intermediate, Advanced) using Azure OpenAI. Perfect for creating accessible educational content and improving documentation accessibility.

## 🚀 Features

- **Intelligent Web Scraping**: Automatically extracts structured content from technical documentation
- **Multi-Level Content Rewriting**: Generates content for three difficulty levels
- **AI-Powered Analysis**: Identifies complex terms and document purpose
- **Structured JSON Output**: Production-ready format for web applications
- **Link Preservation**: Maintains all original hyperlinks and references
- **Comprehensive Summaries**: Creates targeted summaries for each audience level

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [System Architecture](#system-architecture)
- [Usage Guide](#usage-guide)
- [Configuration](#configuration)
- [API Reference](#api-reference)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## 🛠 Installation

### Prerequisites

- Python 3.8 or higher
- Azure OpenAI Service access
- Azure CLI (for authentication)

### Install Dependencies

```bash
pip install requests beautifulsoup4 azure-identity openai
```

### Azure Setup

1. **Create Azure OpenAI Resource**
   ```bash
   az cognitiveservices account create \
     --name your-openai-resource \
     --resource-group your-resource-group \
     --kind OpenAI \
     --sku S0 \
     --location eastus2
   ```

2. **Deploy GPT-4 Model**
   - Deploy `gpt-4` model in Azure OpenAI Studio
   - Note your deployment name (default: `gpt-4.1`)

3. **Authentication**
   ```bash
   az login
   ```

## 🚀 Quick Start

```python
from scraper_rewriter import scrape_sections, difficulty, intermediate_rewrite, beginner_rewrite, summarizer_func

# 1. Scrape documentation
url = "https://learn.microsoft.com/en-us/azure/load-balancer/gateway-overview"
sections = scrape_sections(url)

# 2. Analyze difficulty and identify complex terms
difficulty(sections)

# 3. Generate multi-level content
sections_intermediate = intermediate_rewrite(sections)
sections_beginner = beginner_rewrite(sections)

# 4. Create summaries
summaries = summarizer_func(url)

# 5. Assemble final JSON
final_json = {
    "summaries": {
        "content": [
            {"type": "paragraph", "text": summaries['beginner_level_summary']},
            {"type": "paragraph", "text": summaries['intermediate_level_summary']},
            {"type": "paragraph", "text": summaries['advanced_level_summary']}
        ]
    }
}

# Save to file
import json
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(final_json, f, ensure_ascii=False, indent=4)
```

## 🏗 System Architecture

```
URL Input → Web Scraping → Difficulty Analysis → Multi-level Rewriting → Summarization → JSON Output
```

### Core Components

1. **Web Scraper**: Extracts structured content from documentation pages
2. **Difficulty Analyzer**: Identifies complex terms using AI analysis
3. **Content Rewriters**: Generates simplified versions for different skill levels
4. **Summarizer**: Creates concise summaries for each difficulty level

## 📖 Usage Guide

### Basic Workflow

#### Step 1: Web Scraping
```python
sections = scrape_sections("https://your-documentation-url.com")
```

**Output Structure:**
```json
{
  "id": "section-0",
  "title": "Section Title",
  "content": [{"type": "h1", "text": "Plain text content"}],
  "html": "Raw HTML content",
  "images": ["<img> tags"],
  "img_alt": ["Alt text"],
  "tables": ["<table> HTML"],
  "codes": ["<code> blocks"]
}
```

#### Step 2: Difficulty Analysis
```python
difficulty(sections)
```

Enhances each section with:
- **topic**: Main subject matter
- **purpose_of_document**: Document's intended use
- **difficult_terms**: Technical terms requiring explanation

#### Step 3: Content Rewriting

**Intermediate Level** (Professionals/Students):
```python
sections_intermediate = intermediate_rewrite(sections)
```

**Beginner Level** (Zero field knowledge):
```python
sections_beginner = beginner_rewrite(sections)
```

#### Step 4: Summarization
```python
summaries = summarizer_func(url)
```

Returns three summary levels:
- `beginner_level_summary`: Extremely simple language
- `intermediate_level_summary`: Professional but accessible
- `advanced_level_summary`: Technical accuracy

### Advanced Usage

#### Batch Processing
```python
urls = [
    "https://docs.microsoft.com/page1",
    "https://docs.microsoft.com/page2",
    "https://docs.microsoft.com/page3"
]

for url in urls:
    try:
        # Process each URL
        result = process_documentation(url)
        save_result(result, f"output_{url.split('/')[-1]}.json")
        
        # Rate limiting
        time.sleep(5)
    except Exception as e:
        print(f"Error processing {url}: {e}")
```

#### Custom Configuration
```python
# Custom Azure OpenAI settings
AZURE_OPENAI_ENDPOINT = "https://your-resource.openai.azure.com/"
AZURE_OPENAI_DEPLOYMENT = "your-gpt4-deployment"
AZURE_OPENAI_VERSION = "2024-12-01-preview"
```

## ⚙️ Configuration

### Environment Variables
Create a `.env` file:
```env
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-4.1
AZURE_OPENAI_VERSION=2024-12-01-preview
```

### Azure OpenAI Configuration
```python
from azure.identity import DefaultAzureCredential
from openai import AzureOpenAI

token = DefaultAzureCredential().get_token("https://cognitiveservices.azure.com/.default").token

llm = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://your-resource.openai.azure.com/",
    api_key=token,
)
```

## 📚 API Reference

### `scrape_sections(url)`
Extracts structured content from a webpage.

**Parameters:**
- `url` (str): URL to scrape

**Returns:**
- List of section dictionaries with content, metadata, and HTML

**Example:**
```python
sections = scrape_sections("https://example.com/docs")
```

### `difficulty(sections)`
Analyzes content to identify difficult terms and document purpose.

**Parameters:**
- `sections` (list): Output from `scrape_sections()`

**Modifies:**
- Adds `topic_difficult_terms` to each section

### `intermediate_rewrite(sections)`
Rewrites content for professionals/students unfamiliar with the topic.

**Parameters:**
- `sections` (list): Sections with difficulty analysis

**Returns:**
- List of sections with simplified content

### `beginner_rewrite(sections)`
Rewrites content for users with zero field knowledge.

**Parameters:**
- `sections` (list): Sections with difficulty analysis

**Returns:**
- List of sections with highly simplified content

### `summarizer_func(url)`
Generates summaries at three difficulty levels.

**Parameters:**
- `url` (str): URL to summarize

**Returns:**
- Dictionary with three summary levels

## 🔧 Examples

### Example 1: Processing Microsoft Learn Documentation

```python
# Process Azure Load Balancer documentation
url = "https://learn.microsoft.com/en-us/azure/load-balancer/gateway-overview"

# Complete processing pipeline
sections = scrape_sections(url)
difficulty(sections)

# Generate all difficulty levels
beginner_sections = beginner_rewrite(sections)
intermediate_sections = intermediate_rewrite(sections)
advanced_sections = [{"id": s["id"], "title": s["title"], "content": [{"type": "paragraph", "text": s["html"]}]} for s in sections]

# Create summaries
summaries = summarizer_func(url)

# Combine everything
final_output = {
    "url": url,
    "processed_at": datetime.now().isoformat(),
    "summaries": {
        "content": [
            {"type": "paragraph", "text": summaries["beginner_level_summary"]},
            {"type": "paragraph", "text": summaries["intermediate_level_summary"]},
            {"type": "paragraph", "text": summaries["advanced_level_summary"]}
        ]
    },
    "sections": [
        {
            "id": beginner_sections[i]["id"],
            "title": beginner_sections[i]["title"],
            "content": [
                beginner_sections[i]["content"][0],
                intermediate_sections[i]["content"][0],
                advanced_sections[i]["content"][0]
            ]
        }
        for i in range(len(beginner_sections))
    ]
}

# Save result
with open("azure_load_balancer_docs.json", "w", encoding="utf-8") as f:
    json.dump(final_output, f, ensure_ascii=False, indent=2)
```


### Development Setup
```bash
# Clone repository
git clone https://github.com/yourusername/technical-doc-rewriter.git
cd technical-doc-rewriter

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/
```


