from anthropic import Anthropic
import os
import re
from src.utils import should_print




class Documenter:

  SYSTEM_PROMPT = """You generate markdown that documents the contents of code files. 
                    Only respond with Documentation. Clearly demarcate the start of the file with 
                    the file name. Include the white space at the end, as more documentation will likely be
                    appended to your result. """
  

  def __init__(self, path, api_key=None, filewise=True):
    self.path = path
    self.markdown = ""
    self.num = 0
    self.filewise=filewise
    self.api_key=False
    if(api_key):
      self.api_key=True
      os.environ['ANTHROPIC_API_KEY'] = api_key
    self.files = set({})
  
  def __del__(self):
    if self.api_key:
      os.environ.pop('ANTHROPIC_API_KEY')

    
  def _read_file(self, filename):
    with open(filename, 'r') as file:
      text = file.read()
    
    return text
    
  def _document_file(self, filename):
    """
    generates markdown documentation for the code in a file
    """
    code = self._read_file(filename)
    messages = [{"role" : "user", "content" : f"Please Document this code. This file is called {filename}:" + code}]

    response = Anthropic().messages.create(
      model='claude-3-5-sonnet-latest',
      max_tokens=8192,
      system=Documenter.SYSTEM_PROMPT,
      messages=messages
    )
    text=response.content[0].text

    self.write_md(text, filename)
 
  
  def document(self, path, tabs, hidden=False, all_=True, extensions=None):
    for filename in os.listdir(path):
      f = os.path.join(path, filename)

      is_dir = os.path.isdir(f)

      if(should_print(os.path.basename(f), hidden, all_, is_dir, extensions=extensions)):
        print("documenting " + f)
        if not is_dir:
          self._document_file(f)
        # print(os.path.basename(f))
        if(is_dir): 
          self.document(f, tabs+1, hidden, all_, extensions=extensions)


  def write_md(self, md, filename):
    """writes the result result to a markdown file"""
    try:
      if not self.filewise:
        filename = "./documentation.md"
      with open(f"{filename}.md", "a") as file:
        file.write(md)
      self.files.add(filename)
      self.num+=1
    except:
      return "error writing to file"


    