def main():
    with open("input17") as f:
        line = f.readlines()[0].rstrip("\n").lstrip("target area: ")
        x, y = line.split(", ")
        x_min_str, x_max_str = x.lstrip("x=").split("..")
        y_min_str, y_max_str = y.lstrip("y=").split("..")

        x_min = int(x_min_str)
        x_max = int(x_max_str)
        y_min = int(y_min_str)
        y_max = int(y_max_str)

        # There's always a step when the projectile will end up on y=0 again.
        # This means that the highest y distance we can move in the y direction
        # and still hit the target is y_min. We can work in reverse to figure
        # out the max y from there.
        y_now = y_min
        y_velocity = y_min
        while y_velocity != 0:
            y_now -= y_velocity
            y_velocity += 1

        print(f"P1: {y_now}")


if __name__ == "__main__":
    main()
