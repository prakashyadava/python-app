lower_case_charactors = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 0]
symbols = ['!', '@', '#', '$', '%', '^', '&', "*", '-', '_', '(', ')', '=','+', '/', '{', '}', '[', ']', '"', "'", '\\', '|', '/' ,'?', '<', '>', ',', '.', ':', ';']
upper_case_charactors = []
for i in range(0,26):
    upper_case_charactors.append(lower_case_charactors[i].upper())

letters = lower_case_charactors + upper_case_charactors