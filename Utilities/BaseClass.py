import pytest

from Utilities.common_emails import outlook_signin


@pytest.mark.usefixtures("cp", "credentials")
class Customer_portal:
    pass

    def outlook_signin_helper(self):
        """
        Reusable method for signing into Outlook.
        """
        country_variables = self.country_variables
        outlook_signin(self.driver, country_variables)