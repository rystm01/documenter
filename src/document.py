from anthropic import Anthropic
import os
import re
from src.utils import should_print
from openai import OpenAI
from together import Together




class Documenter:

  SYSTEM_PROMPT = """You generate markdown that documents the contents of code files. 
                    Only respond with Documentation. Clearly demarcate the start of the file with 
                    the file name. Include the white space at the end, as more documentation will likely be
                    appended to your result. """
  

  def __init__(self, path, api_key=None, filewise=True, provider='claude', model='claude-3-5-sonnet-latest'):
    self.path = path
    self.markdown = ""
    self.num = 0
    self.filewise=filewise
    self.api_key=False
    self.provider=provider
    self.model=model

    with open("documently_summary", "w") as file:
      file.write("This is a summary of what each file does")

    print(self.provider)
    print(self.model)
    if(api_key):
        self.api_key=True
        env_var = self.provider.upper() + '_API_KEY'
        os.environ[env_var] = api_key
    self.files = set({})
  
  def __del__(self):
    if self.api_key:
      env_var = self.provider.upper() + 'API_KEY'
      os.environ.pop(env_var)

    
  def _read_file(self, filename):
    with open(filename, 'r') as file:
      text = file.read()
    
    return text
    
  def _document_file(self, filename):
    """
    generates markdown documentation for the code in a file
    """
    code = self._read_file(filename)
    if self.provider == 'claude':
      
      messages = [{"role" : "user", "content" : f"Please Document this code. This file is called {filename}:" + code}]

      response = Anthropic().messages.create(
        model=self.model,
        system=Documenter.SYSTEM_PROMPT,
        messages=messages
      )
      text=response.content[0].text
      messages.append({"role": "assistant", "content": text})

      messages.append({"role" : "user", "content" : "Now write a 1-2 paragraph summary of the code. Include the filename and directory. "
      "Focus on the general purpose of the file how it works within the project."})
      summary_res = response = Anthropic().chat.completions.create(
        messages=messages,
        model=self.model
      )
      summary=summary_res.content[0].text


    elif self.provider == 'openai':
      messages = [ {'role' : 'system', 'content' : Documenter.SYSTEM_PROMPT },
                  {"role" : "user", "content" : f"Please Document this code. This file is called {filename}:" + code}]
      response = OpenAI().chat.completions.create(
        messages=messages,
        model=self.model
      )
      text = response.choices[0].message.content

      messages.append({"role": "assistant", "content": text})

      messages.append({"role" : "user", "content" : "Now write a 1-2 paragraph summary of the code. Include the filename and directory. "
      "Focus on the general purpose of the file how it works within the project."})
      summary_res = response = OpenAI().chat.completions.create(
        messages=messages,
        model=self.model
      )
      summary=summary_res.choices[0].message.content

    
    elif self.provider == "together":
      messages = [ {'role' : 'system', 'content' : Documenter.SYSTEM_PROMPT },
                  {"role" : "user", "content" : f"Please Document this code. This file is called {filename}:" + code}]
      response = Together().chat.completions.create(
        messages=messages,
        model=self.model
      )
      text = response.choices[0].message.content
      messages.append({"role" : "user", "content" : "Now write a 1-2 paragraph summary of the code. Include the filename and directory. "
      "Focus on the general purpose of the file how it works within the project."})
      summary_res = response = Together().chat.completions.create(
        messages=messages,
        model=self.model
      )
      summary=summary_res.choices[0].message.content
      text = response.choices[0].message.content


    with open("documently_summary", "a")as file:
      file.write(summary)
    self.write_md(text, filename)
    return text


 
  
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


  def summarize(self):
    with open("documently_summary") as file:
      summaries = file.read()
    
    prompt = """This is a collection of summaries of code files which were in the same coding project 
                (conceived independently from eachother). Summarize the entire project, noting the connections 
                between files and modules. Try to explain the design of the system. Respond in markdown.
            """
    messages = [{"role" : "user", "content" : prompt + summaries}]

    if self.provider == 'claude':
      response = Anthropic().messages.create(
        model=self.model,
        system=Documenter.SYSTEM_PROMPT,
        messages=messages
      )
      text=response.content[0].text
      pass
    elif self.provider == 'openai':
      response = OpenAI().chat.completions.create(
        messages=messages,
        model=self.model
      )
      text = response.choices[0].message.content
    elif self.provider == "together":
      response = Together().chat.completions.create(
        messages=messages,
        model=self.model
      )
      text = response.choices[0].message.content
    
    self.write_md(text, "project_summary.md")

    

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


    