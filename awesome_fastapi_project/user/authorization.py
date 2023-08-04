from awesome_fastapi_project.exceptions import UserIsNotAuthenticated

class Ensure:
    @staticmethod
    def user_is_not_anonymous(self, user):
        """
            Ensure user is not anonymous.
        """

        if user == "anonymous":
            raise UserIsNotAuthenticated()