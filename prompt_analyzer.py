"""
Prompt Analyzer Module

This module contains the PromptAnalyzer class which evaluates prompts
based on various criteria such as clarity, specificity, structure, 
context, and creativity.
"""

import re
import statistics
from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class AnalysisMetrics:
    """Data structure to hold analysis metrics"""
    clarity_score: float
    specificity_score: float
    structure_score: float
    context_score: float
    creativity_score: float
    overall_score: float
    detailed_feedback: Dict[str, List[str]]


class PromptAnalyzer:
    """Analyzes prompts based on multiple criteria"""
    
    def __init__(self):
        """Initialize the analyzer with predefined patterns and keywords"""
        self.clarity_indicators = {
            'positive': [
                'clearly', 'specifically', 'exactly', 'precisely', 'detailed',
                'explain', 'describe', 'analyze', 'compare', 'contrast',
                'step-by-step', 'in detail', 'thoroughly'
            ],
            'negative': [
                'something', 'anything', 'stuff', 'things', 'maybe', 'perhaps',
                'sort of', 'kind of', 'whatever', 'somehow', 'general'
            ]
        }
        
        self.specificity_indicators = {
            'positive': [
                'format:', 'length:', 'style:', 'tone:', 'audience:', 'purpose:',
                'requirements:', 'constraints:', 'examples:', 'criteria:',
                'must include', 'should contain', 'exactly', 'precisely'
            ],
            'negative': [
                'general', 'broad', 'overview', 'basic', 'simple', 'easy',
                'quick', 'brief', 'short'
            ]
        }
        
        self.structure_indicators = {
            'positive': [
                'first', 'second', 'third', 'finally', 'next', 'then',
                'step 1', 'step 2', 'bullet points', 'numbered list',
                'introduction', 'conclusion', 'summary'
            ]
        }
        
        self.context_indicators = {
            'positive': [
                'background:', 'context:', 'given that', 'assuming',
                'in the context of', 'for the purpose of', 'target audience',
                'use case', 'scenario', 'situation'
            ]
        }
        
        self.creativity_indicators = {
            'positive': [
                'creative', 'innovative', 'unique', 'original', 'imaginative',
                'brainstorm', 'generate ideas', 'think outside', 'alternative',
                'unconventional', 'novel', 'fresh perspective'
            ],
            'negative': [
                'standard', 'typical', 'usual', 'conventional', 'traditional',
                'common', 'ordinary', 'basic', 'simple'
            ]
        }
    
    def analyze(self, prompt: str) -> AnalysisMetrics:
        """
        Analyze a prompt and return detailed metrics
        
        Args:
            prompt: The prompt text to analyze
            
        Returns:
            AnalysisMetrics object containing scores and feedback
        """
        prompt_lower = prompt.lower()
        
        # Calculate individual scores
        clarity_score = self._analyze_clarity(prompt, prompt_lower)
        specificity_score = self._analyze_specificity(prompt, prompt_lower)
        structure_score = self._analyze_structure(prompt, prompt_lower)
        context_score = self._analyze_context(prompt, prompt_lower)
        creativity_score = self._analyze_creativity(prompt, prompt_lower)
        
        # Calculate overall score
        scores = [clarity_score, specificity_score, structure_score, context_score, creativity_score]
        overall_score = statistics.mean(scores)
        
        # Generate detailed feedback
        detailed_feedback = self._generate_detailed_feedback(
            prompt, prompt_lower, {
                'clarity': clarity_score,
                'specificity': specificity_score,
                'structure': structure_score,
                'context': context_score,
                'creativity': creativity_score
            }
        )
        
        return AnalysisMetrics(
            clarity_score=clarity_score,
            specificity_score=specificity_score,
            structure_score=structure_score,
            context_score=context_score,
            creativity_score=creativity_score,
            overall_score=overall_score,
            detailed_feedback=detailed_feedback
        )
    
    def _analyze_clarity(self, prompt: str, prompt_lower: str) -> float:
        """Analyze prompt clarity"""
        score = 5.0  # Base score
        
        # Check for clarity indicators
        positive_count = sum(1 for indicator in self.clarity_indicators['positive'] 
                           if indicator in prompt_lower)
        negative_count = sum(1 for indicator in self.clarity_indicators['negative'] 
                           if indicator in prompt_lower)
        
        # Adjust score based on indicators
        score += min(positive_count * 0.5, 3.0)
        score -= min(negative_count * 0.8, 3.0)
        
        # Check for question marks (good for clarity)
        question_count = prompt.count('?')
        if question_count > 0:
            score += min(question_count * 0.3, 1.0)
        
        # Check for ambiguous pronouns
        ambiguous_pronouns = ['it', 'this', 'that', 'they', 'them']
        ambiguous_count = sum(1 for pronoun in ambiguous_pronouns 
                            if f' {pronoun} ' in prompt_lower)
        score -= min(ambiguous_count * 0.2, 1.5)
        
        # Check sentence length (very long sentences reduce clarity)
        sentences = re.split(r'[.!?]+', prompt)
        avg_sentence_length = sum(len(s.split()) for s in sentences if s.strip()) / max(len([s for s in sentences if s.strip()]), 1)
        if avg_sentence_length > 25:
            score -= 1.0
        elif avg_sentence_length > 35:
            score -= 2.0
        
        return max(0.0, min(10.0, score))
    
    def _analyze_specificity(self, prompt: str, prompt_lower: str) -> float:
        """Analyze prompt specificity"""
        score = 4.0  # Base score
        
        # Check for specificity indicators
        positive_count = sum(1 for indicator in self.specificity_indicators['positive'] 
                           if indicator in prompt_lower)
        negative_count = sum(1 for indicator in self.specificity_indicators['negative'] 
                           if indicator in prompt_lower)
        
        score += min(positive_count * 0.8, 4.0)
        score -= min(negative_count * 0.6, 2.0)
        
        # Check for numbers and specific quantities
        number_count = len(re.findall(r'\b\d+\b', prompt))
        score += min(number_count * 0.3, 2.0)
        
        # Check for specific formats mentioned
        format_keywords = ['json', 'csv', 'xml', 'markdown', 'html', 'list', 'table', 'paragraph']
        format_count = sum(1 for keyword in format_keywords if keyword in prompt_lower)
        score += min(format_count * 0.5, 1.5)
        
        # Check for examples
        if 'example' in prompt_lower or 'for instance' in prompt_lower:
            score += 1.0
        
        return max(0.0, min(10.0, score))
    
    def _analyze_structure(self, prompt: str, prompt_lower: str) -> float:
        """Analyze prompt structure"""
        score = 5.0  # Base score
        
        # Check for structural indicators
        structure_count = sum(1 for indicator in self.structure_indicators['positive'] 
                            if indicator in prompt_lower)
        score += min(structure_count * 0.6, 3.0)
        
        # Check for bullet points or numbered lists
        if re.search(r'^\s*[-*•]\s', prompt, re.MULTILINE):
            score += 1.0
        if re.search(r'^\s*\d+\.\s', prompt, re.MULTILINE):
            score += 1.0
        
        # Check for sections or headers
        if re.search(r'^[A-Z][^.!?]*:$', prompt, re.MULTILINE):
            score += 0.5
        
        # Check for logical flow
        transition_words = ['however', 'therefore', 'furthermore', 'moreover', 'additionally', 'consequently']
        transition_count = sum(1 for word in transition_words if word in prompt_lower)
        score += min(transition_count * 0.3, 1.0)
        
        # Penalize if prompt is just one long paragraph
        paragraph_count = len([p for p in prompt.split('\n\n') if p.strip()])
        if paragraph_count == 1 and len(prompt.split()) > 50:
            score -= 1.5
        
        return max(0.0, min(10.0, score))
    
    def _analyze_context(self, prompt: str, prompt_lower: str) -> float:
        """Analyze prompt context"""
        score = 4.0  # Base score
        
        # Check for context indicators
        context_count = sum(1 for indicator in self.context_indicators['positive'] 
                          if indicator in prompt_lower)
        score += min(context_count * 1.0, 4.0)
        
        # Check for role definition
        role_keywords = ['you are', 'act as', 'pretend to be', 'imagine you are', 'role:', 'persona:']
        if any(keyword in prompt_lower for keyword in role_keywords):
            score += 1.5
        
        # Check for domain-specific terminology
        domains = ['technical', 'medical', 'legal', 'financial', 'academic', 'creative', 'business']
        domain_count = sum(1 for domain in domains if domain in prompt_lower)
        score += min(domain_count * 0.4, 1.0)
        
        # Check for constraints or requirements
        constraint_keywords = ['must', 'should', 'cannot', 'avoid', 'include', 'exclude', 'limit', 'maximum', 'minimum']
        constraint_count = sum(1 for keyword in constraint_keywords if keyword in prompt_lower)
        score += min(constraint_count * 0.2, 1.5)
        
        return max(0.0, min(10.0, score))
    
    def _analyze_creativity(self, prompt: str, prompt_lower: str) -> float:
        """Analyze prompt creativity encouragement"""
        score = 5.0  # Base score
        
        # Check for creativity indicators
        positive_count = sum(1 for indicator in self.creativity_indicators['positive'] 
                           if indicator in prompt_lower)
        negative_count = sum(1 for indicator in self.creativity_indicators['negative'] 
                           if indicator in prompt_lower)
        
        score += min(positive_count * 0.8, 3.0)
        score -= min(negative_count * 0.5, 2.0)
        
        # Check for open-ended questions
        open_questions = ['what if', 'how might', 'what could', 'imagine', 'suppose']
        open_count = sum(1 for question in open_questions if question in prompt_lower)
        score += min(open_count * 0.6, 2.0)
        
        # Check for multiple perspectives requested
        perspective_keywords = ['different ways', 'various approaches', 'multiple solutions', 'alternatives']
        if any(keyword in prompt_lower for keyword in perspective_keywords):
            score += 1.0
        
        # Penalize overly restrictive prompts
        restrictive_keywords = ['only', 'exactly', 'precisely', 'must be', 'required']
        restrictive_count = sum(1 for keyword in restrictive_keywords if keyword in prompt_lower)
        if restrictive_count > 3:
            score -= 1.0
        
        return max(0.0, min(10.0, score))
    
    def _generate_detailed_feedback(self, prompt: str, prompt_lower: str, scores: Dict[str, float]) -> Dict[str, List[str]]:
        """Generate detailed feedback for each category"""
        feedback = {
            'clarity': [],
            'specificity': [],
            'structure': [],
            'context': [],
            'creativity': []
        }
        
        # Clarity feedback
        if scores['clarity'] < 6.0:
            feedback['clarity'].extend([
                "Consider using more specific and clear language",
                "Avoid ambiguous pronouns like 'it', 'this', 'that'",
                "Break down complex sentences into simpler ones"
            ])
        if scores['clarity'] >= 8.0:
            feedback['clarity'].append("Prompt demonstrates excellent clarity")
        
        # Specificity feedback
        if scores['specificity'] < 6.0:
            feedback['specificity'].extend([
                "Add specific requirements or constraints",
                "Include desired format, length, or style",
                "Provide examples of expected output"
            ])
        if scores['specificity'] >= 8.0:
            feedback['specificity'].append("Prompt is highly specific and detailed")
        
        # Structure feedback
        if scores['structure'] < 6.0:
            feedback['structure'].extend([
                "Organize the prompt with clear sections",
                "Use bullet points or numbered lists for multiple requirements",
                "Add transition words to improve flow"
            ])
        if scores['structure'] >= 8.0:
            feedback['structure'].append("Prompt is well-structured and organized")
        
        # Context feedback
        if scores['context'] < 6.0:
            feedback['context'].extend([
                "Provide more background information",
                "Define the role or persona for the AI",
                "Specify the target audience or use case"
            ])
        if scores['context'] >= 8.0:
            feedback['context'].append("Prompt provides excellent context")
        
        # Creativity feedback
        if scores['creativity'] < 6.0:
            feedback['creativity'].extend([
                "Encourage creative and innovative responses",
                "Ask for multiple alternatives or approaches",
                "Use open-ended questions to inspire creativity"
            ])
        if scores['creativity'] >= 8.0:
            feedback['creativity'].append("Prompt effectively encourages creativity")
        
        return feedback
