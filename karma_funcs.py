#Karma ATM will start with a karma points balance.

def karma_score(num):
    ratings = [
        {"advice" : "Really?! You obviously aren't worried about karma.", "score" : 100},
        {"advice" : "You are doomed! Better start rescuing some kittens!", "score" : 250},
        {"advice" : "You know you can do better. Start hugging some trees!", "score" : 400},
        {"advice" : "You have some karma work to do, but tomorrow's a new day to do good!", "score" : 550},
        {"advice" : "You had a bad day or two. Look out for ways to be better today!", "score" : 700},
        {"advice" : "You're walking the line, but the stars seem to be shining on you today!", "score" : 850},
        {"advice" : "I tip my hat to you. Let a tree give YOU a hug for a change.", "score" : 1000},
        {"advice" : "Can I buy you a drink? You have earned one!", "score" : 1150},
        {"advice" : "Can I stand near you? Your aura is pure gold!", "score" : 1300},
        {"advice" : "You're a zen master. Who did you train under?!", "score" : 1450},
        {"advice" : "What does nirvana look like? I know you know.", "score" : 1600},
        {"advice" : "You can't get better karma, but I know that won't stop you from trying!", "score" : 1750}
        ]
    for rating in ratings:
        if rating["score"] == num:
            return rating["advice"]