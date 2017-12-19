class obiekt(object):
    def __init__(self, watwat):
        self._coś = watwat

    @property
    def coś(self,):
        print("Coś działa")
        return self._coś

a = obiekt(5)
b = a.coś
print(b)
input("enter")