# Changelog

## Changes in 1.5.0
Support for python3 has been added

## Changes in 1.4.0
The default state matching behavior has changed to match the passed states to any of the nodes states.  There are also two new options.  The first, explained below is the ```-x``` or exclusive option that provides the exclusive matching that was previously used.  The second option is the ```-N``` or note option which will display any notes in the extended attribute space.  The final change is that any node which has a note associated with it will display an asterisk ```*``` to the left of the hostname and before the OS column.