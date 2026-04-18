
student_scores =  {
    "Harry": 81,
    "Ron": 78,
    "Hermoine": 99,
    "Draco": 74,
    "Neville": 62,
}
studen_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        studen_grades[student] = "Oustanding"
    elif score > 80:
        studen_grades[student] = "Exceeds Expectations"
    else:
        studen_grades[student] = "Fail"
print(studen_grades)


bids = {}
bidding_finished = False
highest_bid = 0
winner = ""

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid: 
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))

    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'Yes' or 'No'.\n")
    if should_continue == "No": 
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "Yes":
        print(f"The bidder is {price}")

