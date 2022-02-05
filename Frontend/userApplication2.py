# FOR COLORAMA
import colorama
from colorama import Fore
from pyfiglet import Figlet
from Backend import baseCrawler

colorama.init()

class UI:

    def __init__(self, user) -> None:
        self.crawler = baseCrawler.crawl(user)
        self.menu()

    def heading(self, txt, color="Blue"):
        f = Figlet(font='slant')
        word = txt
        CLEAR_SCREEN = '\033[2J'
        if color.lower() == "red":
            col = Fore.RED
        elif color.lower() == "blue":
            col = Fore.BLUE
        elif color.lower() == "green":
            col = Fore.GREEN
        else:
            col = Fore.RED
        print(CLEAR_SCREEN + col + f.renderText(word) + Fore.RESET)


    def menu(self):
        ch = 0
        error = 0
        while ch != 3:
            if error <= 3:
                print("1. Get product details\n2. Sell a product\n3. Logout")
                ch = int(input("Enter your choice: "))

                if ch == 1:
                    self.heading("Product Details")
                    self.crawler.select_product()
                elif ch == 2:
                    self.heading("Sell A Product")
                    self.crawler.profit_calc()
                elif ch == 3:
                    self.heading("Logout", "red")
                    print("Logging out...")
                else:
                    print("\nInvalid choice!\n")
                    error += 1
                    continue
            else:
                print("\nMaximum chances exceeded!\n")
                if input("Type 'I am not a bot' to continue: ").lower() == "i am not a bot":
                    self.menu()
                else:
                    self.heading("Logout", "red")
                    print("Bot detected... Logging out!")



