import spacy
nlp = spacy.load('en_core_web_sm')

print("------------------- example 1 -------------------")
exampletokens = nlp('cat apple monkey banana')
for token1 in exampletokens:
    for token2 in exampletokens:
        print(token1.text, token2.text, token1.similarity(token2))

# it is interesting that the similarity function recognises that cat and monkey are similar as both are animals.
# it is more interesting that it recognises that monkey and banana are similar as monkeys like bananas!

print("------------------- my words -------------------")
mytokens = nlp('ford honda river desert')
for token_a in mytokens:
    for token_b in mytokens:
        print(token_a.text, token_b.text, token_a.similarity(token_b))

# I was surprised that this didn't return a stronger relation between river and ford or ford and honda
# as ford and honda are both vehicle companies, and ford is also a name for a river crossing
# I expected that these would have shown a higher similarity, but maybe I was too obscure with my connections
# also, surprisingly, I received a negative relation between many of the words and I do not know how this is possible?

# when running the script through the simpler SM language model, I received the below error message
# however, I also received similarity scores for my words more in line with my expectations from the start.
# This showed the connection between honda and ford and ford and river that I was expecting.

#UserWarning: [W007]
# The model you're using has no word vectors loaded,
# so the result of the Token.similarity method will be based on the tagger, parser and NER,
# which may not give useful similarity judgements.
# This may happen if you're using one of the small models, e.g. `en_core_web_sm`,
# which don't ship with word vectors and only use context-sensitive tensors.
# You can always add your own word vectors, or use one of the larger models instead if available.