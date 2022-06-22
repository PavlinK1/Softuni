from collections import deque

def get_key(val, mix):
    for key, value in val.items():
         if value == mix:
             return key


bomb_types = {
                "Datura Bombs": 40,
                "Cherry Bombs": 60,
                "Smoke Decoy Bombs": 120

             }


bomb_effects = deque(map(int, input().split(", ")))
bomb_casings = deque(map(int, input().split(", ")))

Datura_Bombs = 0
Cherry_Bombs = 0
Smoke_Decoy_Bombs = 0
success = False

while bomb_effects and bomb_casings:
   first_effect = bomb_effects[0]
   last_casing = bomb_casings[-1]
   mix = first_effect + last_casing
   if mix in bomb_types.values():
       bomb = get_key(bomb_types, mix)
       bomb_effects.popleft()
       bomb_casings.pop()
       if bomb == "Datura Bombs":
           Datura_Bombs += 1
       elif bomb == "Cherry Bombs":
           Cherry_Bombs += 1
       elif bomb == "Smoke Decoy Bombs":
           Smoke_Decoy_Bombs += 1
       bomb = ""
       if Datura_Bombs > 2 and Cherry_Bombs > 2 and Smoke_Decoy_Bombs > 2:
           success = True
           break
   else:
       if bomb_casings[-1] != 0:
          bomb_casings[-1] -= 5
       elif bomb_casings[-1] == 0:
           bomb_casings.pop()

if success:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    bomb_effects = list(bomb_effects)
    print("Bomb Effects:", end=" ")
    print(*bomb_effects, sep=", ")
elif not bomb_effects:
    print("Bomb Effects: empty")
if bomb_casings:
    bomb_casings = list(bomb_casings)
    print("Bomb Casings:", end=" ")
    print(*bomb_casings, sep=", ")
elif not bomb_casings:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {Cherry_Bombs}")
print(f"Datura Bombs: {Datura_Bombs}")
print(f"Smoke Decoy Bombs: {Smoke_Decoy_Bombs}")