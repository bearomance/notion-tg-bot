class Page:
    def __init__(self):
        self.properties = {}

    def title(self, key, value):
        self.properties[key] = {
            "title": [
                {
                    "text": {
                        "content": value
                    }
                }
            ]
        }
        return self

    def date(self, key, value):
        self.properties[key] = {
            "date": {
                "start": value
            }
        }
        return self

    def rich_text(self, key, value):
        self.properties[key] = {
            "rich_text": [
                {
                    "text": {
                        "content": value
                    }
                }
            ]
        }
        return self

    def number(self, key, value):
        self.properties[key] = {
            "number": float(value)
        }
        return self

    def checkbox(self, key, value):
        self.properties[key] = {
            "checkbox": bool(value)
        }
        return self

    def select(self, key, value):
        self.properties[key] = {
            "select": {
                "name": value
            }
        }
        return self

    def multi_select(self, key, values):
        self.properties[key] = {
            "multi_select": [
                {
                    "name": value
                } for value in values
            ]
        }
        return self

    def build(self):
        return self.properties