from flask_restful import Resource
from flask_pydantic import validate

from app.api.schemas.user import UserCreate, UserEdit


class UserResource(Resource):
    def get(self, user_id: int):
        """
        Get user profile info
        """

    @validate()
    def post(self, user_id: int, user_data: UserCreate):
        """
        Create new user
        """

    @validate()
    def put(self, user_ud: int, changes: UserEdit):
        """
        Edit user profile
        """
        # Get username, password from changes and handle them
        if changes.password:
            pass  # change password

    def delete(self, user_id: int):
        """
        Delete user profile
        """
