from flask import Flask, jsonify
from worker import *
import json

DESKS_NUM = 100 
WORKERS_NUM = 10
MEALS_NUM = 25
desks = [Desk(i) for i in range(DESKS_NUM)]
workers = [Worker(i) for i in range(WORKERS_NUM)] 
meals = [Meals(i) for i in range(MEALS_NUM)]



app = Flask(__name__)

@app.route("/")
def hello():
    return "HELLO, WORLD"


"""
For worker
"""

@app.route("/api/assign/<int:worker>")
def assignwork(worker):
    """
    Search work for the worker
    """
    for desk in desks:
        # TODO Change to percentage
        
        if desk.have = True and desk.weight <= 20 and desk.assigned == False:
            work = { 
                    "worktype" : "clean",
                    "desknum" : desk.no
                    }
            desk.assigned = True 
            workers[worker].assign(work)
            return jsonify(work)
        return jsonify([])

@app.route("/api/finish/<int:worker>")
def finishwork(worker):
    """
    finish work 
    """
    desks[worker.work["desknum"]].clean()

    return "success"

"""
For dish
"""


@app.route("/api/order/<int:dish>/<int:meal>")
def orderdish(dish,meal):
    """
    Update the ordered meal
    """
    desks[dish].meal = meal 
    desks[dish].weight = 100
    desks[dish].have = True
    return "success"

@app.route("/api/update/<int:dish>/<int:weight>")
def echo(dish,weight):
    """
    Update dish Weight
    """
    desks[dish].update(weight)
    return "success"

"""
For monitor
"""


@app.route("/showall")
def showall():
    """
        input : None 
        Output : Json that show all states
    """
    local_workers = [{"number": worker.no, 
                    "work": worker.work} for worker in workers]
    local_desks = [{"number": desk.no, "weight": desk.weight, 
                    "have" : desk.have, "meal": desk.meal}
                    for desk in desks]
    return jsonify([local_workers, local_desks])
