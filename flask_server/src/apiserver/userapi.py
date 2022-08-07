from flask_restful import Resource
from flask import request,Response
import json
import traceback
import logging


logger = logging.getLogger(__name__)

class UserAPI(Resource):
    def __init__(self,**kwargs):
        pass


    def get(self):
        resp = { "error": False, "message":None,"data":None}
        status = 200
        try:
            user_id = request.args.get('id')
            if user_id:
                user = {}
                # Find User profile from DB and return it via user
                resp["message"] = "User available"
                resp["data"] = user
            else:
                all_users = []
                # Find all users in DB, add to all_users and return it. 
                resp["message"] = "User list available"
                resp["data"] = all_users                
        except Exception as e:
            logger.error(e)
            logger.error(type(e))
            logger.error(traceback.format_exc())
            status = 500
            resp["error"] = True
            resp["message"] = "Internal server error"
            # resp["message"] = "Internal server error"+str(e)
        return Response(json.dumps(resp), status=status, mimetype='application/json')

    def post(self,**kwargs):
        resp = { "error": False, "message":None,"data":{}}
        status = 200
        try:
            errMsg = self.validatePostData()
            if errMsg:
                resp["error"] = True
                resp["message"] = errMsg
                status = 400
            # Check if user already exists in Db
            # add user in Db
            # return success after adding.
            else:
                resp["message"] = "User added successfully"
        except Exception as e:
            logger.error(e)
            logger.error(type(e))
            logger.error(traceback.format_exc())
            status = 500
            resp["error"] = True
            resp["message"] = "Internal server error"
            # resp["message"] = "Internal server error"+str(e)
        return Response(json.dumps(resp), status=status, mimetype='application/json')

    

    def validatePostData(self):
        errMsg = None
        if not "id" in request.json:
            errMsg = "id required."
        elif not "name" in request.json:
            errMsg = "name required."
        elif not "email" in request.json:
            errMsg = "email required."
        return errMsg

