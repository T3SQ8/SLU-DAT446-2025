class Robot:
  def __init__(self):
    self.x, self.y = 0, 0
    self.directions = ('NORTH', 'EAST', 'SOUTH', 'WEST')
    self.direction = self.directions[0]

  def forward(self, steps):
      # NOTE optimalt sätt att göra detta, tyvärr inte
      # NOTE implementerat i Self-Practice (lades till Python år 2021)
      # match self.direction:
      #   case 'NORTH':
      #       self.y += steps
      #   case 'EAST':
      #       self.x += steps
      #   case 'SOUTH':
      #       self.y -= steps
      #   case 'WEST':
      #       self.x -= steps
    if self.direction == 'NORTH':
      self.y += steps
    elif self.direction == 'EAST':
      self.x += steps
    elif self.direction == 'SOUTH':
      self.y -= steps
    elif self.direction == 'WEST':
      self.x -= steps

  def turnRight(self):
    index = self.directions.index(self.direction) # get index of current direction
    index = (index + 1) % len(self.directions) # get next direction, jump back if at the end
    self.direction = self.directions[index]

  def turnLeft(self):
    index = self.directions.index(self.direction)
    index = (index - 1) % len(self.directions)
    self.direction = self.directions[index]

  def getDirection(self):
    return self.direction

  def getPosition(self):
    return (self.x, self.y)

