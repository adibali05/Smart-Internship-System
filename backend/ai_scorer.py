from transformers import pipeline

try:
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
except Exception as e:
    print(f"Model loading error: {e}")
    classifier = None

def score_log_text(text: str):
    if not classifier:
        return {"technical_score": 0.0, "soft_skills_score": 0.0}

    candidate_labels = ["technical development and coding", "communication and management", "irrelevant or empty"]
    
    try:
        result = classifier(text, candidate_labels)
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
    