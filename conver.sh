ffmpeg -i '/mnt/data/temp/Game.of.Thrones.S01.720p.BluRay.x264.ShAaNiG/Game.of.Thrones.S01E02.720p.BluRay.450MB.ShAaNiG.com.mkv' -codec copy /home/john/nfs/GameOfT/S01E02.mp4
ffmpeg -i '/mnt/data/temp/Game.of.Thrones.S01.720p.BluRay.x264.ShAaNiG/sub/1/Game.of.Thrones.S01E02.The.Kingsroad.1080p.BluRay.10Bit.x265.Opus-CommIE.ass' 2.vtt
ffmpeg -i inputfile -map 0 -c:a copy -c:s copy -c:v libx264 output.mkv
ffmpeg -i '/home/john/nfs/gale/[YMDR][刀剑神域外传][Gun Gale Online][2018][03][粉丝来信][1080P][HEVC][JAP][GB][MP4][ViPHD].mp4' -codec copy -c:v libx264 '/home/john/nfs/gale/[Gun Gale Online][03].mp4
