from note_parser import NoteParser


class TestNoteParser():
    def test_keys_from_md(self):
        np = NoteParser()
        np.parse_file('test_md')
        assert ['data', 'Aliquet lectus'] == list(np.data_map.keys())
        assert ['data',
                'Summary'] == list(np.data_map['Aliquet lectus'].keys())
        assert [
            'data', 'Section One: Lorem ipsum dolor sit amet',
            'Section Two: Nulla pellentesque dignissim:'
        ] == list(np.data_map['Aliquet lectus']['Summary'].keys())
        assert [
            'data', 'Chapter One: Tincidunt dui ut ornare',
            'Chapter Two: Dolor purus', 'Chapter Three: Dignissim sodales',
            'Chapter Four: Diam vel quam elementum',
            'Chapter Five: Sed cras ornare arcu dui vivamus',
            'Chapter Six: dio pellentesque diam'
        ] == list(np.data_map['Aliquet lectus']['Summary']
                  ['Section One: Lorem ipsum dolor sit amet'].keys())

    def test_parse_list(self):
        list_string = [
            "- Lorem ipsum",
            "\t- dolor sit amet",
            "\t- dolor sit amet",
            "\t- dolor sit amet",
        ]
        np = NoteParser()
        for line in list_string:
            np.line_type(line)
        assert {
            'data': [[
                '- Lorem ipsum', '\t- dolor sit amet', '\t- dolor sit amet',
                '\t- dolor sit amet'
            ]]
        } == np.data_map
