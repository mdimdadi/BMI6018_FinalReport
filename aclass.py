#Nothing
"""
this is the Anwars class
"""

class CleanDf(object):
    '''
    This class will take a dataframe and clean it (as in remove all NA values)
    The class representation (__repr__) will return:
    - the dataframe's shape
    - list of column names
    '''
    def __init__(self, df):
        self.__df = df
        self._clean()
    @property
    def df(self):
        return self.__df
    def _clean(self):
        return self.__df.dropna(inplace=True)
    def __str__(self):
        return "column headers: %s"%(self.__df.columns.tolist())
    def __repr__(self):
        return "The dataframe after cleaning has a of shape of (rows, columns)%s and %s"%(self.__df.shape, self.__str__())

class stats_data(CleanDf):

    '''
    This class will calculate that average and total of a specified column given

    Class format will be:
    stats_data('column_name',dataframe)

    if the column name is not found in the dataframe, a key error will be raised

    The class representation will produce:
    - the average
    - the total

    '''

    #import the dataframe as a self in the instructor
    def __init__(self, cl, *args):
        self.__cl = ""
        super(stats_data, self).__init__(*args)
        self.cl = cl


    @property
    def cl(self):
        return self.__cl
    @cl.setter
    def cl(self, c):
        try:
            if c in self.df.columns:
                self.__cl = c
        except KeyError:
            print("invalid column name")
            # this step will help with the __repr__ to print invalid column name

    def avg(self):
        ''' this function calculates the average for the column'''
        return self.df[self.cl].mean()


    def total(self):
        ''' this function calculates the total for the column'''
        return self.df[self.cl].sum()


    def __str__(self):
        return [('avg', self.avg()), ('sum', self.total())]

    def __repr__(self):
        if self.cl:
            return "The average value of %s: %4.2f and the total is: %4.2f"%(self.cl, self.avg(), self.total())
        else:
            return "Column name inputted is invalid, check spelling or name again"
