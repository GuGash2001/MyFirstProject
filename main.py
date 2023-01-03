class alcohol:
    strength=18
class Whiskey(alcohol):
    name='None'
    excerpt=10
    def set (self,name,excerpt,strength):
        self.name=name
        self.excerpt=excerpt
Jameson=Whiskey ()
excerpt=3
trength=40
Jameson.set('Jameson','3', '40')
print(Jameson.name,excerpt,trength)
DD=Whiskey ()
excerpt=12
trength=45
DD.set('DD', '12', '45')
print(DD.name,excerpt,trength)
DjimBeam=Whiskey()
excerpt=8
trength=40
Whiskey.name='DjimBeam'
DjimBeam.set('DjimBeam', '8', '40')
print(DjimBeam.name, excerpt,trength)
class Vine(alcohol):
    name='Nope'
    excerpt=5
    strength=11
    def set (self,name,excerpt,strength):
        self.name=name
        self.excerpt=excerpt
        self.strength=strength
Prosseco=Vine()
excerpt=0
strength=11.5
Prosseco.set('Prosseco','0','11.5')
print(Prosseco.name,excerpt,strength)
