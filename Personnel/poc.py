# NahamCon2021 Personnel

# python3 poc.py "query" "setting as int"

import re
import sys

text = "Antlia Apus Aquarius Aquila Ara Aries Auriga Bootes Caelum Camelopardalis Cancer Canes Venatici Canis Major Canis Minor Capricornus Carina Cassiopeia Centaurus Cepheus Cetus Chamaeleon Circinus Columba Coma Berenices Corona Australis Corona Borealis Corvus Crater Crux Cygnus Delphinus Dorado Draco Equuleus Eridanus Fornax Gemini Grus Hercules Horologium Hydra Hydrus Indus Lacerta Leo Leo Minor Lepus Libra Lupus Lynx Lyra Mensa Microscopium Monoceros Musca Norma Octans Ophiuchus Orion Pavo Pegasus Perseus Phoenix Pictor Pisces Piscis Austrinus Puppis Pyxis Reticulum Sagitta Sagittarius Scorpius Sculptor Scutum Serpens Sextans Taurus Telescopium Triangulum Triangulum Australe Tucana Ursa Major Ursa Minor Vela Virgo Volans Vulpecula\nflag{f0e659b45b507d8633065bbd2832c627}"

try:
    r = re.findall(sys.argv[1], text, flags=int(sys.argv[2]))[0]
except:
    r = ""

print(r)
