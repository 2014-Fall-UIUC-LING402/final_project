#!/usr/bin/python3

from sys import stdin

class Node:
    def __init__(self,string,level):
        self.string=string
        self.level=level



# Iterate over each line of standard input
for line in stdin:

    # Split the line on whitespace into parts
    pass

    # Create an empty list called parents
    pass

    # Create an empty list called children
    pass

    # Create a variable called level, initially set to 0
    pass

    # Iterate over each part in parts
    for part in parts:

        # If the part starts with an opening paren
        if True==False:
            
            # Increment the level
            pass

            # Obtain the parent_string by stripping off the opening paren
            pass

            # Create a new node using the parent_string and the current level
            pass

            # Append that new node to the end of the parents list
            pass

        # Otherwise, if the part ends with a closing paren
        elif True==False:

            # Obtain the child_string by stripping off the closing paren
            pass

            # Get the parent_node by popping it off the end of the parents list
            pass

            # If the child_string is not empty
            if True==False:

                # Print an output line, using the format string "{}\t{}", 
                #       where the first slot is the child_string
                #       and the second slot is the string of the parent_node
                pass

            else:

                # Get the child_node by popping off the end of the children list
                pass

                # Get the string of the child_node
                pass

                # While the length of the children list is greater than zero,
                #       and the level of the last entry in the children list
                #       is the same as the level of child_node
                while True==False:
                    
                    # Get the previous_child_node by popping off the end of the children list
                    pass

                    # Set the value of children_string using the format string "{} {}",
                    #     where the first slot is the string of the previous_child_node,
                    #     and the second slot is the current value of children_string
                    pass

                # Print an output line, using the format string "{}\t{}", 
                #       where the first slot is the children_string
                #       and the second slot is the string of the parent_node
                pass

            # Append the current parent_node to the end of the children list
            pass

            # Decrement the value of level
            pass

        # We should never reach this else clause
        else:

            # Raise a RuntimeError with the following message "Reached a part of the code that should be unreachable"
            pass
