from moviepy import (
    ImageClip,
    TextClip,
    ColorClip,
    CompositeVideoClip
)

# =========================
# 設定
# =========================

image_path = "background.jpg"
output_path = "output.mp4"

VIDEO_W = 1280
VIDEO_H = 720

DURATION = 15

FONT_PATH = "C:/Windows/Fonts/meiryo.ttc"

# 字幕データ
subtitles = [
    ("今日は良い天気ですね。", 0, 3),
    ("MoviePyで字幕を表示しています。", 3, 6),
    ("20文字程度でも問題ありません。", 6, 9),
    ("複数文章を順番に表示できます。", 9, 12),
]

font_path = "C:/Windows/Fonts/meiryo.ttc"

# =========================
# 背景
# =========================

bg = (
    ImageClip(image_path)
    .with_duration(DURATION)
    .resized(height=VIDEO_H)
)

# 背景を横移動 2枚をループ
bg_w = bg.w # 画像幅取得

# =========================
# 1枚目
# =========================

def move1(t):
    speed = 50  # px/sec
    x = -(speed * t) % bg_w
    return (x - bg_w, 0)

bg1 = bg.with_position(move1)

# =========================
# 2枚目
# =========================

def move2(t):
    speed = 50
    x = -(speed * t) % bg_w
    return (x, 0)

bg2 = bg.with_position(move2)

# =========================
# 半透明字幕帯
# =========================

subtitle_box_h = 500

subtitle_box = (
    ColorClip(
        size=(VIDEO_W, subtitle_box_h),
        color=(18, 59, 102)
    )
    .with_opacity(0.78)
    .with_duration(DURATION)
    .with_position((0, (VIDEO_H - subtitle_box_h) // 2))
)

# =========================
# 字幕
# =========================


subtitle_clips = []

for text, start, end in subtitles:

    txt_clip = TextClip(
        text=text,
        font=FONT_PATH,
        font_size=50,
        color="white",
        method="caption",
        size=(1000, None)
    ).with_position(("center", 580)) \
     .with_start(start) \
     .with_end(end)

    subtitle_clips.append(txt_clip)

# =========================
# 合成
# =========================

final = CompositeVideoClip(
    [bg1,bg2, subtitle_box] + subtitle_clips,
    size=(VIDEO_W, VIDEO_H)
)

# =========================
# 出力
# =========================

final.write_videofile(
    output_path,
    fps=30,
    codec="libx264",
    audio=False
)