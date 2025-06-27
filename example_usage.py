"""
Technical Documentation Scraper & Multi-Level Content Rewriter

A comprehensive example showing how to use all components of the system.
"""

import json
import time
from datetime import datetime
from pathlib import Path

# Import your modules (adjust import paths as needed)
from scraper_rewriter import (
    scrape_sections,
    difficulty,
    intermediate_rewrite,
    beginner_rewrite,
    summarizer_func
)


def process_complete_documentation(url: str, output_dir: str = "output") -> dict:
    """
    Complete processing pipeline for a documentation URL.
    
    Args:
        url: URL to process
        output_dir: Directory to save output files
        
    Returns:
        Dictionary containing all processed content
    """
    print(f"🚀 Starting to process: {url}")
    start_time = time.time()
    
    # Create output directory
    Path(output_dir).mkdir(exist_ok=True)
    
    try:
        # Step 1: Web Scraping
        print("📄 Scraping webpage content...")
        sections = scrape_sections(url)
        print(f"✅ Extracted {len(sections)} sections")
        
        # Step 2: Difficulty Analysis
        print("🔍 Analyzing content difficulty...")
        difficulty(sections)
        print("✅ Difficulty analysis complete")
        
        # Step 3: Content Rewriting
        print("✏️ Rewriting content for different levels...")
        
        # Intermediate level
        print("  - Generating intermediate level content...")
        sections_intermediate = intermediate_rewrite(sections)
        
        # Beginner level
        print("  - Generating beginner level content...")
        sections_beginner = beginner_rewrite(sections)
        
        # Advanced level (original HTML)
        print("  - Preparing advanced level content...")
        advanced_sections = []
        for sec in sections:
            new_sec = {
                'id': sec['id'],
                'title': sec['title'],
                'content': [{'type': 'paragraph', 'text': sec['html']}]
            }
            advanced_sections.append(new_sec)
        
        print("✅ Content rewriting complete")
        
        # Step 4: Summarization
        print("📝 Generating summaries...")
        summaries = summarizer_func(url)
        print("✅ Summaries generated")
        
        # Step 5: Assemble final JSON
        print("🔧 Assembling final output...")
        final_json = assemble_final_output(
            url, sections_beginner, sections_intermediate, 
            advanced_sections, summaries
        )
        
        # Save to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{output_dir}/processed_documentation_{timestamp}.json"
        
        with open(output_filename, "w", encoding="utf-8") as f:
            json.dump(final_json, f, ensure_ascii=False, indent=2)
        
        processing_time = time.time() - start_time
        print(f"✅ Processing complete! Saved to: {output_filename}")
        print(f"⏱️ Total processing time: {processing_time:.2f} seconds")
        
        return final_json
        
    except Exception as e:
        print(f"❌ Error processing documentation: {e}")
        raise


def assemble_final_output(url: str, beginner_sections: list, intermediate_sections: list, 
                         advanced_sections: list, summaries: dict) -> dict:
    """
    Assemble the final JSON output with all processed content.
    
    Args:
        url: Source URL
        beginner_sections: Beginner-level sections
        intermediate_sections: Intermediate-level sections
        advanced_sections: Advanced-level sections
        summaries: Generated summaries
        
    Returns:
        Complete JSON structure
    """
    # Combine sections with all difficulty levels
    sections_combined = []
    for i in range(len(beginner_sections)):
        section = {
            "id": beginner_sections[i]["id"],
            "title": beginner_sections[i]["title"],
            "content": [
                beginner_sections[i]["content"][0],
                intermediate_sections[i]["content"][0],
                advanced_sections[i]["content"][0]
            ]
        }
        sections_combined.append(section)
    
    # Create final JSON structure
    final_json = {
        "metadata": {
            "source_url": url,
            "processed_at": datetime.now().isoformat(),
            "sections_count": len(sections_combined),
            "difficulty_levels": ["beginner", "intermediate", "advanced"]
        },
        "summaries": {
            "content": [
                {
                    "type": "paragraph",
                    "difficulty": "beginner",
                    "text": summaries['beginner_level_summary']
                },
                {
                    "type": "paragraph",
                    "difficulty": "intermediate",
                    "text": summaries['intermediate_level_summary']
                },
                {
                    "type": "paragraph",
                    "difficulty": "advanced",
                    "text": summaries['advanced_level_summary']
                }
            ]
        },
        "sections": sections_combined
    }
    
    return final_json


def batch_process_urls(urls: list, output_dir: str = "output", delay: int = 5) -> list:
    """
    Process multiple URLs in batch with rate limiting.
    
    Args:
        urls: List of URLs to process
        output_dir: Output directory
        delay: Delay between requests (seconds)
        
    Returns:
        List of processing results
    """
    results = []
    
    print(f"🔄 Starting batch processing of {len(urls)} URLs")
    
    for i, url in enumerate(urls, 1):
        print(f"\n📋 Processing URL {i}/{len(urls)}: {url}")
        
        try:
            result = process_complete_documentation(url, output_dir)
            results.append({
                "url": url,
                "status": "success",
                "result": result
            })
            
        except Exception as e:
            print(f"❌ Failed to process {url}: {e}")
            results.append({
                "url": url,
                "status": "error",
                "error": str(e)
            })
        
        # Rate limiting (except for last URL)
        if i < len(urls):
            print(f"⏳ Waiting {delay} seconds before next request...")
            time.sleep(delay)
    
    # Save batch results summary
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    batch_summary_file = f"{output_dir}/batch_results_{timestamp}.json"
    
    batch_summary = {
        "processed_at": datetime.now().isoformat(),
        "total_urls": len(urls),
        "successful": len([r for r in results if r["status"] == "success"]),
        "failed": len([r for r in results if r["status"] == "error"]),
        "results": results
    }
    
    with open(batch_summary_file, "w", encoding="utf-8") as f:
        json.dump(batch_summary, f, ensure_ascii=False, indent=2)
    
    print(f"\n📊 Batch processing complete! Summary saved to: {batch_summary_file}")
    print(f"✅ Successful: {batch_summary['successful']}/{batch_summary['total_urls']}")
    
    return results


def main():
    """Main function demonstrating usage examples."""
    
    # Example 1: Single URL processing
    print("=" * 60)
    print("EXAMPLE 1: Single URL Processing")
    print("=" * 60)
    
    url = "https://learn.microsoft.com/en-us/azure/load-balancer/gateway-overview"
    
    try:
        result = process_complete_documentation(url)
        print(f"✅ Successfully processed single URL")
        print(f"📊 Generated {len(result['sections'])} sections")
        
    except Exception as e:
        print(f"❌ Single URL processing failed: {e}")
    
    # Example 2: Batch processing
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Batch Processing")
    print("=" * 60)
    
    urls = [
        "https://learn.microsoft.com/en-us/azure/load-balancer/gateway-overview",
        "https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview",
        # Add more URLs as needed
    ]
    
    try:
        batch_results = batch_process_urls(urls, delay=10)  # 10 second delay
        print(f"✅ Batch processing completed")
        
    except Exception as e:
        print(f"❌ Batch processing failed: {e}")
    
    print("\n🎉 All examples completed!")


if __name__ == "__main__":
    main()
