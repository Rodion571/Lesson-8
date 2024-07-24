# Task 1
text1 = input("Input your text: ").split()
text2 = input("Input another text: ").split()
print(f"You repeated the word(s) {set(text1) & set(text2)}")
# Task 2
text_1 = input('Enter first text: ')
text_2 = input('Enter second text: ')
set_1 = set(text_1)
set_2 = set(text_2)
res = set_1.intersection(set_2)
print(len(res))
# Task 3
def has_unique_values(d):
    values = list(d.values())
    unique_values = set(values)
    return len(values) == len(unique_values)
example_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 1
}
if has_unique_values(example_dict):
    print("All values are unique.")
else:
    print("There are duplicate values.")
# Task 4
def find_common_friends_for_four(user1, user2, user3, user4, friendships):
    if user1 in friendships and user2 in friendships and user3 in friendships and user4 in friendships:
        common_friends = friendships[user1] & friendships[user2] & friendships[user3] & friendships[user4]
        return common_friends
    else:
        return set()
friendships = {
    "user1": {"user2", "user3", "user4"},
    "user2": {"user1", "user3"},
    "user3": {"user1", "user2", "user4"},
    "user4": {"user1", "user3"}
}
user1 = input("user1: ")
user2 = input("user2: ")
user3 = input("user3: ")
user4 = input("user4: ")
common_friends = find_common_friends_for_four(user1, user2, user3, user4, friendships)
if common_friends:
    print(f"Mutual friends for {user1}, {user2}, {user3} и {user4}: {common_friends}")
else:
    print(f"No mutual friends for {user1}, {user2}, {user3} и {user4}.")
# Task 5
def longest_common_word(text1, text2):
    words1 = text1.split()
    words2 = text2.split()
    common_words = [word for word in words1 if word in words2]
    if not common_words:
        return "No common words found"
    longest_word = max(common_words, key=len)
    return longest_word
text1 = input("Enter the first text: ")
text2 = input("Enter the second text: ")
result = longest_common_word(text1, text2)
print("The longest common word is:", result)