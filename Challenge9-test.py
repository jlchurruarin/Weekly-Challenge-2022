import unittest
from Challenge9 import morse_encode_decode

class TestMorseEncodeDecode(unittest.TestCase):

    def test_morse_encode(self):
        self.assertEqual(morse_encode_decode("102"),".---- ----- ..---")
        self.assertEqual(morse_encode_decode("Hola"),".... --- .-.. .-")
        self.assertEqual(morse_encode_decode("Hola mundo"),
                         ".... --- .-.. .-  -- ..- -. -.. ---")
        self.assertEqual(morse_encode_decode("Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
                         ".-.. --- .-. . --  .. .--. ... ..- --  -.. --- .-.. --- .-.  ... .. -  .- -- . - --..--  -.-. --- -. ... . -.-. - . - ..- .-.  .- -.. .. .--. .. ... -.-. .. -. --.  . .-.. .. - .-.-.-")
                         
        self.assertEqual(morse_encode_decode("Prueba con numeros, por ejemplo 123"),
                         ".--. .-. ..- . -... .-  -.-. --- -.  -. ..- -- . .-. --- ... --..--  .--. --- .-.  . .--- . -- .--. .-.. ---  .---- ..--- ...--")
        
        with self.assertRaises(Exception):
            morse_encode_decode("Probamos caracteres erroneos, como por ejemplo: ¿")

    def test_morse_decode(self):
        self.assertEqual(morse_encode_decode(".---- ..... ..--- ....-"),"1524")
        self.assertEqual(morse_encode_decode(".--. -.-- - .... --- -."),"Python".upper())
        self.assertEqual(morse_encode_decode("- .-- ---  .-- --- .-. -.. ..."),
                         "Two words".upper())
        self.assertEqual(morse_encode_decode(".-.. --- .-. . --  .. .--. ... ..- --  -.. --- .-.. --- .-.  ... .. -  .- -- . - --..--  -.-. --- -. ... . -.-. - . - ..- .-.  .- -.. .. .--. .. ... -.-. .. -. --.  . .-.. .. - .-.-.-  .--. . .-.. .-.. . -. - . ... --.- ..- .  -.-. --- -. ... . -.-. - . - ..- .-. .-.-.-"),
                         "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque consectetur.".upper())
        self.assertEqual(morse_encode_decode(".-.. --- .-. . --  .. .--. ... ..- --  -.. --- .-.. --- .-.  ... .. -  .- -- . - .-.-.-  .---- ..... -----"),
                         "Lorem ipsum dolor sit amet. 150".upper())


if __name__ == '__main__':
    unittest.main()
