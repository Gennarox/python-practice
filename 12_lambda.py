def increment(x):
  return x+1

print(increment(25))

#V2 con lambda
increment_v2 = lambda x:x+1
print(increment_v2(25))

print("*"*20)

concat_words = lambda word1, word2 : f'El texto concatenado y tratado es -> {word1.strip().title()} {word2.strip().title()}'

print(concat_words("hOlA","mUndO"))