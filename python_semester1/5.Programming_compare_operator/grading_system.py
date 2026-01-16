# gs stands for grading system
""""rule 
A : 95 - 100
B : 85 - 94
C : 75 - 84
D : 65 - 74
E : 50 - 64
F : below 50

"""
import turtle as t

#usts stands for user input score

usts = int(t.numinput("Score system", "Please enter your score: ")) #value type is float


# gs stands for grading system

def gs(score: int):
    t.penup() # to prevent it from drawing?
    t.hideturtle()

    if score < 0 or score > 100:
        result = "Are you a fucking clown?"

    elif score >= 95:
        result = "You got A"

    elif score >= 85:
        result = "You got B"
    
    elif score >= 75:
        result = "You got C"

    elif score >= 65:
        result = "You got D"
    
    elif score >= 50:
        result = "You got E"
    
    else:
        result = "You got F, study harder bro"

    t.write(result, font=("Arial", 40, "bold"), align="center")
    

if usts is not None:
    gs(usts)

t.done()

#this should be in local file too