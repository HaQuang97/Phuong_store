from datetime import datetime


def convert_string_to_date(string, format):
    try:
        return datetime.strptime(string, format)
    except:
        raise Exception("en wrong in format datetime!")


class FixJustInTime:
    
    def on_content_required(self, file):
        try:
            file.generate()
        except:
            pass
    
    def on_existence_required(self, file):
        try:
            file.generate()
        except:
            pass
