"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    # Create an empty dictionary to store legendary MLG players.
    # Each username is a key, and their dankness level is the value.
    # Python dictionaries use hashing to quickly locate stored data.
    # Basically, finding memes at the speed of a 360 no-scope.

    mlg_players = {}

    mlg_players["xX_QuickScope_Xx"] = 9001
    mlg_players["ShrekIsLove"] = 420
    mlg_players["JohnCE$na"] = 9999
    mlg_players["DogeMuchWow"] = 1337
    mlg_players["DoritoDestroyer"] = 360

    print("MLG players successfully deployed:")
    print(mlg_players)
    print("WOW. SUCH HASH TABLE. MUCH EFFICIENCY.")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    # Looking up a key retrieves its associated dankness level.
    # Hash tables make this efficient without searching every player.
    # Even if John Cena is invisible, his data is still accessible.


    print("John CE$na's dankness level:", mlg_players["JohnCE$na"])
    print("Shrek's dankness level:", mlg_players["ShrekIsLove"])
    print("AND HIS NAME IS JOHN CE$NA!!!")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("Before the Mountain Dew power-up:", mlg_players)

    # Assigning a new value to an existing key replaces the old one.
    #   QuickScope drank three Mountain Dews and achieved enlightenment.
    # His dankness level has officially exceeded 9000.

    mlg_players["xX_QuickScope_Xx"] = 99999

    print("After the Mountain Dew power-up:", mlg_players)
    print("IT'S OVER 9000!!!")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("Before getting absolutely rekt:", mlg_players)

    # The del keyword removes a key and its associated value.
    # DoritoDestroyer got 360 no-scoped and was removed from the lobby.
    # Press F to pay respects.

    del mlg_players["DoritoDestroyer"]

    print("After getting absolutely rekt:", mlg_players)
    print("F IN THE CHAT. DORITODESTROYER HAS BEEN ELIMINATED.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    # Edge Case 1: Look up a player who does not exist.
    # The get() method prevents a KeyError for missing keys.
    # You cannot retrieve a player who was never in the lobby.

    missing = mlg_players.get("IlluminatiConfirmed", "404 MEME NOT FOUND")
    print("Searching for Illuminati:", missing)

    # Edge Case 2: Attempt to delete a nonexistent player.
    # pop() with a default message avoids crashing the program.
    # Can't eliminate someone who already rage quit.

    removed = mlg_players.pop("PepeTheFrog", "PLAYER ALREADY REKT")
    print("Attempting to eliminate Pepe:", removed)

    # Edge Case 3: Assigning a value to a missing key adds a new entry.
    # A new challenger has entered the MLG arena.

    mlg_players["MLG_Noscoper_420"] = 6969

    print("New player joined the lobby:", mlg_players)
    print("AIRHORNS INTENSIFY!!!")
    print("ILLUMINATI CONFIRMED.")

    print("\n=== FINAL MLG LEADERBOARD ===")

    # Display all remaining players and their dankness levels.
    for player, dankness in mlg_players.items():
        print(player, "- Dankness Level:", dankness)

    print("\nMISSION COMPLETE. 360 NO-SCOPE. GG EZ.")



if __name__ == "__main__":
    main()