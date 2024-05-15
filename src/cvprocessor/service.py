"""
This module contains the ServiceData and Services classes.
"""
import pandas as pd


class ServiceData:
    """
    The ServiceData class is used to store the service data.

    Attributes:
    type (str): The type of the service.
    venue (str): The venue of the service.
    link (str): The link to the service.
    """

    def __init__(self):
        self.type = str()
        self.venue = str()
        self.link = str()

    def get_type(self) -> str:
        """
        Get the type of the service.
        """
        return self.type

    def get_venue(self) -> str:
        """
        Get the venue of the service.
        """
        return self.venue

    def get_link(self) -> str:
        """
        Get the link to the service.
        """
        return self.link

    def load(self, filename) -> None:
        """
        Load the service data.
        """
        self.type = filename["Type"]
        self.venue = filename["Venue"]
        self.link = filename["Link"]

    def __str__(self) -> str:
        string = f"Type: {self.type}\n"
        string += f"Venue: {self.venue}\n"
        string += f"Link: {self.link}\n"
        return string

    def __repr__(self) -> str:
        string = (
            f"ServiceData("
            f"type={self.type}, "
            f"venue={self.venue}, "
            f"link={self.link})"
        )
        return string


class Services:
    """
    The Services class is used to store the service data.

    Attributes:
    services (list): The list of services.
    """

    def __init__(self):
        self.services = []

    def get_service_types_ordered(self):
        """
        Get the service types in order.
        """
        service_type = []
        for service in self.services:
            if service.type not in service_type:
                service_type.append(service.type)
        return service_type

    def load(self, filename):
        """
        Load the service data.
        """
        service_df = pd.read_excel(
            filename, sheet_name="Professional_services")
        for _, row in service_df.iterrows():
            service = ServiceData()
            service.load(row)
            self.services.append(service)

    def __str__(self):
        string = ""
        for service in self.services:
            string += str(service) + "\n"
        return string

    def __repr__(self):
        string = f"Services(services={repr(list(self.services))})"
        return string

    def __iter__(self):
        return iter(self.services)
