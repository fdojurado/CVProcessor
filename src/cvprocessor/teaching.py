import pandas as pd


class YearData:
    def __init__(self, year_range):
        self._year_range = year_range
        self._start_year = None
        self._end_year = None
        self._process_year_range()

    @property
    def year_range(self):
        return self._year_range

    @property
    def start_year(self):
        return self._start_year

    @property
    def end_year(self):
        return self._end_year

    def format_year(self, year):
        year = year.strip()
        year = pd.to_datetime(year, format="%b %Y")
        return year

    def _process_year_range(self):
        year_range = self.year_range.split("-")
        self._start_year = self.format_year(year_range[0])
        self._start_year = pd.to_datetime(self.start_year, format="%b %Y")
        if len(year_range) > 1:
            self._end_year = self.format_year(year_range[1])
            self._end_year = pd.to_datetime(self.end_year, format="%b %Y")
        else:
            self._end_year = None

    def __str__(self):
        string = f"Year range: {self.year_range}\n"
        string += f"Start year: {self.start_year}\n"
        string += f"End year: {self.end_year}\n"
        return string

    def __repr__(self):
        string = f"YearData(year_range={self.year_range}, start_year={self.start_year}, end_year={self.end_year})"
        return string


class TeachingData:
    def __init__(self, filename):
        self._filename = filename
        self._year_range = None
        self._start_year = None
        self._end_year = None
        self._position = None
        self._course = None
        self._link = None
        self._type = None
        self._institution = None
        self._supervisor = None
        self._responsibilities = None
        self._load_teaching()

    @property
    def filename(self):
        return self._filename

    @property
    def year(self):
        return self._year_range

    @property
    def start_year(self):
        return self._start_year

    @property
    def end_year(self):
        return self._end_year

    @property
    def position(self):
        return self._position

    @property
    def course(self):
        return self._course

    @property
    def link(self):
        return self._link

    @property
    def type(self):
        return self._type

    @property
    def institution(self):
        return self._institution

    @property
    def supervisor(self):
        return self._supervisor

    @property
    def responsibilities(self):
        return self._responsibilities

    def get_start_year(self):
        min_year = 1e6
        date = None
        for year in self.year:
            if int(year.start_year.year) < min_year:
                min_year = int(year.start_year.year)
                date = year.start_year
        return date

    def get_end_year(self):
        max_year = -1
        date = None
        for year in self.year:
            if year.end_year is not None:
                if int(year.end_year.year) > max_year:
                    max_year = int(year.end_year.year)
                    date = year.end_year
        return date

    def process_year_data(self):
        self._year_range = self.filename["Year"]
        self._year_range = self._year_range.split(";")
        self._year_range = list(filter(None, self._year_range))
        year_list = []
        for year in self._year_range:
            year_list.append(YearData(year))
        self._year_range = year_list
        # Sort the year data by start year
        self._year_range = sorted(
            self.year, key=lambda x: x.start_year, reverse=True)

    def _load_teaching(self):
        self.process_year_data()
        self._start_year = self.get_start_year()
        self._end_year = self.get_end_year()
        self._position = self.filename["Position"]
        self._course = self.filename["Course"]
        self._link = self.filename["Link"]
        self._type = self.filename["Type"]
        self._institution = self.filename["Institution"]
        self._supervisor = self.filename["Supervisor"]
        self._responsibilities = self.filename["Responsibilities"]

    def __str__(self):
        year_data = ""
        for year in self.year:
            year_data += str(year)
        string = f"Year range: {year_data}\n"
        string += f"Start year: {self.start_year}\n"
        string += f"End year: {self.end_year}\n"
        string += f"Position: {self.position}\n"
        string += f"Course: {self.course}\n"
        string += f"Link: {self.link}\n"
        string += f"Type: {self.type}\n"
        string += f"Institution: {self.institution}\n"
        string += f"Supervisor: {self.supervisor}\n"
        string += f"Responsibilities: {self.responsibilities}\n\n"
        return string

    def __repr__(self):
        string = f"TeachingData(year_range={self.year}, start_year={self.start_year}, end_year={self.end_year}, position={self.position}, course={self.course}, link={self.link}, type={self.type}, institution={self.institution}, department={self.department}, country={self.country}, supervisor={self.supervisor}, responsibilities={self.responsibilities})"
        return string


class Teaching:
    def __init__(self, filename):
        self._filename = filename
        self._teaching = self._load_teaching()
        # Sort the teaching data by type then by year
        self._teaching = sorted(
            self.teaching, key=lambda x: (x.type, x.start_year), reverse=True)

    @property
    def filename(self):
        return self._filename

    @property
    def teaching(self):
        return self._teaching

    def get_teaching_type_ordered(self):
        teaching_type = []
        for teaching in self.teaching:
            if teaching.type not in teaching_type:
                teaching_type.append(teaching.type)
        return teaching_type

    def get_num_teaching_by_document_type(self, teaching_type):
        count = 0
        for teaching in self.teaching:
            if teaching.type == teaching_type:
                count += 1
        return count

    def _load_teaching(self):
        teaching_df = pd.read_excel(self.filename, sheet_name="Teaching")
        return [TeachingData(teaching) for _, teaching in teaching_df.iterrows()]

    def __str__(self):
        string = ""
        for teaching in self.teaching:
            string += str(teaching)
        return string

    def __repr__(self):
        string = f"Teaching(filename={self.filename}, teaching={self.teaching})\n"
        return string
