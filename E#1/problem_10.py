t = int(input("Enter the value : "))

i = 1

while i <= t:

    opposition_run, team_run, ball_left = map(int, input("Enter the number : ").split())
    current_rr = (team_run / ((300 - ball_left) / 6))
    required_rr = (((opposition_run + 1) - team_run) / (ball_left / 6))

    if opposition_run < team_run:
        required_rr = 0.00
    print(f"{current_rr:.2f}", end=" ")
    print(f"{required_rr:.2f}")

    """
    python 3.5 not allow f string 
    """

    i = i + 1
