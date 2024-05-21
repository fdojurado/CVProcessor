"""
This module contains the ServiceData and Services classes.
"""
import pandas as pd

from cvprocessor.links.links import Link


class ServiceData:
    """
    The ServiceData class is used to store the service data.

    Attributes:
    type (str): The type of the service.
    venue (str): The venue of the service.
    links (Link): The links of the service.
    """

    def __init__(self):
        self.venue = str()
        self.link = Link()

    def get_venue(self) -> str:
        """
        Get the venue of the service.
        """
        return self.venue

    def load(self, df) -> None:
        """
        Load the service data.
        """
        self.venue = df["Venue"]
        self.link.type = df["Type"]
        self.link.url = df["Link"]

    def __repr__(self) -> str:
        string = (
            f"ServiceData("
            f"venue={self.venue}, "
            f"link={repr(self.link)})"
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

    def get_services_ordered(self):
        """
        Get the services ordered by link type.
        """
        services_ordered = []
        for service in self:
            if service.link.get_type() not in services_ordered:
                services_ordered.append(service.link.get_type())
        return services_ordered

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
        # Sort the services by venue alphabetically
        self.services = sorted(self.services, key=lambda x: x.venue)

    def __repr__(self):
        string = f"Services(services={repr(list(self.services))})"
        return string

    def __iter__(self):
        return iter(self.services)
