from moviepy import VideoFileClip
from pathlib import Path

def main(input_file, output_file_stem):
    clip1 = VideoFileClip(input_file)

    top = 124
    clip2 = clip1.cropped(x1=0, y1=top, x2=320, y2=top+220)

    clip2.write_videofile(f"{output_file_stem}.mp4")
    clip2.write_gif(f"{output_file_stem}.gif", fps=20)

if __name__=='__main__':
    movie_file = Path('./data/mv1.mp4')
    out_file_stem = str(movie_file.parent / f"{movie_file.stem}_out")

    main(str(movie_file), out_file_stem)

    