import random
game_list = ["rock","paper","scissor"]
user_choose = int(input("Enter your choice: 0 for rock , 1 for paper and 2 for scissor: "))
computer_choose = random.randint(0,len(game_list)-1)
print("Computer choosed : ",computer_choose)
user_rock = ["It is rock-rock. So lets call it a draw","You won!! rock-paper"," You loose!! rock-scissor"]
user_paper = ["You won!! paper-rock", "It is paper-paper. So lets call it a draw","You loose!! paper-scissor"]
user_scissor = ["You loose!! scissor-rock","You won!! scissor-paper","It is scissor-scissor. So lets call it a draw"]
possible_outcomes = [user_rock,user_paper,user_scissor]
select_user = possible_outcomes[user_choose]
message = select_user[computer_choose]
print(message)