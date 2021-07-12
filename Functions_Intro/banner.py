def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Draws a banner from input string
    Args:
        text:
        screen_width:
    Raises valueError: when the text is longer than the input width

    """
    if len(text) > screen_width - 4:
        # print("EEK!", 60)
        # print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH", 60)
        raise ValueError(f"String {text} is larger then specified width {screen_width}", 60)

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = f"**{centered_text}**"
        print(output_string)


banner_text("*", 60)
banner_text("alma", 60)
banner_text("dejóóóóóóóó", 15)
banner_text("*", 60)
banner_text(screen_width=60)


