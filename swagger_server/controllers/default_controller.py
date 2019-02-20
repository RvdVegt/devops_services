import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.person import Person  # noqa: E501
from swagger_server.models.persons import Persons  # noqa: E501
from swagger_server import util

from flask import request, abort, Response, jsonify

persons_list = []


def persons_get(pageSize=None, pageNumber=None):  # noqa: E501
    """Get persons

    returns a list of persons # noqa: E501

    :param pageSize: Number of persons returned
    :type pageSize: int
    :param pageNumber: Page number
    :type pageNumber: int

    :rtype: Persons
    """
    res = []
    if pageSize is not None and pageNumber is not None:
        res = persons_list[(pageNumber-1)*pageSize:pageNumber*pageSize]
    return jsonify(items=res)


def persons_post(person=None):  # noqa: E501
    """create a person

    adds new person to the persons list. # noqa: E501

    :param person: person to create
    :type person: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        person = Person.from_dict(connexion.request.get_json())  # noqa: E501
        persons_list.append(person)
    return Response(mimetype='application/json', status=204)


def persons_username_delete(username):  # noqa: E501
    """Deletes a person

    Delete a single person from its username # noqa: E501

    :param username: The person&#39;s username
    :type username: str

    :rtype: None
    """
    return 'do some magic!'


def persons_username_get(username):  # noqa: E501
    """Get a person

    Returns a single person for its username # noqa: E501

    :param username: The person&#39;s username
    :type username: str

    :rtype: Person
    """
    return 'do some magic!'
