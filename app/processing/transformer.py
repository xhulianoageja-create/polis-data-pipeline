def transform(quotes, age_lookup):
    """
    Kombinon citatet me moshën e autorëve.
    """
    transformed = []

    for q in quotes:
        transformed.append({
            "quote": q["quote"],
            "author": q["author"],
            "estimated_age": age_lookup.get(q["author"])
        })

    return transformed
