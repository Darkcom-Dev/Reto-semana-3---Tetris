import random

def move(key):
  '''
    Retorna un estado para poder mover el bloque con fluides
    Parameters
    ----------
    key : Integer
      Codigo de la tecla entrada
    Returns
    ----------
    code : String
      Codigo que puede ser 'left', 'right', 'down', 'turn', devolver 
      caracteres vacios en caso de no ser ningun excenario
  '''
  keyCode = str()
  if key == 79:
    keyCode = 'right'
  elif key == 80:
    keyCode = 'left'
  elif key == 82:
    keyCode = 'turn'
  elif key == 81:
    keyCode = 'down'
  
  return keyCode


def set_pause(key):
  '''
    Retorna un booleando true, si la tecla de pausa se preciona.
    Parameters
    ----------
    key : Integer
      Codigo de la tecla entrada
    Returns
    ----------
    code : Boolean
      True si la tecla de pausa es presionada
  '''
  
  return 19 == key == 72 


def score_message(score):
  '''
    Retorna el texto y color del mensaje de acuerdo al puntaje del jugador.
    Parameters

    - Para puntuacion mayor o igual a 10 y menor a 15: "Meh" con un color Rojo: 231, verde: 76, azul: 60
    - Para puntuacion mayor o igual a 15 y menor a 25: "Algo es algo" con un color Rojo: 245, verde: 176, azul: 65
    - Para puntuacion mayor o igual a 25 y menor a 50: "Algo mejor" con un color Rojo: 235, verde: 152, azul: 78
    - Para puntuacion mayor o igual a 50 y menor a 75: "No tan mal" con un color Rojo: 93, verde: 173, azul: 226
    - Para puntuacion mayor o igual a 75 y menor a 100: "Mucho mejor" con un color Rojo: 46, verde: 204, azul: 113
    - Para puntuacion mayor o igual a 100: "WOW" con un color al azar entre 0 y 255  para cada tono de color
    ----------
    score : Integer
      Puntaje de la partida
    Returns
    ----------
    message : String
      Texto para el jugador
    color: Truple
      Codificacion RGB para mostrar colores en pantalla
  '''
  mensaje = str()
  color = tuple()
  if score <= 10 and score < 15:
    mensaje = 'Meh'
    color = (231,76,60)
  elif score >= 15 and score < 25:
    mensaje = 'Algo es algo'
    color = (245,152,65)
  elif score >= 25 and score < 50:
    mensaje = 'Algo mejor'
    color = (235,152,78)
  elif score >= 50 and score < 75:
    mensaje = 'No tan mal'
    color = (93,173,226)
  elif score >= 75 and score < 100:
    mensaje = 'Mucho mejor'
    color = (46,204,113)
  elif score >= 100:
    mensaje = 'WOW'
    color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    print(color)
  else:
    mensaje = 'Error'
    color = (0,0,0)
  return mensaje, color
