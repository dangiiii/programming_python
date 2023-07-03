import logging
import sys   

# Create logger object
logger = logging.getLogger()

# Set the minimum log level (compare table in fig. 1 of the exercise sheet)
logger.setLevel(logging.INFO)

# Define handlers. These tell the logging object where/how to store/output the logging message.
# There can be multiple handlers per logging object, in this case the output gets logged to 'mylog.log'
# as well as the 'sys.stdout', which is your terminal/IDE output.
handler_file = logging.FileHandler('testlog.log')
handler_stdout = logging.StreamHandler(sys.stdout)

# Define the logging format/what to log
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# The logging format needs to be set specifically for every handler
handler_file.setFormatter(formatter)

# The handlers defined above need to be added to the logger object 
logger.addHandler(handler_file)
logger.addHandler(handler_stdout)

# They can also be removed by using the following syntax
# logger.removeHandler(handler_stdout)

# Instead of using print you need to use logging.LEVEL to output a message.
# You can use the same syntax and commands you already know from the print() method.
logger.info(f"INFO logged")
logger.warning(f"WARNING logged") 
