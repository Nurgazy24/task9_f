
# [фа́циле ди́кту, диффи́циле фа́кту]
# Легко сказать, трудно сделать.

#"Facile dictu, difficile factu."


s = "facile dictu, difficile factu."

if s.count("f") >= 2:
    print(s.find("f"), s.rfind("f"))
elif s.find("f") == 0:
    print(s.find("f"))
else:
    print(s.find("f"))
