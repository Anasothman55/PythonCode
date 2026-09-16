from rich import print


class Morris:
  def __init__(
      self,
      title: str,
      up: Morris | None = None,
      down: Morris | None = None,
      right: Morris | None = None,
      left: Morris | None = None,
  ):
    self.title = title
    self.up = up
    self.down = down
    self.right = right
    self.left = left

  def add_up(self, moris: Morris):
    self.up = moris

  def add_down(self, moris: Morris):
    self.down = moris

  def add_right(self, moris: Morris):
    self.right = moris

  def add_left(self, moris: Morris):
    self.left = moris




















