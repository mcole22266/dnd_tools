from random import choice

def greek_name(male=True):
    if male:
        return choice([
            'Pittheus', 'Machaon', 'Aias', 'Axylus', 'Anakletos', 'Lycus', 'Amopaon', 
            'Paopeus', 'Helgesippos', 'Naubolus', 'Phaedo', 'Cleon', 'Rhadamanthos', 'Kritoboulos', 'Paios', 
            'Hermogenes', 'Gallus', 'Oenemaus', 'Phaidon', 'Spinther', 'Pylas', 'Antigonos', 'Proreus', 
            'Eudorus', 'Elatreus', 'Evenios', 'Aristodemos', 'Chalcon', 'Elpides', 'Epiphanes', 'Mys', 
            'Plades', 'Olympiodorus', 'Laogonus', 'Niarchos', 'Alkibiades', 'Protus', 'Proreus', 'Trophnus', 
            'Hippotion', 'Cobon', 'Autolycus', 'Erechtheus', 'Threspotus', 'Polyas', 'Theramenes', 'Radamanthos', 
            'Kroisos', 'Gnipho', 'Phrynichos', 'Asonides', 'Alastor', 'Alkestis', 'Cleodaeos', 'Eurysthenes', 
            'Peritas', 'Euripides', 'Peleus', 'Antemion', 'Lemnus', 'Salmoneus', 'Damasippus', 'Zeuxidamos', 
            'Agesilaus', 'Praxites', 'Kyros', 'Dorian', 'Synesius', 'Iphicrates', 'Sosibios', 'Maro', 
            'Xanthippus', 'Eurydemon', 'Eudorus', 'Charopos', 'Diokles', 'Chrysolorus', 'Hephaestos', 'Phalinos', 
            'Kannadis', 'Leonnatos', 'Athamas', 'Anaxandrides', 'Triopas', 'Cleandros', 'Epitrophos', 'Ion', 
            'Antigenes', 'Iphitos', 'Simoisius', 'Theos', 'Echëeus', 'Ennaeus', 'Idaios', 'Hermogenes', 
            'Theodoros', 'Myrsinus', 'Barates', 'Lysikles', 'Choerilos', 'Harpagos', 'Cisseus', 'Gordias', 
            'Gorgias', 'Autodikos', 'Tydeides', 'Choeros', 'Hypenor', 'Kapaneus', 'Tros'
        ])
    else:
        return choice([
            'Kassandra', 'Dirce', 'Herophile', 'Anastasia', 'Ismene', 'Phigaleia', 
            'Berenike', 'Omphale', 'Megare', 'Orithyia', 'Glauce', 'Caleope', 'Phylace', 'Alcestis', 
            'Labda', 'Pyrrha', 'Drosis', 'Phylomedusa', 'Actë', 'Kynna', 'Ianessa', 'Melantho', 
            'Helike', 'Philinna', 'Nausicaa', 'Iomene', 'Metis', 'Agape', 'Deiphobe', 'Theodotis', 
            'Castianiera', 'Clymene', 'Oenone', 'Althaia', 'Aithra', 'Theophane', 'Chrysothemis', 'Iphitheme', 
            'Philona', 'Hypsipyle', 'Harmodias', 'Althea', 'Chryse', 'Clymere', 'Glauce', 'Dexamene', 
            'Philomache', 'Lalage', 'Labda', 'Cilissa', 'Oreithuia', 'Ianessa', 'Polyxena', 'Agamede', 
            'Ianthe', 'Elpir', 'Aganippe', 'Pherenike', 'Procris', 'Hecuba', 'Epicaste', 'Gygaea', 
            'Hekaline', 'Otonia', 'Cydippe', 'Polyxena', 'Xene', 'Caleope', 'Milto', 'Cilissa', 
            'Pasiphae', 'Medea', 'Thisbe', 'Leda', 'Milto', 'Galatea', 'Prone', 'Iaera', 
            'Laodameia', 'Charis', 'Hermione', 'Iomene', 'Limnoreia', 'Philinna', 'Isadora', 'Appollonia', 
            'Theresa', 'Arete', 'Doris', 'Astera', 'Iaera', 'Cydippe', 'Baucis', 'Phylomedusa', 
            'Europa', 'Europa', 'Iole', 'Philea', 'Berenike', 'Timo', 'Aethre', 'Panora', 
            'Erigone', 'Amarhyllis', 'Jocasta', 'Polydamna', 'Ianeira', 'Phaia', 'Ada', 'Kleopatra', 
            'Aerope', 'Hellanike', 'Haidee', 'Erigone', 'Psamathe', 'Katana', 'Hippolyta', 'Perse', 
            'Alkmena', 'Arsinoe'
        ])