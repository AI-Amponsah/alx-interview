#!/usr/bin/env python3

import sys
import signal

# Initialize variables
total_file_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_statistics():
    print(f'Total file size: File size: {total_file_size}')
    for status_code in sorted(status_codes_count):
        if status_codes_count[status_code] > 0:
            print(f'{status_code}: {status_codes_count[status_code]}')


# Handle keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1

        # Parse the input line
        try:
            parts = line.split()
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Check if the line matches the expected format
            if len(parts) >= 7 and parts[5] == '"GET' and parts[6].startswith('/projects/260'):
                total_file_size += file_size
                status_codes_count[status_code] += 1

        except (ValueError, IndexError):
            # Skip lines with incorrect format
            continue

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Print final statistics on keyboard interruption
    print_statistics()
    sys.exit(0)
