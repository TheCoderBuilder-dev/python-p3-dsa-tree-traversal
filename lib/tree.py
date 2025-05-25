class Tree:
  def __init__(self, root=None):
    self.root = root

  def get_element_by_id(self, id):
    return self._dfs(self.root, id)

  def _dfs(self, node, target_id):
    if node is None:
      return None

    if node.get("id") == target_id:
      return node

    for child in node.get("children", []):
      found = self._dfs(child, target_id)
      if found:
        return found

    return None

