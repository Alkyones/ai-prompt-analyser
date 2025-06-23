"""
Utility functions for the AI Prompt Analyzer and Optimizer
"""

import json
import csv
from datetime import datetime
from typing import List, Dict, Any
from pathlib import Path


def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Load configuration from JSON file
    
    Args:
        config_path: Path to configuration file
        
    Returns:
        Configuration dictionary
    """
    default_config = {
        "output_format": "text",
        "save_history": True,
        "verbose": False,
        "scoring_weights": {
            "clarity": 1.0,
            "specificity": 1.0,
            "structure": 1.0,
            "context": 1.0,
            "creativity": 1.0
        }
    }
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return {**default_config, **config}
    except FileNotFoundError:
        return default_config
    except json.JSONDecodeError:
        print(f"Warning: Invalid JSON in {config_path}, using default configuration")
        return default_config


def save_analysis_report(results, output_path: str, format_type: str = "auto"):
    """
    Save analysis results to a file
    
    Args:
        results: List of AnalysisResult objects
        output_path: Path to save the report
        format_type: Output format ('json', 'csv', 'txt', or 'auto')
    """
    if format_type == "auto":
        format_type = Path(output_path).suffix.lower()
        if format_type == ".json":
            format_type = "json"
        elif format_type == ".csv":
            format_type = "csv"
        else:
            format_type = "txt"
    
    if format_type == "json":
        _save_json_report(results, output_path)
    elif format_type == "csv":
        _save_csv_report(results, output_path)
    else:
        _save_text_report(results, output_path)


def _save_json_report(results, output_path: str):
    """Save results as JSON"""
    json_data = {
        "generated_at": datetime.now().isoformat(),
        "results": []
    }
    
    for result in results:
        json_data["results"].append({
            "original_prompt": result.original_prompt,
            "optimized_prompt": result.optimized_prompt,
            "scores": {
                "overall": result.overall_score,
                "clarity": result.clarity_score,
                "specificity": result.specificity_score,
                "structure": result.structure_score,
                "context": result.context_score,
                "creativity": result.creativity_score
            },
            "feedback": {
                "strengths": result.strengths,
                "weaknesses": result.weaknesses,
                "suggestions": result.suggestions
            }
        })
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)


def _save_csv_report(results, output_path: str):
    """Save results as CSV"""
    fieldnames = [
        'original_prompt', 'optimized_prompt', 'overall_score',
        'clarity_score', 'specificity_score', 'structure_score',
        'context_score', 'creativity_score', 'strengths',
        'weaknesses', 'suggestions'
    ]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for result in results:
            writer.writerow({
                'original_prompt': result.original_prompt,
                'optimized_prompt': result.optimized_prompt,
                'overall_score': result.overall_score,
                'clarity_score': result.clarity_score,
                'specificity_score': result.specificity_score,
                'structure_score': result.structure_score,
                'context_score': result.context_score,
                'creativity_score': result.creativity_score,
                'strengths': '; '.join(result.strengths),
                'weaknesses': '; '.join(result.weaknesses),
                'suggestions': '; '.join(result.suggestions)
            })


def _save_text_report(results, output_path: str):
    """Save results as formatted text"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("AI PROMPT ANALYSIS REPORT\n")
        f.write("=" * 50 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Prompts Analyzed: {len(results)}\n\n")
        
        for i, result in enumerate(results, 1):
            f.write(f"ANALYSIS {i}\n")
            f.write("-" * 20 + "\n\n")
            
            f.write("ORIGINAL PROMPT:\n")
            f.write(f"{result.original_prompt}\n\n")
            
            f.write("OPTIMIZED PROMPT:\n")
            f.write(f"{result.optimized_prompt}\n\n")
            
            f.write("SCORES:\n")
            f.write(f"Overall: {result.overall_score:.1f}/10\n")
            f.write(f"Clarity: {result.clarity_score:.1f}/10\n")
            f.write(f"Specificity: {result.specificity_score:.1f}/10\n")
            f.write(f"Structure: {result.structure_score:.1f}/10\n")
            f.write(f"Context: {result.context_score:.1f}/10\n")
            f.write(f"Creativity: {result.creativity_score:.1f}/10\n\n")
            
            f.write("STRENGTHS:\n")
            for strength in result.strengths:
                f.write(f"• {strength}\n")
            f.write("\n")
            
            f.write("WEAKNESSES:\n")
            for weakness in result.weaknesses:
                f.write(f"• {weakness}\n")
            f.write("\n")
            
            f.write("SUGGESTIONS:\n")
            for suggestion in result.suggestions:
                f.write(f"• {suggestion}\n")
            f.write("\n")
            
            if i < len(results):
                f.write("=" * 50 + "\n\n")


def validate_prompt(prompt: str) -> tuple[bool, str]:
    """
    Validate a prompt before analysis
    
    Args:
        prompt: The prompt to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not prompt or not prompt.strip():
        return False, "Prompt cannot be empty"
    
    if len(prompt.strip()) < 3:
        return False, "Prompt is too short (minimum 3 characters)"
    
    if len(prompt) > 10000:
        return False, "Prompt is too long (maximum 10,000 characters)"
    
    # Check for potentially problematic content
    if prompt.strip().lower() in ['test', 'hello', 'hi', '123']:
        return False, "Prompt appears to be a test input rather than a real prompt"
    
    return True, ""


def format_score(score: float) -> str:
    """Format a score for display"""
    return f"{score:.1f}"


def get_score_color(score: float) -> str:
    """Get color code for score display (for future terminal coloring)"""
    if score >= 8.0:
        return "green"
    elif score >= 6.0:
        return "yellow"
    else:
        return "red"


def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate text for display purposes"""
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."


def count_words(text: str) -> int:
    """Count words in text"""
    return len(text.split())


def count_sentences(text: str) -> int:
    """Count sentences in text"""
    import re
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])


