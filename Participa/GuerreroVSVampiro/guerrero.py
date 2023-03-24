import random

listaAtaques = None
y = None
ataqueGuerrero = None
ataqueVampiro = None
vidaVampiro = None
ataqueIA = None
ataqueElegidoIA = None
ataqueElegido = None
randomAux = None
da_C3_B1a = None
resultadoDefensa = None
vidaGuerrero = None
ataque = None
combateActivo = None
textoResultado = None
intentoDefensa = None
probabilidad = None
limiteEnergiaGuerrero = None
limiteEnergiaVampiro = None
pocionActiva = None
da_C3_B1oTeorico = None
contadorPocion = None
reduccionDefensa = None
posibilidadesDefensa = None

# Describe esta función...
def SeleccionIA():
  global listaAtaques, y, ataqueGuerrero, ataqueVampiro, vidaVampiro, ataqueIA, ataqueElegidoIA, ataqueElegido, randomAux, da_C3_B1a, resultadoDefensa, vidaGuerrero, ataque, combateActivo, textoResultado, intentoDefensa, probabilidad, limiteEnergiaGuerrero, limiteEnergiaVampiro, pocionActiva, da_C3_B1oTeorico, contadorPocion, reduccionDefensa, posibilidadesDefensa
  ataqueIA = random.randint(1, 3)
  if ataqueIA == 1:
    probabilidad = 90
    da_C3_B1oTeorico = 5
  elif ataqueIA == 2:
    probabilidad = 60
    da_C3_B1oTeorico = 10
  elif ataqueIA == 3:
    probabilidad = 40
    da_C3_B1oTeorico = 30
  else:
    print('Error en seleccion IA')
  ataqueElegidoIA = [da_C3_B1oTeorico, probabilidad]
  return ataqueElegidoIA

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)

# Describe esta función...
def SeleccionAtaque():
  global listaAtaques, y, ataqueGuerrero, ataqueVampiro, vidaVampiro, ataqueIA, ataqueElegidoIA, ataqueElegido, randomAux, da_C3_B1a, resultadoDefensa, vidaGuerrero, ataque, combateActivo, textoResultado, intentoDefensa, probabilidad, limiteEnergiaGuerrero, limiteEnergiaVampiro, pocionActiva, da_C3_B1oTeorico, contadorPocion, reduccionDefensa, posibilidadesDefensa
  if vidaGuerrero >= limiteEnergiaGuerrero:
    ataque = None
    while ataque != 1 and ataque != 2 and ataque != 3:
      ataque = float(text_prompt('Elija un ataque (numero): ' + str(listaAtaques)))
    probabilidad = 0
    da_C3_B1oTeorico = 0
    if ataque == 1:
      probabilidad = 50
      da_C3_B1oTeorico = 7
    elif ataque == 2:
      probabilidad = 25
      da_C3_B1oTeorico = 15
    elif ataque == 3:
      probabilidad = 12
      da_C3_B1oTeorico = 30
    ataqueElegido = [da_C3_B1oTeorico, probabilidad]
  else:
    ataqueElegido = [0, 0]
  return ataqueElegido

# Describe esta función...
def PruebaEfectividad(y):
  global listaAtaques, ataqueGuerrero, ataqueVampiro, vidaVampiro, ataqueIA, ataqueElegidoIA, ataqueElegido, randomAux, da_C3_B1a, resultadoDefensa, vidaGuerrero, ataque, combateActivo, textoResultado, intentoDefensa, probabilidad, limiteEnergiaGuerrero, limiteEnergiaVampiro, pocionActiva, da_C3_B1oTeorico, contadorPocion, reduccionDefensa, posibilidadesDefensa
  randomAux = random.randint(1, 100)
  if randomAux <= y:
    da_C3_B1a = True
  else:
    da_C3_B1a = False
  return da_C3_B1a

