# --- Define your functions below! ---
#author: Ajene-Ayele
#file: chatbot2.py
#desc: Example of return statements
#created: 6/19/19



# --- Put your main program below! ---
def main():
    print("lets get to know each other!", "whats our name?")	 
  while True:	
    answer = input("(name) ")
    def pick_a_greeting(name):
        greetings = ["hello", "whats up", "hi"]

        rand = random()

        greet = rand.choice(greetings) +"," +name +"!"
        

    


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
