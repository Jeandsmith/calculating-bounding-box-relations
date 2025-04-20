
if __name__ == "__main__":

    ENABLE_DARK_THEME = 0b00001

    config = 0

    # DARK theme is enabled?
    print (bool(config & ENABLE_DARK_THEME))

    # ENABLED the config
    config |= ENABLE_DARK_THEME

    print (bool(config & ENABLE_DARK_THEME))
