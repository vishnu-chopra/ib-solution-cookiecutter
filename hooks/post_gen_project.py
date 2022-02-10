import os
import json
import shutil


def refine_config(config):
  for key in config.keys():
    if config[key] == "":
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
      "icon_url": "icon.png" if "{{cookiecutter.icon_url}}" != "" else None,
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
  with open(os.path.join(os.getcwd(), "package.json"), "w") as file:
    file.write(json.dumps(config))


def copy_over_files():
  icon_url = "{{cookiecutter.icon_url}}"
  if icon_url != "":
    if not os.path.isfile(icon_url):
      print(f"WARNING: No file {icon_url} exists, not copying to icon.png")
    shutil.copyfile(icon_url, os.path.join(
        os.path.join(os.getcwd(), "solution"), "icon.png"))


write_package_config()
copy_over_files()
