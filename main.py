import sys
#variables kept track from user
userName = ''
userName = str(input('What is your name? '))
oneRepMax = float(input('What is your one rep max? '))
workoutRx = None


def myoGenerator():
    moddedRepCount = round(oneRepMax * .7)
    print (userName + '\n' + str(moddedRepCount) + ' lbs is the weight you will be using for your split. \nThis is from your 1 rep max of: ' + str(oneRepMax) + '\n \n WORKING SET: \n 12 reps of ' + str(moddedRepCount) + ' \n 15 second break \n 5 reps of ' + str(moddedRepCount) + '\n 15 second break\n 5 reps of ' + str(moddedRepCount) + '\n 15 second break\n 2-3 reps of ' + str(moddedRepCount) + '\n 15 second break \n 2-3 reps of ' + str(moddedRepCount) + '\n COMPLETE \n\n')

myoGenerator()

### while True:
    #oneRepMax = input(' What is your 1 Rep Max?')
    #if type(oneRepMax) == int or type(oneRepMax) == float:
     #   myoGenerator()
      #  break
    #else:
     #   print('You need to put a number in! Try Again.')
#workout calculator for myo-workout
#while True: #start the calculator
 #   if workoutRx =None:
  #      print('We will need to get you started with a workout')
   # else:
    #    print(workoutRx)
    #while True: #the input loop
     #   print('Please enter your 1 Rep Max for your lift that you would like to get a split for \n type "q" to exit')
