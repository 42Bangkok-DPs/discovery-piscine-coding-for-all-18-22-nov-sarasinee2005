if number > 0:
            print("This number is positive.")
        elif number < 0:
            print("This number is negative.")
        else:
            print("This number is both positive and negative.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if name == "main":
    main()