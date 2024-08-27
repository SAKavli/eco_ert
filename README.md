# eco_ert
Simple example of ert usage for simulation of a house loan.

As instructed in the ert polyexample documentation,
first enable the komodo environment by typing..

> source /prog/res/komodo/stable/enable

..in your shell, followed by:

> ert gui eco.ert

Then, run ensemble experiment in the ert GUI.
A window taking user input will appear, which will ask
for information about price of desired house, equity and salary.

Hit "Simulate my loan". If invalid input was entered
a new window will appear requesting the information again.

By pressing "show plotting", ert will visualize how large your loan
will be, and when you will be rent free (curve hitting y = 0).

There is by default 50 realizations of the simulated loan, which vary the parameters taxrate (25-35%, Triangular distribution) and interest (2-9%, Triangular distribution).