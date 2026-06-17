def score_segment(text):

    text = text.lower()

    score = 0

    weights = {
        "ai": 4,
        "future": 5,
        "secret": 6,
        "mistake": 5,
        "million": 5,
        "never": 4,
        "best": 3,
        "important": 3,
        "crazy": 4,
        "success": 4
    }

    for word, weight in weights.items():

        if word in text:
            score += weight

    return score