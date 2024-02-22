"""Module is for testing."""
import subprocess

def greeting(name: str) -> str:
    """Generate a greeting message for a given name.

    Parameters
    ----------
    name: The name of the person to greet.
        It should be a string representing the name of the individual.

    Returns
    -------
    str: A greeting message addressed to the provided name.

    """
    return "Hello " + name


x = 3
y = 2


user_input = input("Enter your name: ")
subprocess.call(["echo", user_input])
