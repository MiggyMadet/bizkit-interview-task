import operator
from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    # Implement search here!
    keys = list()
    result = list()
    for item in args.items():
        key = item[0]
        value = item[1]
        #print(key)
        for people in USERS:
            if key == "name" or key == "occupation":
                if value in people[key]:
                    result.append(people)
            else:
                if key == "id":
                    if people[key] == value:
                        result.append(people) 
                else:
                    if people[key] == int(value):
                        result.append(people) 
    
    # for Search Specifications
    # result.sort(key=lambda x: x["id"])
    
    # for Bonus Challenge
    result.sort(key=lambda x: key)
    return result
