class persons():

   def my_func(self):

    return f"My name is {self.name}.I read in class {self.Class}"

    

Santosh =persons()

Belal=persons()

Santosh.name="Santosh"

Santosh.Class="Nine"

Belal.name="Hari"

Belal.Class="Ten"

print(Belal.my_func())

print(Santosh.my_func())

class person():

    def __init__(self,nam,kaksha,Roll):

        self.name=nam

        self.kaksha=kaksha

        self.Roll=Roll

    

x=person("Manoj","Eleven","Six")

print(x.name)
