def more_general(h1, h2):
    return all(x == '?' or x == y for x, y in zip(h1, h2))

def fulfills(h, example):
    return all(h[i] == '?' or h[i] == example[i] for i in range(len(h)))

def min_generalizations(h, example):
    h_new = list(h)
    for i in range(len(h)):
        if h[i] == '0':
            h_new[i] = example[i]
        elif h[i] != example[i]:
            h_new[i] = '?'
    return [tuple(h_new)]

def candidate_elimination_step(examples, domains):
    G = {('?',) * len(domains)}
    S = {('0',) * len(domains)}

    example, label = examples[0]
    print(f"Processing example: {example}, label: {label}")
    
    if label == 'Yes':  # Positive example
        # Remove from G any hypothesis that does not cover the example
        G = {g for g in G if fulfills(g, example)}
        print(f"Updated G: {G}")
        
        # Update S
        S_new = set(S)
        for s in S:
            if not fulfills(s, example):
                S_new.remove(s)
                S_new.update(min_generalizations(s, example))
        S = S_new
        print(f"Updated S: {S}")
        
        # Ensure S is more specific than at least one hypothesis in G
        S = {s for s in S if any(more_general(g, s) for g in G)}
    
    print(f"Most specific hypotheses (S): {S}")
    print(f"Most general hypotheses (G): {G}")

# Example usage
domains = [
    ['Sunny', 'Rainy'],
    ['Warm', 'Cold'],
    ['Normal', 'High'],
    ['Strong', 'Weak'],
    ['Warm', 'Cool'],
    ['Same', 'Change']
]

examples = [
    (['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'], 'Yes'),
    (['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same'], 'Yes'),
    (['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'], 'No'),
    (['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change'], 'Yes')
]

candidate_elimination_step(examples, domains)
