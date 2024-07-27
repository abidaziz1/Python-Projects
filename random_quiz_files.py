import random

# Dictionary of states and their capitals
capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 
    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 
    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 
    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 
    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 
    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 
    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 
    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 
    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

# Generate 35 quiz files
for quizNum in range(35):
    # Create the quiz and answer key files
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
    
    # Write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    
    # A list of all state names is created and then shuffled to randomize the order of the questions.
    states = list(capitals.keys())
    random.shuffle(states)
    
    # Create 50 questions
    for questionNum in range(50):
        # Get the correct answer for the current state
        correctAnswer = capitals[states[questionNum]]
        
        # Create a list of all possible wrong answers
        wrongAnswers = list(capitals.values())
        
        # Remove the correct answer from the list of wrong answers
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        
        # Randomly select three wrong answers
        wrongAnswers = random.sample(wrongAnswers, 3)
        
        # Combine the correct answer with the three wrong answers
        answerOptions = wrongAnswers + [correctAnswer]
        
        # Shuffle the order of the answer options
        random.shuffle(answerOptions)
        
        # Write the question and answer options to the quiz file
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')
        
        # Write the answer key to a file
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    
    # Close the files
    quizFile.close()
    answerKeyFile.close()
