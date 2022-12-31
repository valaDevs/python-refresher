numbers = [1,2,3]

doubled = [num * 2 for num in numbers]

friends = ["daryl","carol","vala","vahid","Rick","ebraham","versia","venus","valeh","glen","carol"]
starts_v = [fr for fr in friends if fr.startswith("v")]

# for fr in friends:
#     if fr.startswith('v'):
#         starts_v.append(fr)
        
print(starts_v)