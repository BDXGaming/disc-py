class embedMeta:

    def __init__(self, **kwargs):

        self._field_count = kwargs["field_count"]

    @property
    def field_count(self):
        return self._field_count

    @field_count.setter
    def field_count(self, field_count):
        self._field_count = field_count

class embedField:
    def __init__(self, **kwargs):
        self.title = kwargs['title'] or ""
        self.value = kwargs['value'] or ""
        self.inline = kwargs['inline'] or False

    def to_dict(self):
        dict = {"name":self.title, "value":self.value,"inline":self.inline}
        return dict

class Embed(embedMeta):

    def __init__(self, title: str = None, description: str = None, fields: int = 0, color: int = None, **kwargs):

        super().__init__(field_count=fields)

        self.title = title
        self.description = description
        self.color = color
        self.fields = []

    def to_dict(self):
        data = {}

        data['title'] = self.title
        data['description'] = self.description

        data['color'] = self.color
        data["fields"] = self.fields

        return data

    def add_field(self, name:str, value:str, inline:bool = False):
        field = embedField(title=name, value=value, inline=inline)
        self.fields.append(field.to_dict())