# Describe esta función...
def CombateActivo():
  global listaAtaques, y, ataqueGuerrero, ataqueVampiro, vidaVampiro, ataqueIA, ataqueElegidoIA, ataqueElegido, randomAux, da_C3_B1a, resultadoDefensa, vidaGuerrero, ataque, combateActivo, textoResultado, intentoDefensa, probabilidad, limiteEnergiaGuerrero, limiteEnergiaVampiro, pocionActiva, da_C3_B1oTeorico, contadorPocion, reduccionDefensa, posibilidadesDefensa
  if vidaGuerrero <= 0:
    combateActivo = False
    textoResultado = 'GAME OVER - El vampiro te ha matado!'
  elif vidaVampiro <= 0:
    combateActivo = False
    textoResultado = 'VICTORIA - Has devuelto al Vampiro al inframundo!'

# Describe esta función...
def AtaqueGuerrero(ataqueGuerrero):
  global listaAtaques, y, ataqueVampiro, vidaVampiro, ataqueIA, ataqueElegidoIA, ataqueElegido, randomAux, da_C3_B1a, resultadoDefensa, vidaGuerrero, ataque, combateActivo, textoResultado, intentoDefensa, probabilidad, limiteEnergiaGuerrero, limiteEnergiaVampiro, pocionActiva, da_C3_B1oTeorico, contadorPocion, reduccionDefensa, posibilidadesDefensa
  if vidaGuerrero >= limiteEnergiaGuerrero:
    if PruebaEfectividad(ataqueGuerrero[-1]):
      vidaVampiro = vidaVampiro - ataqueGuerrero[0]
      print(''.join([str(x2) for x2 in ['Ataque efectivo. El Vampiro recibe ', ataqueGuerrero[0], ' puntos de daño! Le quedan ', vidaVampiro, ' puntos de vida.']]))
      if vidaVampiro < limiteEnergiaVampiro and vidaVampiro > 0:
        print('Has dejado al Vampiro inconsciente.')
    else:
      print('Has fallado! El Vampiro no recibe daño.')
  else:
    vidaGuerrero = vidaGuerrero + 2
    print(''.join([str(x3) for x3 in ['Estas inconsciente, no puedes atacar. 2 puntos de vida añadidos. Tienes ', vidaGuerrero, ' puntos de vida.']]))

# Describe esta función...
def AtaqueVampiro(ataqueVampiro):
  global listaAtaques, y, ataqueGuerrero, vidaVampiro, ataqueIA, ataqueElegidoIA, ataqueElegido, randomAux, da_C3_B1a, resultadoDefensa, vidaGuerrero, ataque, combateActivo, textoResultado, intentoDefensa, probabilidad, limiteEnergiaGuerrero, limiteEnergiaVampiro, pocionActiva, da_C3_B1oTeorico, contadorPocion, reduccionDefensa, posibilidadesDefensa
  if vidaVampiro >= limiteEnergiaVampiro:
    if PruebaEfectividad(ataqueVampiro[-1]):
      if Defensa():
        vidaGuerrero = vidaGuerrero - (ataqueVampiro[0] - reduccionDefensa)
        print(''.join([str(x4) for x4 in ['Ataque reducido. Recibes ', ataqueVampiro[0] - reduccionDefensa, ' puntos de daño! Te quedan ', vidaGuerrero, ' puntos de vida.']]))
      else:
        vidaGuerrero = vidaGuerrero - ataqueVampiro[0]
        print(''.join([str(x5) for x5 in ['El Vampiro te ha dado. Recibes ', ataqueVampiro[0], ' puntos de daño! Te quedan ', vidaGuerrero, ' puntos de vida.']]))
      if vidaGuerrero < limiteEnergiaGuerrero and vidaGuerrero > 0:
        print('Te has desmayado!')
    else:
      print('El Vampiro falla! No recibes daño.')
  else:
    vidaVampiro = vidaVampiro + 2
    print(''.join([str(x6) for x6 in ['El Vampiro esta inconsciente. No puede atacar. El vampiro se cura 2 puntos de vida. Le quedan ', vidaVampiro, ' puntos de vida.']]))

