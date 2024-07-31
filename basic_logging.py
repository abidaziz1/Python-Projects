import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s  -  %(message)s')
logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total
print(factorial(5))
logging.debug('End of program')

'''
The nice thing about log messages is that you’re free to fill your program 
with as many as you like, and you can always disable them later by adding 
a single logging.disable(logging.CRITICAL) call.
'''


"""
>>> logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  
%(levelname)s -  %(message)s')
 >>> logging.debug('Some debugging details.')
 2015-05-18 19:04:26,901 - DEBUG - Some debugging details.
 >>> logging.info('The logging module is working.')
 2015-05-18 19:04:35,569 - INFO - The logging module is working.
 >>> logging.warning('An error message is about to be logged.')
 2015-05-18 19:04:56,843 - WARNING - An error message is about to be logged.
 >>> logging.error('An error has occurred.')
 2015-05-18 19:05:07,737 - ERROR - An error has occurred.
 >>> logging.critical('The program is unable to recover!')
 2015-05-18 19:05:45,794 - CRITICAL - The program is unable to recover!

"""