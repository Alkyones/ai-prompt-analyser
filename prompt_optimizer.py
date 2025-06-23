"""
Prompt Optimizer Module

This module contains the PromptOptimizer class which takes analysis results
and generates optimized versions of prompts along with specific feedback.
"""

import re
from typing import List, Dict
from dataclasses import dataclass
from prompt_analyzer import AnalysisMetrics


@dataclass
class OptimizationResult:
    """Data structure to hold optimization results"""
    optimized_prompt: str
    strengths: List[str]
    weaknesses: List[str]
    suggestions: List[str]


class PromptOptimizer:
    """Optimizes prompts based on analysis results"""
    
    def __init__(self):
        """Initialize the optimizer with improvement strategies"""
        self.optimization_strategies = {
            'clarity': self._optimize_clarity,
            'specificity': self._optimize_specificity,
            'structure': self._optimize_structure,
            'context': self._optimize_context,
            'creativity': self._optimize_creativity
        }
        
        self.general_tips = [
            "Use active voice instead of passive voice when possible",
            "Be specific about the desired output format",
            "Include examples when helpful",
            "Define technical terms or jargon",
            "Specify the target audience",
            "Break complex requests into smaller parts",
            "Use clear, actionable verbs",
            "Provide context and background information",
            "Set clear expectations and constraints",
            "Encourage creative thinking when appropriate"
        ]
    
    def optimize(self, original_prompt: str, analysis: AnalysisMetrics) -> OptimizationResult:
        """
        Optimize a prompt based on analysis results
        
        Args:
            original_prompt: The original prompt text
            analysis: Analysis results from PromptAnalyzer
            
        Returns:
            OptimizationResult with optimized prompt and feedback
        """
        # Start with the original prompt
        optimized = original_prompt
        applied_optimizations = []
        
        # Apply optimizations based on low scores
        scores = {
            'clarity': analysis.clarity_score,
            'specificity': analysis.specificity_score,
            'structure': analysis.structure_score,
            'context': analysis.context_score,
            'creativity': analysis.creativity_score
        }
        
        # Sort by lowest scores first to prioritize improvements
        sorted_scores = sorted(scores.items(), key=lambda x: x[1])
        
        for category, score in sorted_scores:
            if score < 7.0:  # Apply optimization if score is below 7
                try:
                    optimized, improvements = self.optimization_strategies[category](optimized, score)
                    applied_optimizations.extend(improvements)
                except Exception as e:
                    # Continue with other optimizations if one fails
                    continue
        
        # Generate strengths, weaknesses, and suggestions
        strengths = self._identify_strengths(original_prompt, analysis)
        weaknesses = self._identify_weaknesses(original_prompt, analysis)
        suggestions = self._generate_suggestions(analysis, applied_optimizations)
        
        return OptimizationResult(
            optimized_prompt=optimized,
            strengths=strengths,
            weaknesses=weaknesses,
            suggestions=suggestions
        )
    
    def _optimize_clarity(self, prompt: str, score: float) -> tuple[str, List[str]]:
        """Optimize prompt clarity"""
        improvements = []
        optimized = prompt
          # Replace ambiguous pronouns (only when they appear to be ambiguous)
        ambiguous_replacements = {
            ' it ': ' the item ',
            ' they ': ' these items ',
            ' them ': ' these elements '
        }
        
        for ambiguous, replacement in ambiguous_replacements.items():
            if ambiguous in optimized.lower():
                optimized = re.sub(ambiguous, replacement, optimized, flags=re.IGNORECASE)
                improvements.append("Replaced ambiguous pronouns with specific terms")
                break
        
        # Break down overly long sentences
        sentences = re.split(r'([.!?]+)', optimized)
        new_sentences = []
        
        for i in range(0, len(sentences), 2):
            if i < len(sentences):
                sentence = sentences[i].strip()
                if len(sentence.split()) > 30:
                    # Try to split at conjunctions
                    if ' and ' in sentence:
                        parts = sentence.split(' and ', 1)
                        new_sentences.append(parts[0] + '.')
                        new_sentences.append('Additionally, ' + parts[1])
                        improvements.append("Broke down long sentences for better clarity")
                    else:
                        new_sentences.append(sentence)
                else:
                    new_sentences.append(sentence)
                
                # Add punctuation back
                if i + 1 < len(sentences):
                    new_sentences.append(sentences[i + 1])
        
        if improvements:
            optimized = ''.join(new_sentences)
        
        # Add clarity enhancers if score is very low
        if score < 5.0:
            if not optimized.strip().endswith('?') and 'please' not in optimized.lower():
                optimized = "Please " + optimized[0].lower() + optimized[1:]
                improvements.append("Added polite language for clarity")
        
        return optimized, improvements
    
    def _optimize_specificity(self, prompt: str, score: float) -> tuple[str, List[str]]:
        """Optimize prompt specificity"""
        improvements = []
        optimized = prompt
        
        # Add format specification if missing
        format_keywords = ['format', 'json', 'csv', 'list', 'paragraph', 'table']
        if not any(keyword in optimized.lower() for keyword in format_keywords):
            optimized += "\n\nFormat: Please provide your response in a clear, structured format."
            improvements.append("Added format specification")
        
        # Add length specification if missing
        length_keywords = ['length', 'words', 'sentences', 'paragraphs', 'brief', 'detailed']
        if not any(keyword in optimized.lower() for keyword in length_keywords):
            optimized += "\n\nLength: Provide a comprehensive response with sufficient detail."
            improvements.append("Added length guideline")
        
        # Add constraints section if score is very low
        if score < 4.0:
            if 'requirements:' not in optimized.lower() and 'constraints:' not in optimized.lower():
                optimized += "\n\nRequirements:\n- Be specific and detailed\n- Include relevant examples\n- Address all aspects of the request"
                improvements.append("Added specific requirements")
        
        return optimized, improvements
    
    def _optimize_structure(self, prompt: str, score: float) -> tuple[str, List[str]]:
        """Optimize prompt structure"""
        improvements = []
        optimized = prompt
        
        # Add structure if prompt is one long paragraph
        if '\n' not in optimized.strip() and len(optimized.split()) > 50:
            # Try to identify different parts of the request
            parts = []
            current_part = []
            
            sentences = re.split(r'[.!?]+', optimized)
            for sentence in sentences:
                sentence = sentence.strip()
                if sentence:
                    current_part.append(sentence)
                    
                    # If we detect a new instruction type, start a new part
                    instruction_starters = ['please', 'also', 'additionally', 'furthermore', 'include', 'make sure']
                    if any(sentence.lower().startswith(starter) for starter in instruction_starters):
                        if len(current_part) > 1:
                            parts.append('. '.join(current_part[:-1]) + '.')
                            current_part = [current_part[-1]]
            
            if current_part:
                parts.append('. '.join(current_part) + '.')
            
            if len(parts) > 1:
                optimized = '\n\n'.join(parts)
                improvements.append("Restructured into clear paragraphs")
        
        # Add section headers if missing and content is complex
        if len(optimized.split()) > 100 and ':' not in optimized:
            # Check if we can identify task and requirements
            lines = optimized.split('\n')
            if len(lines) <= 2:
                optimized = "Task:\n" + optimized + "\n\nInstructions:\nPlease ensure your response is comprehensive and well-structured."
                improvements.append("Added clear section headers")
        
        return optimized, improvements
    
    def _optimize_context(self, prompt: str, score: float) -> tuple[str, List[str]]:
        """Optimize prompt context"""
        improvements = []
        optimized = prompt
        
        # Add role definition if missing
        role_keywords = ['you are', 'act as', 'pretend', 'imagine you', 'role:']
        if not any(keyword in optimized.lower() for keyword in role_keywords):
            optimized = "Context: You are an expert assistant helping with this task.\n\n" + optimized
            improvements.append("Added role context")
        
        # Add purpose if missing
        purpose_keywords = ['purpose:', 'goal:', 'objective:', 'for the purpose', 'in order to']
        if not any(keyword in optimized.lower() for keyword in purpose_keywords):
            optimized += "\n\nPurpose: This information will be used to provide accurate and helpful guidance."
            improvements.append("Added purpose statement")
        
        # Add audience context if score is very low
        if score < 4.0:
            audience_keywords = ['audience:', 'for', 'target', 'readers', 'users']
            if not any(keyword in optimized.lower() for keyword in audience_keywords):
                optimized += "\n\nAudience: General audience seeking clear and actionable information."
                improvements.append("Added audience context")
        
        return optimized, improvements
    
    def _optimize_creativity(self, prompt: str, score: float) -> tuple[str, List[str]]:
        """Optimize prompt creativity encouragement"""
        improvements = []
        optimized = prompt
        
        # Add creativity encouragement if missing
        creative_keywords = ['creative', 'innovative', 'unique', 'original', 'think outside']
        if not any(keyword in optimized.lower() for keyword in creative_keywords):
            optimized += "\n\nApproach: Feel free to be creative and think of innovative solutions."
            improvements.append("Added creativity encouragement")
        
        # Add request for alternatives if score is low
        if score < 5.0:
            alternative_keywords = ['alternatives', 'different ways', 'various approaches', 'multiple']
            if not any(keyword in optimized.lower() for keyword in alternative_keywords):
                optimized += "\n\nAdditional: Please consider multiple approaches and provide alternatives where applicable."
                improvements.append("Encouraged multiple perspectives")
        
        # Transform restrictive language if too many constraints
        restrictive_count = len(re.findall(r'\b(only|exactly|precisely|must be|required)\b', optimized, re.IGNORECASE))
        if restrictive_count > 3:
            optimized = re.sub(r'\bonly\b', 'primarily', optimized, flags=re.IGNORECASE, count=1)
            optimized = re.sub(r'\bexactly\b', 'preferably', optimized, flags=re.IGNORECASE, count=1)
            improvements.append("Softened restrictive language to encourage creativity")
        
        return optimized, improvements
    
    def _identify_strengths(self, prompt: str, analysis: AnalysisMetrics) -> List[str]:
        """Identify strengths in the original prompt"""
        strengths = []
        
        if analysis.clarity_score >= 7.0:
            strengths.append("Clear and unambiguous language")
        
        if analysis.specificity_score >= 7.0:
            strengths.append("Specific requirements and detailed instructions")
        
        if analysis.structure_score >= 7.0:
            strengths.append("Well-organized and logically structured")
        
        if analysis.context_score >= 7.0:
            strengths.append("Provides sufficient background and context")
        
        if analysis.creativity_score >= 7.0:
            strengths.append("Encourages creative and innovative thinking")
        
        # Check for specific good practices
        if '?' in prompt:
            strengths.append("Uses questions to guide response")
        
        if 'example' in prompt.lower():
            strengths.append("Includes examples for clarification")
        
        if len(prompt.split('\n\n')) > 1:
            strengths.append("Uses paragraphs for better organization")
        
        if not strengths:
            strengths.append("Shows clear intent to communicate a request")
        
        return strengths
    
    def _identify_weaknesses(self, prompt: str, analysis: AnalysisMetrics) -> List[str]:
        """Identify weaknesses in the original prompt"""
        weaknesses = []
        
        if analysis.clarity_score < 6.0:
            weaknesses.append("Could be clearer and less ambiguous")
        
        if analysis.specificity_score < 6.0:
            weaknesses.append("Lacks specific requirements and constraints")
        
        if analysis.structure_score < 6.0:
            weaknesses.append("Could benefit from better organization")
        
        if analysis.context_score < 6.0:
            weaknesses.append("Needs more background information and context")
        
        if analysis.creativity_score < 6.0:
            weaknesses.append("Could better encourage creative responses")
        
        # Check for specific issues
        if len(prompt.split()) < 10:
            weaknesses.append("Too brief - could provide more detail")
        
        if len(prompt.split()) > 200:
            weaknesses.append("Quite lengthy - consider breaking into sections")
        
        ambiguous_pronouns = ['it', 'this', 'that', 'they', 'them']
        if any(f' {pronoun} ' in prompt.lower() for pronoun in ambiguous_pronouns):
            weaknesses.append("Contains ambiguous pronouns")
        
        return weaknesses
    
    def _generate_suggestions(self, analysis: AnalysisMetrics, applied_optimizations: List[str]) -> List[str]:
        """Generate suggestions for future prompt writing"""
        suggestions = []
        
        # Category-specific suggestions based on scores
        if analysis.clarity_score < 7.0:
            suggestions.extend([
                "Use specific nouns instead of pronouns when possible",
                "Keep sentences concise and focused",
                "Define any technical terms or jargon"
            ])
        
        if analysis.specificity_score < 7.0:
            suggestions.extend([
                "Specify the desired format for the response",
                "Include length or scope requirements",
                "Provide examples of what you're looking for"
            ])
        
        if analysis.structure_score < 7.0:
            suggestions.extend([
                "Use bullet points or numbered lists for multiple requirements",
                "Organize complex prompts into clear sections",
                "Use headers to separate different types of instructions"
            ])
        
        if analysis.context_score < 7.0:
            suggestions.extend([
                "Provide background information about the task",
                "Define the role you want the AI to assume",
                "Specify the target audience for the response"
            ])
        
        if analysis.creativity_score < 7.0:
            suggestions.extend([
                "Ask for multiple approaches or alternatives",
                "Use open-ended questions to encourage exploration",
                "Avoid overly restrictive constraints unless necessary"
            ])
        
        # Add general best practices
        suggestions.extend([
            "Test your prompts with different phrasings to see what works best",
            "Consider the AI's perspective when crafting instructions",
            "Be explicit about what you want rather than assuming the AI will infer it"
        ])
        
        # Remove duplicates and limit to most relevant suggestions
        suggestions = list(dict.fromkeys(suggestions))[:8]
        
        return suggestions
