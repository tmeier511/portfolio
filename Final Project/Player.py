class Player:
    
    _name = ''
    
    
    def __init__(self, name=''):
        self.name = name
        self.wins = 0
        self.hand = []
    
    def __str__(self):
        return str(self.wins)
    
    @property
    def name(self):
        """Gets name.

        Returns:
            str: name

        """
        return self._name
    
    
    @name.setter
    def name(self, value):
        """Sets name.

        Args:
            value (str): name
            
        Raises:
            Assertion Error: Value must be a valid str type
    
        """
        
        try:
            if not isinstance (value, str):
                raise TypeError
            self._name = value
        except TypeError:
            raise
        