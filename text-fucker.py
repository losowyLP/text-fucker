import fire
from random import randint


class App():
    def reverse(self, text):
        """Reverse a string of text"""
        return text[::-1]

    def caps(self, text):
        """Make a string of text uppercase"""
        return text.upper()

    def nocaps(self, text):
        """Make a string of text lowercase"""
        return text.lower()

    def randcaps(self, text):
        """Randomly make letter in a string of text upper- or lowercase, as if you're spamming the shift key for some reason."""
        result = ""
        for i in range(len(text)):
            if randint(0, 1) == 1:
                l = text[i].upper()
            else:
                l = text[i].lower()

            result = result + l

        print(result)


if __name__ == "__main__":
    app = App()
    fire.Fire(app)
