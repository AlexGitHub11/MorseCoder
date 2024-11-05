class MorseCoder:

    def __init__(self):

        self.code_dict = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.",
                "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..",
                "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.",
                "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-",
                "y":"-.--", "z":"--..", 1:".----", 2:"..---", 3:"...--", 4:"....-",
                5:".....", 6:"-....", 7:"--...", 8:"---..", 9:"----.", 0:"-----"}

    def coder(self, plain_text):
        """ Return coded data """
        for value in plain_text:
            print(self.code_dict[value], " ", end="")

    def decoder(self, cipher_text):
        """ Return morse code, enter code as CSVs """
        cipher_text = cipher_text.split(",")
        for i in cipher_text:
            cipher_text_value = i
            for key, value in self.code_dict.items():
                if value == cipher_text_value:
                    print(key, end="")



