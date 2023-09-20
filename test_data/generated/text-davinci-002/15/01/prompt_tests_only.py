def test_spaces():
  text = '    '
  assert capitalize(text) == ''

def capitalize(text):
  # your code goes here
  return text.title()