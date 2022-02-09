import os
import json

def refine_config(config):
  for key in config.keys():
    if config[key] == "None":
      config[key] = None
  
  if config["authors"] != None:
    items = config["authors"].split(',')
    config["authors"] = [x.strip() for x in items]

  config["beta"] = config["beta"].lower() == "true"

  config["encryption_config"] = {
    "encryption_type": config["encryption_type"]
  }

  config.pop("encryption_type")
  return config

def write_package_config():
  config = {
  "name": "{{cookiecutter.name}}",
  "version": "{{cookiecutter.version}}",
  "icon_url": "{{cookiecutter.icon_url}}",
  "keywords": "{{cookiecutter.keywords}}",
  "category": "{{cookiecutter.category}}",
  "short_description": "{{cookiecutter.short_description}}",
  "long_description": "{{cookiecutter.long_description}}",
  "authors": "{{cookiecutter.authors}}",
  "beta": "{{cookiecutter.beta}}",
  "solution_type": "{{cookiecutter.solution_type}}",
  "encryption_type": "{{cookiecutter.encryption_type}}"
  }

  refined_config = refine_config(config)
  with open( os.path.join(os.path.join(os.getcwd(),"solution"),"package.json"), "w") as file:
    file.write(json.dumps(config))

write_package_config()