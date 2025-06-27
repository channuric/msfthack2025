"""
Setup configuration for the Technical Documentation Scraper & Multi-Level Content Rewriter package.
"""

from setuptools import setup, find_packages

# Read the contents of README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements from requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="technical-doc-rewriter",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="AI-powered system for scraping and rewriting technical documentation at multiple difficulty levels",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/technical-doc-rewriter",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/technical-doc-rewriter/issues",
        "Documentation": "https://github.com/yourusername/technical-doc-rewriter#readme",
        "Source Code": "https://github.com/yourusername/technical-doc-rewriter",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
            "pre-commit>=3.4.0",
        ],
        "api": [
            "flask>=2.3.0",
            "gunicorn>=21.0.0",
        ],
        "async": [
            "aiohttp>=3.8.0",
            "asyncio-throttle>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "doc-rewriter=technical_doc_rewriter.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "documentation",
        "scraping",
        "ai",
        "openai",
        "azure",
        "content-rewriting",
        "accessibility",
        "education",
        "technical-writing",
        "nlp",
    ],
)
