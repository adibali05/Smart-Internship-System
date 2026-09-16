from transformers import pipeline

# Load the NLP model (Zero-Shot Classification)
# Yeh model aapke system mein already download ho chuka hai
try:
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
except Exception as e:
    print(f"Model loading error: {e}")
    classifier = None

def score_log_text(text: str):
    if not classifier:
        return {"technical_score": 0.0, "soft_skills_score": 0.0}

    # Hum AI se poochenge ki is log mein kya zyada hai
    candidate_labels = ["technical development and coding", "communication and management", "irrelevant or empty"]
    
    try:
        # AI ko text classify karne ke liye bhej rahe hain
        result = classifier(text, candidate_labels)
        
        # Result ko dictionary mein convert kar rahe hain aur 100 se multiply (Percentage ke liye)
        scores = dict(zip(result['labels'], result['scores']))
        
        tech_score = round(scores.get("technical development and coding", 0) * 100, 2)
        soft_score = round(scores.get("communication and management", 0) * 100, 2)
        
        return {
            "technical_score": tech_score,
            "soft_skills_score": soft_score
        }
    except Exception as e:
        print(f"Scoring error: {e}")
        return {
            "technical_score": 0.0,
            "soft_skills_score": 0.0
        }