# Describe esta función...
def FinCombate():
  global listaAtaques, y, ataqueGuerrero, ataqueVampiro, vidaVampiro, ataqueIA, ataqueElegidoIA, ataqueElegido, randomAux, da_C3_B1a, resultadoDefensa, vidaGuerrero, ataque, combateActivo, textoResultado, intentoDefensa, probabilidad, limiteEnergiaGuerrero, limiteEnergiaVampiro, pocionActiva, da_C3_B1oTeorico, contadorPocion, reduccionDefensa, posibilidadesDefensa
  print(textoResultado)

# Describe esta función...
def Pocion():
  global listaAtaques, y, ataqueGuerrero, ataqueVampiro, vidaVampiro, ataqueIA, ataqueElegidoIA, ataqueElegido, randomAux, da_C3_B1a, resultadoDefensa, vidaGuerrero, ataque, combateActivo, textoResultado, intentoDefensa, probabilidad, limiteEnergiaGuerrero, limiteEnergiaVampiro, pocionActiva, da_C3_B1oTeorico, contadorPocion, reduccionDefensa, posibilidadesDefensa
  if pocionActiva == 1:
    if contadorPocion == 0:
      vidaGuerrero = 150
      print(''.join([str(x7) for x7 in ['La pocion ha funcionado. Vuelves a tener ', vidaGuerrero, ' puntos de vida.']]))
      contadorPocion = 2
      pocionActiva = 0
    else:
      print(''.join([str(x8) for x8 in ['Estas tomando una pocion. No puedes atacar durante ', contadorPocion, ' turnos.']]))
      contadorPocion = contadorPocion - 1
  else:
    if vidaGuerrero < 150:
      pocionActiva = float(text_prompt(''.join([str(x9) for x9 in ['Te quedan ', vidaGuerrero, ' puntos de vida. ¿Quieres tomar una pocion? (Si: 1, No: 0)']])))
      while pocionActiva != 1 and pocionActiva != 0:
        pocionActiva = float(text_prompt(''.join([str(x10) for x10 in ['Te quedan ', vidaGuerrero, ' puntos de vida. ¿Quieres tomar una pocion? (Si: 1, No: 0)']])))
      if pocionActiva == 1:
        print('Estas tomando una pocion. No podras atacar en 3 turnos.')

# Describe esta función...
def Defensa():
  global listaAtaques, y, ataqueGuerrero, ataqueVampiro, vidaVampiro, ataqueIA, ataqueElegidoIA, ataqueElegido, randomAux, da_C3_B1a, resultadoDefensa, vidaGuerrero, ataque, combateActivo, textoResultado, intentoDefensa, probabilidad, limiteEnergiaGuerrero, limiteEnergiaVampiro, pocionActiva, da_C3_B1oTeorico, contadorPocion, reduccionDefensa, posibilidadesDefensa
  if pocionActiva == 0:
    intentoDefensa = None
    while intentoDefensa != 1 and intentoDefensa != 0:
      intentoDefensa = float(text_prompt('¿Quiere intentar defenderse? (Si: 1, No: 0)'))
    if intentoDefensa == 1:
      if PruebaEfectividad(posibilidadesDefensa):
        resultadoDefensa = True
      else:
        resultadoDefensa = False
        print('Defensa fallida.')
    elif intentoDefensa == 0:
      resultadoDefensa = False
  else:
    resultadoDefensa = False
  return resultadoDefensa


listaAtaques = ''.join([str(x) for x in ['Arma 1: 7pts - 50% /', 'Arma 2: 15pts - 25% /', 'Arma 3: 30pts - 12%']])
vidaVampiro = 60
vidaGuerrero = 150
combateActivo = True
textoResultado = ''
reduccionDefensa = 5
posibilidadesDefensa = 80
limiteEnergiaGuerrero = 30
limiteEnergiaVampiro = 20
pocionActiva = 0
contadorPocion = 2
while combateActivo:
  if combateActivo and pocionActiva == 0:
    AtaqueGuerrero(SeleccionAtaque())
    CombateActivo()
  if combateActivo:
    AtaqueVampiro(SeleccionIA())
    CombateActivo()
  if combateActivo:
    Pocion()
FinCombate()