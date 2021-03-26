import sys
sys.setrecursionlimit(1000)

def cipher(toggle):
  if toggle == 'encode':
    text = input('enter a message: ')
    text = text.upper()
    encdDict = {
    65 : 73, 66 : 74,
    67 : 72, 68 : 80,
    69 : 75, 70 : 77,
    71 : 78, 72 : 84,
    73 : 86, 74 : 87,
    75 : 67, 76 : 69,
    77 : 70, 78 : 79,
    79 : 81, 80 : 82,
    81 : 65, 82 : 68,
    83 : 71, 84 : 83,
    85 : 88, 86 : 89,
    87 : 76, 88 : 85,
    89 : 90, 90 : 66}
    result = text.translate(encdDict)

  elif toggle == 'decode':
    text = input('enter an encoded message: ')
    text = text.upper()
    decdDict = {
    73 : 65, 74 : 66,
    72 : 67, 80 : 68,
    75 : 69, 77 : 70,
    78 : 71, 84 : 72,
    86 : 73, 87 : 74,
    67 : 75, 69 : 76,
    70 : 77, 79 : 78,
    81 : 79, 82 : 80,
    65 : 81, 68 : 82,
    71 : 83, 83 : 84,
    88 : 85, 89 : 86,
    76 : 87, 85 : 88,
    90 : 89, 66 : 90
    }
    result = text.translate(decdDict)
  print('\n', result.lower(), '\n')
  
def menu():
  global option
  print('-----E621 Cipher-----')
  print('Enter:')
  print('"encode" to encode a message')
  print('"decode" to decode a message')
  print('"info" for info about the cipher')
  print('"key" to see the transcription key')
  print('(if you want to transcribe something \nmanually for some reason)')
  print('"stop" to stop the program')
  option = input()
  option = option.lower()
  print('---------------------')
  options()

def options():
  if option == 'encode':
    cipher('encode')
    menu()

  elif option == 'decode':
    cipher('decode')
    menu()

  elif option == 'info':
    print('\n-----info-----')
    print('I came up with this because I was bored.')
    print('Starting at E, it goes forward 6, then 2, then 1, then repeat until all letters are used, so')
    print('E is K, since K is 6 letters forward from E, F is M because that is 2 letters forward from K.')
    print('(See the \'key\' tab for a better reference)')
    print('The cipher deffinitely came from the name, not the other way around.')
    print('I\'m a degenerate, okay?')
    print('UwU motherfucker. \n')
    print('-----Contact info to harass me about being a furry or something-----')
    print('Discord: ioh#4704 \n')
    menu()

  elif option == 'key':
    print('\n-----key-----')
    print('\n Eng. - A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
    print('E621 - I J H P K M N T V W C E F O Q R A D G S X Y L U Z B \n')
    menu()

  elif option == 'stop':
    print('Script ended. goodbye.')
    exit()

  else:
    print('\n Please ensure spelling is correct and that there are no unnecessary symbols. \n')
    menu()
menu()