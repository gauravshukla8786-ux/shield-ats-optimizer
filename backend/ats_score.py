from sklearn.feature_extraction.text import TfidfVectorizer

CORPORATE_KEYWORDS = [
    "project",
    "management",
    "leadership",
    "operations",
    "team",
    "analysis",
    "planning",
    "coordination"
]

def calculate_ats_score(resume_text: str) -> float:
    documents = [resume_text] + CORPORATE_KEYWORDS

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    resume_vector = tfidf_matrix[0]
    keyword_vectors = tfidf_matrix[1:]

    score = resume_vector.multiply(keyword_vectors).sum()
    return round(float(score * 10), 2)
