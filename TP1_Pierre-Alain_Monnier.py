from MaBase_MIB import *

les_gardiens={g.Nom for g in BaseGardiens}
les_villes_agents={Agent.Ville for Agent in BaseAgents}
{'Hesperos', 'Kalgan', 'Terminus', 'Uco'}
triples={(alien.NoCabine, alien.Nom, gardien.Nom) for alien in BaseAliens  for gardien in BaseGardiens if gardien.NoCabine == alien.NoCabine}

Q3={('1', 'Zorglub', 'Branno'),('2', 'Blorx', 'Darell'),('3', 'Urxiz', 'Demerzel'),('4', 'Darneurane', 'Seldon'),('5', 'Zbleurdite', 'Seldon'),('6', 'Mulzo', 'Hardin'),('7', 'Zzzzzz', 'Trevize'),('8', 'Arghh', 'Pelorat'),('9', 'Joranum', 'Riose')}
Q4={(Alien.Nom, allee.NoAllee) for Alien in BaseAliens for allee in BaseCabines if Alien.NoCabine==allee.NoCabine}
Q5={(Alien.Nom, Cabine.NoAllee) for Alien in BaseAliens for Cabine in BaseCabines if Alien.NoCabine==Cabine.NoCabine and Cabine.NoAllee=="2"}
Q6={(alien.Planete) for alien in BaseAliens if float(alien.NoCabine)%2==0}
Q7={ (alien.Nom) for alien in BaseAliens for gardien in BaseGardiens for agent in BaseAgents if alien.NoCabine==gardien.NoCabine and gardien.Nom==agent.Nom and agent.Ville=='Terminus'}
Q8={ (gardien.Nom) for gardien in BaseGardiens for alien in BaseAliens for miam in BaseMiams if miam.Aliment=='Bortsch' and miam.NomAlien==alien.Nom and alien.Sexe=='F' and alien.NoCabine==gardien.NoCabine }
Q9={ (cabine.NoCabine) for cabine in BaseCabines for gardien in BaseGardiens for alien in BaseAliens for agent in BaseAgents if (gardien.Nom==agent.Nom and agent.Ville=='Terminus' and gardien.NoCabine==cabine.NoCabine) or (alien.Sexe=='F' and alien.NoCabine==cabine.NoCabine) }
Q10={ (gardien.Nom,miam.Aliment) for gardien in BaseGardiens for miam in BaseMiams for alien in BaseAliens if miam.NomAlien==alien.Nom and alien.NoCabine==gardien.NoCabine and miam.Aliment[0]==gardien.Nom[0] }
Q11={ (alien.Nom) for alien in BaseAliens if alien.Planete=='Euterpe' }
Q12={ (Alien.Nom) for Alien in BaseAliens if 'x' in Alien.Nom }
Q13 = {(Alien.Nom, Agent.Nom) for Alien in BaseAliens for Gardien in BaseGardiens for Agent in BaseAgents if 'x' in Alien.Nom if Agent.Ville == 'Terminus' if Agent.Nom == Gardien.Nom if Gardien.NoCabine == Alien.NoCabine}
Q14a={ (Alien.Nom) for Alien in BaseAliens for Miam in BaseMiams if Alien.Sexe == 'M' if Alien.Planete == 'Trantor' if Alien.Nom == Miam.NomAlien if Miam.Aliment == 'Bortsch'}
Q14b={ (Alien.Nom) for Alien in BaseAliens for Gardien in BaseGardiens for Agent in BaseAgents if Alien.Sexe == 'M' if Alien.Planete == 'Trantor' if Alien.NoCabine == Gardien.NoCabine if Gardien.Nom == Agent.Nom if Agent.Ville == 'Terminus'}
