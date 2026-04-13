"""
RegistrarChatbot Class - Demonstrates COMPOSITION and DEPENDENCY INJECTION with ML AI

OOP Principles Applied:
1. COMPOSITION - Uses FAQItem objects to build functionality
2. SINGLE RESPONSIBILITY - Manages chatbot logic and FAQ matching
3. DEPENDENCY INJECTION - FAQ data can be injected from external sources
4. ENCAPSULATION - Internal logic is hidden from external use

Machine Learning Features:
1. TF-IDF Vectorization for semantic understanding
2. Cosine similarity for better query matching
"""

from faq_item import FAQItem
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class RegistrarChatbot:
    """
    Main chatbot class that processes user queries and provides responses.

    OOP Principle: COMPOSITION
    - Contains a collection of FAQItem objects
    - Builds complex functionality from simpler objects
    """

    def __init__(self):
        """
        Constructor - OOP PRINCIPLE: ENCAPSULATION
        Initializes the chatbot with empty FAQ database and ML models
        """
        self._faq_database = []
        self._default_response = "I'm sorry, I don't have information about that. Please contact the registrar office directly at 8:00 AM - 5:00 PM for assistance."
        self._greetings = ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening', 'greetings', 'howdy', 'what\'s up', 'whats up', 'yo', 'sup']
        
        # ML Components
        self._vectorizer = TfidfVectorizer(lowercase=True, stop_words='english')
        self._faq_vectors = None
        self._ml_enabled = False

    def load_faq_data(self):
        """
        Load FAQ data into the chatbot and train ML models

        OOP PRINCIPLE: COMPOSITION
        - Creates and manages FAQItem objects
        - Demonstrates object composition

        OOP PRINCIPLE: SINGLE RESPONSIBILITY
        - This method's only job is to load FAQ data and train ML
        """
        faq_data = [
            {
                "question": "What are the enrollment requirements?",
                "answer": "For enrollment, you need: Good Moral Character (GMC), Form 138, and PSA Birth Certificate.",
                "keywords": ["enroll", "enrollment", "requirements", "requirement", "need", "form 138", "gmc"]
            },
            {
                "question": "How do I request a Transcript of Records (TOR)?",
                "answer": "To request a TOR, you need to pay 65 pesos per page. Processing takes 7 business days.",
                "keywords": ["tor", "transcript", "records", "transcript of records", "cost", "price", "fee"]
            },
            {
                "question": "How long does document processing take?",
                "answer": "Document processing typically takes 7 business days from the date of request.",
                "keywords": ["how long", "days", "processing", "release", "time", "duration", "wait"]
            },
            {
                "question": "What are the graduation requirements?",
                "answer": "For graduation, you need: Form 137, PSA Birth Certificate, and Good Moral Character (GMC).",
                "keywords": ["graduation", "graduate", "requirements", "form 137"]
            },
            {
                "question": "How do I correct records?",
                "answer": "To correct your records, you need to submit your PSA Birth Certificate to the registrar office.",
                "keywords": ["correct", "correction", "error", "wrong", "mistake", "change", "update"]
            },
            {
                "question": "What are the requirements for transferees?",
                "answer": "Transferees need: Form 137, Exit Clearance, and Clearance from previous school.",
                "keywords": ["transfer", "transferee", "shifting", "shift"]
            },
            {
                "question": "How do I add or drop subjects?",
                "answer": "To add or drop subjects, you must follow the adding/dropping schedule set by the registrar office. Please check the academic calendar.",
                "keywords": ["add", "drop", "subject", "subjects", "adding", "dropping"]
            },
            {
                "question": "What are the office hours?",
                "answer": "The Registrar Office is open from 8:00 AM to 5:00 PM, Monday to Friday.",
                "keywords": ["hours", "time", "open", "schedule", "office hours", "when"]
            },
            {
                "question": "How do I address grade concerns?",
                "answer": "For grade concerns, please contact your Registrar College In-Charge directly.",
                "keywords": ["grade", "grades", "grading", "concern", "score", "mark"]
            },
            {
                "question": "How do I get a Certificate of Enrollment?",
                "answer": "To get a Certificate of Enrollment, you need to submit your PSA Birth Certificate to the registrar office.",
                "keywords": ["certificate", "enrollment certificate", "coe", "certification"]
            }
        ]

        for faq in faq_data:
            faq_item = FAQItem(
                question=faq["question"],
                answer=faq["answer"],
                keywords=faq["keywords"]
            )
            self._faq_database.append(faq_item)
        
        # Train ML model with FAQ questions
        self._train_ml_model()

    def is_greeting(self, user_input):
        """
        Check if user input is a greeting

        Args:
            user_input (str): User's input message

        Returns:
            bool: True if input is a greeting, False otherwise
        """
        user_input_lower = user_input.lower().strip()
        
        # Check if the input matches any greeting
        for greeting in self._greetings:
            if greeting in user_input_lower:
                return True
        return False

    def get_faq_list(self):
        """
        Get a formatted list of all available FAQs

        OOP PRINCIPLE: ENCAPSULATION
        - Provides controlled access to FAQ list

        Returns:
            str: Formatted list of FAQ questions
        """
        faq_list = "Here are the topics I can help you with:\n\n"
        for idx, faq_item in enumerate(self._faq_database, 1):
            faq_list += f"{idx}. {faq_item.get_question()}\n"
        return faq_list

    def _train_ml_model(self):
        """
        Train ML model with FAQ questions using TF-IDF vectorization

        ML PRINCIPLE: FEATURE EXTRACTION
        - Uses TF-IDF to convert text into numerical vectors
        - Creates semantic understanding of FAQ content
        """
        try:
            questions = [faq.get_question() for faq in self._faq_database]
            self._faq_vectors = self._vectorizer.fit_transform(questions)
            self._ml_enabled = True
        except Exception as e:
            print(f"ML training error: {e}. Falling back to keyword matching.")
            self._ml_enabled = False

    def _find_best_match_ml(self, user_query):
        """
        Find best match using ML (TF-IDF + Cosine Similarity)

        ML PRINCIPLE: SEMANTIC SIMILARITY
        - Computes cosine similarity between user query and FAQ questions
        - Returns match with highest similarity score

        Args:
            user_query (str): User's input query

        Returns:
            tuple: (best_match_faq, confidence_score)
        """
        if not self._ml_enabled or self._faq_vectors is None:
            return None, 0.0

        try:
            query_vector = self._vectorizer.transform([user_query])
            similarities = cosine_similarity(query_vector, self._faq_vectors)[0]
            best_idx = np.argmax(similarities)
            confidence = similarities[best_idx]

            # Only return if confidence exceeds threshold
            if confidence > 0.2:
                return self._faq_database[best_idx], float(confidence)
        except Exception as e:
            print(f"ML matching error: {e}")

        return None, 0.0

    def find_best_match(self, user_query):
        """
        Find the best matching FAQ using hybrid approach (ML + Keyword)

        OOP PRINCIPLE: ABSTRACTION
        - Hides complex matching algorithm
        - Provides simple interface for finding matches

        HYBRID ML APPROACH:
        1. First tries ML-based semantic matching (TF-IDF)
        2. Falls back to keyword matching for robustness
        3. Combines both methods for best results

        Args:
            user_query (str): User's input query

        Returns:
            FAQItem or None: Best matching FAQ item or None if no match
        """
        # Try ML-based matching first
        ml_match, ml_confidence = self._find_best_match_ml(user_query)
        
        # Keyword matching as fallback/verification
        keyword_match = None
        highest_keyword_score = 0

        for faq_item in self._faq_database:
            match_score = faq_item.matches_query(user_query)

            if match_score > highest_keyword_score:
                highest_keyword_score = match_score
                keyword_match = faq_item

        # Hybrid decision: Prefer ML if confidence is good, else use keywords
        if ml_match and ml_confidence > 0.3:
            return ml_match
        elif keyword_match and highest_keyword_score > 0:
            return keyword_match
        elif ml_match and ml_confidence > 0.2:
            return ml_match
        
        return None

    def process_input(self, user_input):
        """
        Process user input and generate response

        OOP PRINCIPLE: SINGLE RESPONSIBILITY
        - This method's only job is to process input and return response

        Args:
            user_input (str): User's message

        Returns:
            str: Bot's response
        """
        if not user_input or user_input.strip() == "":
            return "Please ask me a question about registrar services."

        # Check if user is greeting
        if self.is_greeting(user_input):
            greeting_response = "Hello! 👋 Welcome to the Registrar AI Chatbot. I'm here to help you with information about registrar services.\n\n"
            greeting_response += self.get_faq_list()
            greeting_response += "\nFeel free to ask me any questions about these topics!"
            return greeting_response

        best_match = self.find_best_match(user_input)

        if best_match:
            return best_match.get_answer()
        else:
            return self._default_response

    def get_response(self, message):
        """
        Public interface for getting chatbot response

        OOP PRINCIPLE: ABSTRACTION
        - Simple interface for external code
        - Hides internal processing complexity

        Args:
            message (str): User's message

        Returns:
            str: Chatbot's response
        """
        return self.process_input(message)

    def get_faq_count(self):
        """
        Get the number of FAQs loaded

        OOP PRINCIPLE: ENCAPSULATION
        - Provides controlled access to internal data

        Returns:
            int: Number of FAQ items
        """
        return len(self._faq_database)
