def annoy(discs, start_peg, middle_peg, goal_peg):
    if discs >= 1:
        # move tower of size n - 1 to middle_peg
        annoy(discs - 1, start_peg, goal_peg, middle_peg)

        # move base disc from start_peg to goal_peg
        print("Move disc", discs, "from peg", start_peg, "to peg", goal_peg)

        # move tower from middle_peg to goal_peg
        annoy(discs - 1, middle_peg, start_peg, goal_peg)

annoy(100, "A", "B", "C")

64800 = 12 x 3600