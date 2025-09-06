#!/usr/bin/env python3

from src.demo import Demo
from src.logger import get_logger


def main() -> None:
    """Main application entry point."""
    logger = get_logger("main")

    logger.info("Application started")

    # Run demo
    demo = Demo()
    demo.run()

    logger.info("Application finished")


if __name__ == "__main__":
    main()
