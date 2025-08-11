n, k = map(int, input().split())
scores = list(map(int, input().split()))
passing_score = scores[k]
count = sum(1 for score in scores if score >= passing_score and score > 0)
print(count)