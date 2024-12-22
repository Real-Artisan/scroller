import time
import random
import argparse
import pyautogui

def auto_scroll_randomly(seconds):
    """
    Scrolls the screen up and down randomly for the specified duration.

    :param seconds: Duration to keep scrolling in seconds.
    """
    print(f"Starting random scrolling for {seconds} seconds.")
    start_time = time.time()

    while time.time() - start_time < seconds:
        # Choose a random direction and scroll amount
        direction = random.choice(["up", "down"])
        scroll_amount = random.randint(5, 50)  # Random scroll amount
        interval = random.uniform(0.5, 2.0)   # Random interval between scrolls

        # Scroll up or down
        pyautogui.scroll(scroll_amount if direction == "up" else -scroll_amount)
        print(f"Scrolled {direction} by {scroll_amount} units. Next in {interval:.2f}s.")
        time.sleep(interval)

    print("Random scrolling completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A CLI tool for random automatic scrolling.")
    parser.add_argument(
        "-s", "--seconds",
        type=int,
        required=True,
        help="Duration in seconds for the random scrolling."
    )
    args = parser.parse_args()

    auto_scroll_randomly(args.seconds)
