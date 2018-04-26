from flask import request, session
from mamom import app

from mamom.models.Goal import Goal
from mamom.models.User import User

@app.route("/mamom/goals/<goal_id>/", methods=["GET"])
def get_goal(goal_id):
    goal = Goal().getGoalById(goal_id)

    return render_template("goals/goals.html")


@app.route("/mamom/goals/<goal_id>/", methods=["DELETE"])
def delete_goal(goal_id):
    try:
        goal = Goal(id=goal_id)

        if goal.deleteGoal():
            return "OK", 200
        else:
            return "Error", 400
    except Exception as e:
        return "Error", 400

@app.route("/mamom/goals/<goal_id>/", methods=["PUT"])
def update_goal(goal_id):
    try:
        name = request.form.get("name")
        value = float(request.form.get("value"))
        deadline = request.form.get("deadline")

        goal = Goal(id=goal_id, value=value, name=name, deadline=deadline)

        if goal.updateGoal():
            return "OK", 200
        else:
            return "Error", 400
    except Exception as e:
        return "Error", 400

@app.route("/mamom/goals/", methods=["POST"])
def create_goal():
    try:
        name = request.form.get("name")
        value = float(request.form.get("value"))
        deadline = request.form.get("deadline")
        user = User().getUserById(session["_id"])

        goal = Goal(name=name, balance=0, value=value, deadline=deadline, user=user)

        if(goal.createGoal()):
            return "OK", 200
        else:
            return "Error", 400
    except Exception as e:
        return "Error", 400
