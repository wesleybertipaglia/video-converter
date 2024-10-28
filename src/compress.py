import ffmpeg
from normalize import normalize_name

def compress(input_file, output_file, crf=28):
    """Compress the video to reduce file size with specified CRF (default 28)."""
    try:
        output_extension = output_file.split('.')[-1].lower()
        normalized_output_file = f"{normalize_name(output_file)}.{output_extension}"

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
            crf=crf,
            preset='fast',
            map_metadata=-1
        ).run(overwrite_output=True)

        print(f"Compressed {input_file} with CRF={crf} as {normalized_output_file}.")
    except ffmpeg.Error as e:
        print(f"Error in compressing to {output_extension.upper()}:", e.stderr.decode())
    except ValueError as e:
        print(e)
