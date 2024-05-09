import pandas as pd


class ServiceData:
    def __init__(self, filename):
        self._filename = filename
        self._type = None
        self._venue = None
        self._link = None
        self._load_service()

    @property
    def filename(self):
        return self._filename

    @property
    def type(self):
        return self._type

    @property
    def venue(self):
        return self._venue

    @property
    def link(self):
        return self._link

    def _load_service(self):
        self._type = self.filename["Type"]
        self._venue = self.filename["Venue"]
        self._link = self.filename["Link"]

    def __str__(self) -> str:
        string = f"Type: {self.type}\n"
        string += f"Venue: {self.venue}\n"
        string += f"Link: {self.link}\n\n"
        return string

    def __repr__(self) -> str:
        repr = f"ServiceData(type={self.type}, venue={self.venue}, link={self.link})"
        return repr


class Services:
    def __init__(self, filename):
        self._filename = filename
        self._services = self._load_service()
        self._services = sorted(self.services, key=lambda x: (x.type, x.venue))

    @property
    def filename(self):
        return self._filename

    @property
    def services(self):
        return self._services

    def get_service_types_ordered(self):
        service_type = []
        for service in self.services:
            if service.type not in service_type:
                service_type.append(service.type)
        return service_type

    def _load_service(self):
        service_df = pd.read_excel(self.filename, sheet_name="Professional_services")
        return [ServiceData(row) for _, row in service_df.iterrows()]

    def __str__(self):
        string = ""
        for service in self.services:
            string += str(service)
        return string

    def __repr__(self):
        repr = f"Service(filename={self.filename}, services={self.services})"
        return repr