def get_readability_stats(text: str) -> Dict[str, Any]:
    """Get basic readability statistics"""
    words = text.split()
    sentences = count_sentences(text)
    
    if sentences == 0:
        return {
            "word_count": len(words),
            "sentence_count": 0,
            "avg_words_per_sentence": 0,
            "avg_characters_per_word": sum(len(word) for word in words) / max(len(words), 1)
        }
    
    return {
        "word_count": len(words),
        "sentence_count": sentences,
        "avg_words_per_sentence": len(words) / sentences,
        "avg_characters_per_word": sum(len(word) for word in words) / max(len(words), 1)
    }


def create_sample_prompts() -> List[str]:
    """Create sample prompts for testing"""
    return [
        "Write a story about a robot.",
        
        "Please write a comprehensive 500-word story about a robot who discovers emotions for the first time. The story should be written for a young adult audience, include dialogue, and follow a clear three-act structure with an introduction, conflict, and resolution. Focus on the robot's internal journey and use descriptive language to create an engaging narrative.",
        
        "Explain machine learning.",
        
        "As an expert data scientist, please explain machine learning concepts to a business executive audience. Your explanation should cover: 1) What machine learning is in simple terms, 2) Three main types of machine learning with real-world examples, 3) Key benefits and limitations, 4) How it differs from traditional programming. Keep the explanation concise (300-400 words) and avoid technical jargon. Include practical examples from business contexts like marketing, finance, or operations.",
        
        "Help me with my project.",
        
        "I'm working on a web development project for a small business website and need guidance on the following specific areas: 1) Choosing between React and Vue.js for the frontend, 2) Selecting a suitable backend framework (considering Node.js, Django, or Rails), 3) Database recommendations for storing customer information and product catalog, 4) Best practices for implementing user authentication and security. The website will have approximately 1000 products and expect 500 daily users. Please provide detailed recommendations with pros and cons for each option."
    ]
