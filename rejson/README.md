# Hands-On Session: ReJSON

This exercise demonstrates using both a module and specifically, ReJSON. 

You will learn how to execute non-standard Redis commands directly from Python and learn a few commands to manipulate JSON directly from within Redis.

This directory contains files to use for the exercise.  The `rejson.py` program provides a skeleton to
help you get started.  We have added code to manage multiple publishers and subscribers running locally 
and to help create simulated messages.  If you get stuck, files ending with `_solution.py` implements our solution to 
the exercise.  Feel free to study it or ask questions of the training staff.

Although this is a hands-on exercise, we want to encourage you to use this time to ask 
questions of the training staff as well.

## Part One: Review ReJSON Documentation

### Instructions

Please review the following documentation on redis.io to get started:
* [ReJSON API](https://oss.redislabs.com/rejson/commands/)
* [Python client API](https://github.com/andymccurdy/redis-py)

## Part Two: Update JSON from within Redis

1. Prior to modifying `rejson.py`, run the program and see what happens
2. Update the file with your connection information
3. Write code to set the `last` field in the `name` object of the Key to "Sanfilippo"
4. Write code to append "Sicily" to the `location` array in the Key
5. Write code to increment `age` in the Key from 40 to 41.

### Further Activities

1. Write code to delete the the `first` field from the `last` object using `JSON.DEL`
2. Write code to remove the 'Campobello di Licata' from the `location` array.

