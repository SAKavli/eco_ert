# eco_ert
Simple example of ert usage for simulation of a house loan.

As instructed in the ert polyexample documentation,
first enable the komodo environment by typing..

> source /prog/res/komodo/stable/enable

..in your shell, followed by:

> ert gui eco.ert

Then, run ensemble experiment in the ert GUI.
A window taking user input will appear, which will ask
for information about price of desired house, equity, salary and estimated monthly expenses.

Hit "Simulate my loan". If invalid input was entered
a new window will appear requesting the information again.
If the window was exited with blank fields, the ert experiment
will fail.

By pressing "show plotting", ert will visualize how large your loan
will be, and at what month you will be rent free (curve hitting y = 0).

There is by default 50 realizations of the simulated loan, which vary the parameters taxrate (25-35%, Triangular distribution) and interest (2-9%, Triangular distribution).

Each realization will keep iterating until the loan hits 0, unless there has been 100 iterations, and the
loan is increasing for each month (meaning interest + monthly expenses > monthly repayment) 

If you want to run more experiments after the first, the storage and userinput.txt folder and file should be removed:

> rm -r storage userinput.txt