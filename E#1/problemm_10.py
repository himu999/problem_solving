t = int(input())

i = 1

while i <= t:
    opposition_run, team_run, ball_left = map(int, input().split())
    current_rr = (team_run / ((300 - ball_left) / 6))
    required_rr = (((opposition_run + 1) - team_run) / (ball_left / 6))

    if opposition_run < team_run:
        required_rr = 0.00

    print("{:.2f}".format(current_rr), "{:.2f}".format(required_rr))

    i = i + 1
