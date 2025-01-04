def main() -> None:
    # Set starting code and position
    code = 20151125
    pos = (1, 1)

    # Generate codes until target position is reached
    while pos != (3010, 3019):
        # Calculate next code
        code = (code * 252533) % 33554393

        # Go to next position
        if pos[0] != 1:
            pos = (pos[0] - 1, pos[1] + 1)
        else:
            pos = (pos[1] + 1, 1)

    # Display results
    print(f"Code: {code}")


if __name__ == "__main__":
    main()
