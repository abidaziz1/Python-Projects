from moviepy.editor import VideoFileClip

def convert_video(input_path, output_path):
    """
    Convert a video from one format to another.
    
    Args:
    input_path (str): Path to the input video file.
    output_path (str): Path to the output video file with the desired format extension.
    """
    # Load the video file
    clip = VideoFileClip(input_path)
    
    # Write the video file to the new format
    clip.write_videofile(output_path, codec='libx264')

def main():
    input_path = 'path/to/input/video.mp4'  # Specify the path to the input video
    output_path = 'path/to/output/video.avi'  # Specify the path to the output video with desired format
    
    # Convert the video
    convert_video(input_path, output_path)
    
    print(f'Converted {input_path} to {output_path}')

if __name__ == "__main__":
    main()
