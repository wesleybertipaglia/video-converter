import ffmpeg
from normalize import normalize_name

def convert(input_file, output_file):
    """Convert any video format to a specified format with H.264 (if compatible) codec."""
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
            preset='fast',
            map_metadata=-1
        ).run(overwrite_output=True)
        
        print(f"Converted {input_file} to {output_extension.upper()} format as {normalized_output_file}.")
    except ffmpeg.Error as e:
        print(f"Error in converting to {output_extension.upper()}:", e.stderr.decode())
    except ValueError as e:
        print(e)
