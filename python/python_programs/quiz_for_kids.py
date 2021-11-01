# GK quiz for kids.

score = 0
ans = input("Do you want to appear for quiz?Y/N  ")
ans = ans.upper()
if ans == 'Y':
 name =input('Enter your name: ')
 print('Hello', name, 'welcome! Be ready for quiz!')

 ques_1 = print('Who is prime minister of India?')
 ans_1 =input('Your answer: ')
 ans_1 = ans_1.lower()
 if ans_1 == 'narendra modi':
    print('Right!')
    score += 1
 else:
    print('Wrong :(')

 ques_2 = print('What is the name of Indian flag?')
 ans_2 =input('Your answer: ')
 ans_2 = ans_2.lower()
 if ans_2 == 'tricolour':
    print('Right!')
    score += 1
 else:
    print('Wrong :(')

 ques_3 = print('Which planet has an eye?')
 ans_3 = input('Your answer: ')
 ans_3 = ans_3.lower()
 if ans_3 == 'jupiter':
     print('Right!')
     score += 1
 else:
     print('Wrong :(')

 ques_4 = print('In which state of India Statue of unity is located?')
 ans_4 = input('Your answer: ')
 ans_4 = ans_4.lower()
 if ans_4 == 'gujarat':
     print('Right!')
     score += 1
 else:
     print('Wrong :(')

 ques_5 = print('Which city is known as pink city in India?')
 ans_5 = input('Your answer: ')
 ans_5 = ans_5.lower()
 if ans_5 == 'jaipur':
     print('Right!')
     score += 1
 else:
     print('Wrong :(')

 ques_6 = print('What is the capital of USA?')
 ans_6 = input('Your answer: ')
 ans_6 = ans_6.lower()
 if ans_6 == 'washington dc':
     print('Right!')
     score += 1
 else:
     print('Wrong :(')

 ques_7 = print('National sports of India?')
 ans_7 = input('Your answer: ')
 ans_7 = ans_7.lower()
 if ans_7 == 'hockey':
     print('Right!')
     score += 1
 else:
     print('Wrong :(')

 ques_8 = print('When is international yoga day?')
 ans_8 = input('Your answer: ')
 if ans_8 == '21 june':
     print('Right!')
     score += 1
 else:
     print('Wrong :(')

 ques_9 = print('How many continents are there in the world?')
 ans_9 = input('Your answer: ')
 if ans_9 == '7':
     print('Right!')
     score += 1
 else:
     print('Wrong :(')

 ques_10 = print('Which is the smallest continent?')
 ans_10 = input('Your answer: ')
 ans_10 = ans_10.lower()
 if ans_10 == 'australia':
     print('Right!')
     score += 1
 else:
     print('Wrong :(')


 print('Your score is', score,'out of 10.')

 if score == 10:
     print('Brilliant!!!!! :) ')



