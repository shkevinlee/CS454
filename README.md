# CS454

## Dataset Description

# bugzilla_eclipse_log(comments)_2016meancost.pkl

Definition of Cost: Time cost for resolved bug for each component

Definition of Profit: log(number of comments) + 1

Real Cost sum : 50699.701903571

Real Profit sum : 3489.635924693581


# bugzilla_eclipse_comments_2016meancost.pkl

Definition of Cost: Time cost for resolved bug for each component

Definition of Profit: number of comments

Real Cost sum : 50699.701903571

Real Profit sum : 11586


# bugzilla_firefox_log(comments)_2016meancost.pkl

Definition of Cost: Time cost for resolved bug for each component

Definition of Profit: log(number of comments) + 1

Real Cost sum : 262945.49580958224

Real Profit sum : 13025.880847481712


# bugzilla_firefox_comments_2016meancost.pkl

Definition of Cost: Time cost for resolved bug for each component

Definition of Profit: number of comments

Real Cost sum : 262945.49580958224

Real Profit sum : 62927


# bugzilla_firefox_priority_2016meancost.pkl

Definition of Cost: Time cost for resolved bug for each component

Definition of Profit: priority

Real Cost sum : 262945.49580958224

Real Profit sum : 12210


# bugzilla_firefox_comments+priority_2016meancost.pkl

Definition of Cost: Time cost for resolved bug for each component

Definition of Profit: priority

Real Cost sum : 262945.49580958224

Real Profit sum : 26332.880847481712

# ILP (install modules)
To run ilp.py, user has to install PuLP and gurobipy module in local by following these instructions.

## install PuLP
PuLP requires Python >= 2.6

### In windows
in cmd, use

> pip install pulp
### in Linux
> $ sudo pip install pulp

> $ sudo pulptest

after install PuLP, use in python:

> from pulp import *

reference : https://pythonhosted.org/PuLP/main/installing_pulp_at_home.html

## install gurobipy
register in http://www.gurobi.com/ and follow the instrucutions.

> register on website -> download gurobi optimizer -> install license on local with command (You can see this command on gurobi website after getting license.)

after install gurobipy, use in python:

> from gurobipy import *
