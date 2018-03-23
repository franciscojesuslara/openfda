class Molecle():
	def __init__(self,oxygen, hydrogen):
		self.oxygen = oxygen
		self.hydrogen = hydrogen
	def get_electrons(self):
        return self.electrons
    
    def get_protons(self):
        return self.protons	
water = Molecle(hydrogen =2,oxygen = 1)
print("The water molecle has %i of hydrogen atoms" % hydrogen.get_electrons())
print("The water molecle has %i of oxygen atoms " % hydrogen.get_protons())
class Atom():
    def __init__(self, electrons, protons):
        self.electrons = electrons
        self.protons = protons

    def get_electrons(self):
        return self.electrons
    
    def get_protons(self):
        return self.protons

hydrogen = Atom(electrons =1, protons = 1)
print("The hydrogen atom has %i electrons" % hydrogen.get_electrons())
print("The hydrogen atom has %i protons" % hydrogen.get_protons())
oxygen = Atom(electrons =8, protons = 8)
print("The oxygen atom has %i electrons" % oxygen.get_electrons())
print("The oxygen atom has %i protons" % oxygen.get_protons())

		
