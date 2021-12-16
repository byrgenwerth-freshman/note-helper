class NoteParser():
    data_map = {'data': []}
    heading1 = '# '
    heading2 = '## '
    heading3 = '### '
    heading4 = '#### '
    heading5 = '##### '
    heading6 = '###### '
    list_marker = '-'
    sublist_marker_regex = '\t-'

    current_header1 = ''
    current_header2 = ''
    current_header3 = ''
    current_header4 = ''
    current_header5 = ''
    current_header6 = ''

    making_list = False

    def parse_file(self, f_name):
        with open(f_name, 'r') as file_obj:
            for line in file_obj:
                self.line_type(line)

    def line_type(self, line: str):
        if line.startswith(self.heading1):
            self.current_header1 = line.replace(self.heading1, '').strip()
            self.data_map[self.current_header1] = self.data_list()
            self.reset_header(1)
        elif line.startswith(self.heading2):
            self.current_header2 = line.replace(self.heading2, '').strip()
            self.data_map[self.current_header1][
                self.current_header2] = self.data_list()
            self.reset_header(2)
        elif line.startswith(self.heading3):
            self.current_header3 = line.replace(self.heading3, '').strip()
            self.data_map[self.current_header1][self.current_header2][
                self.current_header3] = self.data_list()
            self.reset_header(3)
        elif line.startswith(self.heading4):
            self.current_header4 = line.replace(self.heading4, '').strip()
            self.data_map[self.current_header1][self.current_header2][
                self.current_header3][self.current_header4] = self.data_list()
            self.reset_header(4)
        elif line.startswith(self.heading5):
            self.current_header5 = line.replace(self.heading5, '').strip()
            self.data_map[self.current_header1][self.current_header2][
                self.current_header3][self.current_header4][
                    self.current_header5] = self.data_list()
            self.reset_header(5)
        elif line.startswith(self.heading6):
            self.current_header6 = line.replace(self.heading6, '').strip()
            self.data_map[self.current_header1][self.current_header2][
                self.current_header3][self.current_header4][
                    self.current_header5][
                        self.current_header6] = self.data_list()
            self.making_list = True
        elif line.startswith(self.list_marker) or line.startswith("\t-"):
            self.process_list(line)
        elif line.startswith(self.sublist_marker):
            self.process_sublist(line)
        else:
            if self.current_header6:
                self.data_map[self.current_header1][self.current_header2][
                    self.current_header3][self.current_header4][
                        self.current_header5][
                            self.current_header6]['data'].append(line)
            elif self.current_header5:
                self.data_map[self.current_header1][self.current_header2][
                    self.current_header3][self.current_header4][
                        self.current_header5]['data'].append(line)
            elif self.current_header4:
                self.data_map[self.current_header1][self.current_header2][
                    self.current_header3][self.current_header4]['data'].append(
                        line)
            elif self.current_header3:
                self.data_map[self.current_header1][self.current_header2][
                    self.current_header3]['data'].append(line)
            elif self.current_header2:
                self.data_map[self.current_header1][
                    self.current_header2]['data'].append(line)
            elif self.current_header1:
                self.data_map[self.current_header1]['data'].append(line)
            self.making_list = False

    def process_list(self, line):
        if self.current_header6:
            if self.making_list:
                self.data_map[self.current_header1][self.current_header2][
                    self.current_header3][self.current_header4][
                        self.current_header5][
                            self.current_header6]['data'][-1].append(line)
            else:
                self.data_map[self.current_header1][self.current_header2][
                    self.current_header3][self.current_header4][
                        self.current_header5][
                            self.current_header6]['data'].append([line])
                self.making_list = True
        elif self.current_header5:
            if self.making_list:
                self.data_map[self.current_header1][self.current_header2][
                    self.current_header3][self.current_header4][
                        self.current_header5]['data'][-1].append(line)
            else:
                self.data_map[self.current_header1][self.current_header2][
                    self.current_header3][self.current_header4][
                        self.current_header5]['data'].append([line])
                self.making_list = True
        elif self.current_header4:
            if self.making_list:
                self.data_map[self.current_header1][self.current_header2][
                    self.current_header3][
                        self.current_header4]['data'][-1].append(line)
            else:
                self.data_map[self.current_header1][self.current_header2][
                    self.current_header3][self.current_header4]['data'].append(
                        [line])
                self.making_list = True
        elif self.current_header3:
            if self.making_list:
                self.data_map[self.current_header1][self.current_header2][
                    self.current_header3]['data'][-1].append(line)
            else:
                self.data_map[self.current_header1][self.current_header2][
                    self.current_header3]['data'].append([line])
                self.making_list = True
        elif self.current_header2:
            if self.making_list:
                self.data_map[self.current_header1][
                    self.current_header2]['data'][-1].append(line)
            else:
                self.data_map[self.current_header1][
                    self.current_header2]['data'].append([line])
                self.making_list = True
        elif self.current_header1:
            if self.making_list:
                self.data_map[self.current_header1]['data'][-1].append(line)
            else:
                self.data_map[self.current_header1].append([line])
                self.making_list = True
        else:
            if self.making_list:
                self.data_map['data'][-1].append(line)
            else:
                self.data_map['data'].append([line])
                self.making_list = True

    def process_sublist(self, line):
        if self.making_list:
            self.data_map['data'].append([])

    def process_text(self, line):
        self.making_list = False
        if self.current_header6:
            self.data_map[self.current_header1][self.current_header2][
                self.current_header3][self.current_header4][
                    self.current_header5][self.current_header6]['data'].append(
                        line)
        elif self.current_header5:
            self.data_map[self.current_header1][self.current_header2][
                self.current_header3][self.current_header4][
                    self.current_header5]['data'].append(line)
        elif self.current_header4:
            self.data_map[self.current_header1][self.current_header2][
                self.current_header3][self.current_header4]['data'].append(
                    line)
        elif self.current_header3:
            self.data_map[self.current_header1][self.current_header2][
                self.current_header3]['data'].append(line)
        elif self.current_header2:
            self.data_map[self.current_header1][
                self.current_header2]['data'].append(line)
        elif self.current_header1:
            self.data_map[self.current_header1]['data'].append(line)

    def reset_header(self, number):
        if number <= 5:
            self.current_header6 = ''
        if number <= 4:
            self.current_header5 = ''
        if number <= 3:
            self.current_header4 = ''
        if number <= 2:
            self.current_header3 = ''
        if number <= 1:
            self.current_header2 = ''

    @staticmethod
    def data_list():
        return {'data': []}
