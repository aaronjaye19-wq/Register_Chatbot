"""
FAQItem Class - Demonstrates ENCAPSULATION and DATA ABSTRACTION

OOP Principles Applied:
1. ENCAPSULATION - Data (question, answer, keywords) is bundled with methods
2. DATA ABSTRACTION - Exposes only necessary information through public methods
3. SINGLE RESPONSIBILITY PRINCIPLE - Class has one clear purpose: represent an FAQ item
"""

class FAQItem:
    """
    Represents a single FAQ entry with question, answer, and keywords.

    OOP Principle: ENCAPSULATION
    - Private-like attributes (using Python convention with _)
    - Data is accessed through methods, not directly
    """

    def __init__(self, question, answer, keywords):
        """
        Constructor method - OOP PRINCIPLE: ENCAPSULATION

        Args:
            question (str): The FAQ question
            answer (str): The answer to the question
            keywords (list): List of keywords to match this FAQ
        """
        self._question = question
        self._answer = answer
        self._keywords = [keyword.lower() for keyword in keywords]

    def get_question(self):
        """
        Getter method - OOP PRINCIPLE: ENCAPSULATION
        Provides controlled access to private data

        Returns:
            str: The FAQ question
        """
        return self._question

    def get_answer(self):
        """
        Getter method - OOP PRINCIPLE: ENCAPSULATION
        Provides controlled access to private data

        Returns:
            str: The FAQ answer
        """
        return self._answer

    def get_keywords(self):
        """
        Getter method - OOP PRINCIPLE: ENCAPSULATION
        Provides controlled access to private data

        Returns:
            list: List of keywords
        """
        return self._keywords

    def matches_query(self, query):
        """
        Check if this FAQ matches the user's query

        OOP PRINCIPLE: ABSTRACTION
        - Hides the complexity of keyword matching
        - Provides simple interface for checking matches

        Args:
            query (str): User's input query

        Returns:
            int: Number of keyword matches found
        """
        query_lower = query.lower()
        match_count = 0

        for keyword in self._keywords:
            if keyword in query_lower:
                match_count += 1

        return match_count

    def __str__(self):
        """
        String representation - OOP PRINCIPLE: POLYMORPHISM
        Overrides default __str__ method for better representation

        Returns:
            str: String representation of the FAQ item
        """
        return f"FAQ: {self._question}"

    def __repr__(self):
        """
        Object representation - OOP PRINCIPLE: POLYMORPHISM
        Overrides default __repr__ method

        Returns:
            str: Detailed representation of the FAQ item
        """
        return f"FAQItem(question='{self._question}', keywords={self._keywords})"