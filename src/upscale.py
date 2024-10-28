import ffmpeg
from .save import save_file

def upscale(input_file, output_file, resolution='720p'):
    """Upscale the video to the specified resolution (default 720p)."""
    try:
        output_extension = output_file.split('.')[-1].lower()
        normalized_output_file = save_file(output_file)

        resolutions = { 
            '480p': (854, 480),
            '720p': (1280, 720),
            '1080p': (1920, 1080)
        }

        if resolution not in resolutions:
            raise ValueError("Resolution must be '480p', '720p' or '1080p'.")

        width, height = resolutions[resolution]

        if output_extension in ['mp4', 'mkv']:
            vcodec = 'libx264'
            acodec = 'aac'
        elif output_extension == 'avi':
            vcodec = 'mpeg4'
            acodec = 'mp3'
        else:
            raise ValueError(f"Unsupported output format: .{output_extension}")

        ffmpeg.input(input_file).output(
            normalized_output_file,
            vcodec=vcodec,
            acodec=acodec,
            vf=f'scale={width}:{height}',
            preset='fast',
            map_metadata=-1
        ).run(overwrite_output=True)

        print(f"Upscaled {input_file} to {resolution} as {normalized_output_file}.")
    except ffmpeg.Error as e:
        print(f"Error in upscaling to {output_extension.upper()}:", e.stderr.decode())
    except ValueError as e:
        print(e)