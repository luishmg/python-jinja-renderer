from jinja2 import Environment, FileSystemLoader
import os
import re


class JinjaRender:
    def __init__(self, name, parameters, output=None, force=False):
        self.file_name = name
        self.parameters = parameters
        self.output = output
        self.force = force

    def RenderTemplate(self):
        file_loader = FileSystemLoader('.')
        env = Environment(loader=file_loader)
        template = env.get_template(self.file_name)
        return template.render(self.parameters)

    def RenderJinjaFile(self):
        if re.match(r'^.*/.*$', self.file_name):
            file_name = ".".join(self.file_name.split("/")[-1].split(".")[:-1])
        else:
            file_name = ".".join(self.file_name.split(".")[:-1])
        if self.output:
            if os.path.isdir(self.output):
                if re.match(r'^.*/$', self.output):
                    file_name = self.output + file_name
                else:
                    file_name = self.output + "/" + file_name
            else:
                file_name = self.output
        if ((os.path.isfile(file_name)
             and self.force) or not os.path.isfile(file_name)):
            with open(file_name, "w") as jinjaFile:
                jinjaFile.write(self.RenderTemplate())
                if os.path.isfile(file_name):
                    return "Succeded in rendering the file"
                else:
                    return "Failed to render the file"
        else:
            return "Failed to render the file, it already exists"
