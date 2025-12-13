# Exception Handling

It is pythonic to handle Exceptions. How this is done is up to the developer, but I have two
requirement and two suggestions:

## Requirements

- At no time will an Exception bubble up to the user to read
- When creating a wrapped function for a monad, read the documentation on the side-effect you are
  hiding for the exceptions. Do NOT use the generic Exception.

## Suggestions

- Handle the Exception at the lowest possible level, and send a custom Exception with an
  easy-to-read message to be caught by the interface, or
- Use an IO Monad along with a Maybe Monad to stop the execution if required.

