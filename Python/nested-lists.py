if __name__ == '__main__':
    all_names = []
all_scores = []
total = []
sec_small = -1
sec_names = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    record = [name, score]
    all_names.append(name)
    all_scores.append(score)
sor_scores = sorted(all_scores)

for i in sor_scores:
    if i == min(sor_scores):
        continue
    elif i > min(sor_scores):
        sec_small = i
        break

for index, value in enumerate(all_scores):
    if value == sec_small:
        sec_names.append(all_names[index])

sor_names = sorted(sec_names)
for alph in sor_names:
    print(alph)
