from discpy.user import baseUser


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
        self.title = kwargs.pop("title", None)
        self.value = kwargs.pop("value", None)
        self.inline = kwargs.pop("inline", None)

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
        self._author = None
        self._footer = None
        self._thumbnail = None

    @property
    def author(self):
        return self._author

    @property
    def thumbnail(self):
        return self._thumbnail

    def set_thumbnail(self, url):
        self._thumbnail = url

    def set_author(self, **kwargs):
        _username = kwargs.pop("username", None)
        _avatar_url = kwargs.pop("icon_url", None)

        self._author = baseUser(username=_username, icon_url=_avatar_url)

    def set_footer(self, footer:str):
        self._footer = footer

    def to_dict(self):
        data = {}

        data['title'] = self.title
        data['description'] = self.description
        data['color'] = self.color
        data["fields"] = self.fields

        if(self._author != None):
            data['author'] = self._author.to_dict()

        if(self._footer is not None):
            data['footer'] = {"text": self._footer}

        if(self._thumbnail is not None):
            data['thumbnail'] = {"url": self._thumbnail}

        return data

    def add_field(self, name:str, value:str, inline:bool = False):
        field = embedField(title=name, value=value, inline=inline)
        self.fields.append(field.to_dict())


