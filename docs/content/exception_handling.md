# Exception Handling

It is pythonic to handle Exceptions. How this is done is up to the developer,
but I have one requirement and two suggestions:

## Requirement

At no time will an Exception bubble up to the user to read.

## Suggestions

- Handle the Exception at the lowest possible level, and send a custom
  Exception with an easy-to-read message to be caught by the interface.
- Use an IO Monad along with a Maybe Monad to stop the exception and execution
  if required.
