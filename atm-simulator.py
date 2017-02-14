import math
from Ragnarok import *

# Set to default value NONE
state = None
bills = None

"""
Initialize the app
"""
def init ():
    global state, bills

    print("====== ATM SIMULATOR ======")

    # Starts the raganarok (STATE MANAGER)
    state = Ragnarok()
    state.setInitialState({
        "current": 0,
        "previous": 0,
        "bills": []
    })

    bills = sorted([500, 200, 100, 50, 20], reverse=True)

    req = requestQuantity()

    # If request does not fit the requirement, stop execution
    if type(req) != int or req < min(bills):
        print "ERROR: The value should be an INT or more than " + str(min(bills)) + " USD"
        return None

    calculate(req)

    displayResult(state.getState()["bills"])

"""
Display the prompt to enable use enter the quantity
"""
def requestQuantity ():
    quantity = raw_input("Enter the quantity: ")
    try:
        quantity = int(quantity)
        return quantity
    except Exception:
        return quantity

"""
Calculate bills to deliver
"""
def calculate (req):
    global state, bills

    deliveryBills = []

    state.updateState({"current": req})

    for bill in bills:
        # Stops the loop when current money is 0
        if state.getState()["current"] == 0:
            break;

        quantity = int(math.floor(state.getState()["current"] / float(bill)))
        newMoney = state.getState()["current"] - (quantity * bill)

        # Skip when bills quantity is 0
        if quantity > 0:
            deliveryBills.append({"bill": bill, "quantity": quantity})

        state.updateState({
            "current": newMoney,
            "previous": state.getState()["current"],
            "bills": deliveryBills
        })

    return state.getState()

# Display the results friendly
def displayResult (_bills):
    print "--------------------------------"
    print "DELIVERING MONEY"
    print "--------------------------------"

    for bill in _bills:
        print "----- " + str(bill["quantity"]) + " bills of " + str(bill["bill"]) + " USD"

init()