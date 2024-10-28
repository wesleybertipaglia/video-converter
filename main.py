import argparse
import os
from src.convert import convert
from src.compress import compress
from src.upscale import upscale

def main():
    parser = argparse.ArgumentParser(description="Video Processing Script")
    parser.add_argument("operation", choices=["convert", "compress", "upscale"], help="Operation to perform on the video")
    parser.add_argument("input_file", type=str, help="Path to the input video file")
    parser.add_argument("output_file", type=str, help="Path for the output video file")
    parser.add_argument("--crf", type=int, default=28, help="CRF value for compression (default: 28)")
    parser.add_argument("--resolution", choices=["480p", "720p", "1080p"], default="720p", help="Resolution for upscaling (default: 720p)")

    args = parser.parse_args()

    if not os.path.isfile(args.input_file):
        print(f"Input file '{args.input_file}' does not exist.")
        return

    if args.operation == "convert":
        convert(args.input_file, args.output_file)
    elif args.operation == "compress":
        compress(args.input_file, args.output_file, crf=args.crf)
    elif args.operation == "upscale":
        upscale(args.input_file, args.output_file, resolution=args.resolution)
    else:
        print(f"Unknown operation '{args.operation}'")

if __name__ == "__main__":
    main()
