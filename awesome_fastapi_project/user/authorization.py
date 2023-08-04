from awesome_fastapi_project.exceptions import UserIsNotAuthenticated

class Ensure:
    @staticmethod
    def user_is_not_anonymous(user):
        """
            Ensure user is not anonymous.
        """

        if user == "anonymous":
            raise UserIsNotAuthenticated()